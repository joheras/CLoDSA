from __future__ import absolute_import
from builtins import str
from builtins import range
from builtins import object
from .iaugmentor import IAugmentor
from imutils import paths
from .utils.aspectawarepreprocessor import AspectAwarePreprocessor
import os
import cv2
import numpy as np
import random
from sklearn.preprocessing import LabelBinarizer


def readAndGenerateImage(image,label, transformers):
    newimage = image
    newlabel = label
    for (j, transformer) in enumerate(transformers):
        if (random.randint(0,100)>50):
            newimage,newlabel = transformer.transform(newimage,newlabel)

    return (newimage,newlabel)

# This class serves to generate images for a classification
# problem where all the images are organized by folders
# distributed by labels. Example:
# - Folder
# |- cats
#    |- image1.jpg
#    |- image2.jpg
#    |- ...
# |- dogs
#    |- image1.jpg
#    |- image2.jpg
#    |- ...
class FolderKerasLinearClassificationAugmentor(IAugmentor):

    def __init__(self,inputPath,parameters):
        IAugmentor.__init__(self)
        self.inputPath = inputPath
        # output path represents the folder where the images will be stored
        if parameters["batchSize"]:
            self.batchSize = parameters["batchSize"]
        else:
            self.batchSize = 32
        if parameters["width"]:
            self.width = parameters["width"]
        else:
            self.width = 64
        if parameters["height"]:
            self.height = parameters["height"]
        else:
            self.height = 64
        self.readImagesAndAnnotations()


    def readImagesAndAnnotations(self):
        self.imagePaths = list(paths.list_files(self.inputPath,validExts=(".jpg", ".jpeg", ".png", ".bmp",".tiff",".tif")))
        random.shuffle(self.imagePaths)
        self.numImages = len(self.imagePaths)
        self.labels = [p.split(os.path.sep)[-2] for p in self.imagePaths]
        self.classes = len([str(x) for x in np.unique(self.labels)])
        le = LabelBinarizer()
        self.labels = le.fit_transform(self.labels)


    def applyAugmentation(self,passes=np.inf):
        epochs = 0
        aap = AspectAwarePreprocessor(self.width,self.height)
        batch_features = np.zeros((self.batchSize, self.width, self.height, 3))
        batch_labels = np.zeros((self.batchSize, self.classes))
        while epochs < passes:

            for i in np.arange(0, self.numImages, self.batchSize):
                imagPaths = self.imagePaths[i:i+self.batchSize]
                labels = self.labels[i:i+self.batchSize]
                images = [cv2.imread(imagePath) for imagePath in imagPaths]
                imagesLabels = [readAndGenerateImage(image,label,self.transformers) for image,label in zip(images,labels)]
                labels = [imageLabel[1] for imageLabel in imagesLabels]
                images = [aap.preprocess(imageLabel[0]) for imageLabel in imagesLabels]
                for j in range(self.batchSize):

                    index = random.randint(0,len(images)-1)
                    batch_features[j] = images[index]
                    batch_labels[j] = labels[index]
                yield (batch_features,batch_labels)


            epochs += 1









