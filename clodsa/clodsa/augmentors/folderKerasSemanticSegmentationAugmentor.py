from __future__ import absolute_import
from builtins import zip
from builtins import object
from mahotas.demos import image_path

from .iaugmentor import IAugmentor
from imutils import paths
import os
import cv2
from joblib import Parallel, delayed
import random
import numpy as np
from .utils.aspectawarepreprocessor import AspectAwarePreprocessor

def readAndGenerateImageSegmentation(image,label,transformers):
    newimage = image
    newlabel = label
    for (j, transformer) in enumerate(transformers):
        if (random.randint(0, 100) > 50):
            newimage,newlabel = transformer.transform(newimage,newlabel)

    return (newimage,newlabel)

# This class serves to generate images for a semantic segmentation
# problem where all the images are organized in two folders called
# images and labels. Both folders must contain the same number of images
# and with the same names (but maybe different extensions). Example
# - Folder
# |- images
#    |- image1.jpg
#    |- image2.jpg
#    |- ...
# |- labels
#    |- image1.tiff
#    |- image2.tiff
#    |- ...
# where Folder/labels/image1.tiff is the annotation of the image Folder/images/image1.jpg.
# Hence, both images must have the same size.
class FolderKerasSemanticSegmentationAugmentor(IAugmentor):

    def __init__(self,inputPath,parameters):
        IAugmentor.__init__(self)
        self.inputPath = inputPath
        self.imagesPath = inputPath+"images/"
        self.labelsPath = inputPath + "labels/"
        # output path represents the folder where the images will be stored
        if parameters["labelsExtension"]:
            self.labelsExtension=parameters["labelsExtension"]
        else:
            self.labelsExtension = ".tiff"
        if parameters["width"]:
            self.width = parameters["width"]
        else:
            self.width = 64
        if parameters["height"]:
            self.height = parameters["height"]
        else:
            self.height = 64

        if parameters["batchSize"]:
            self.batchSize = parameters["batchSize"]
        else:
            self.batchSize = 32
        self.readImagesAndAnnotations()


    def readImagesAndAnnotations(self):
        self.imagePaths = list(paths.list_files(self.imagesPath,validExts=(".jpg", ".jpeg", ".png", ".bmp",".tiff",".tif")))
        self.labelPaths = list(paths.list_files(self.labelsPath,validExts=(".jpg", ".jpeg", ".png", ".bmp",".tiff",".tif")))
        self.numImages = len(self.imagePaths)
        if (len(self.imagePaths)!=len(self.labelPaths)):
            raise Exception("The number of files is different in the folder of images and in the folder of labels")



    def applyAugmentation(self,passes=np.inf):
        epochs = 0
        aap = AspectAwarePreprocessor(self.width, self.height)
        while epochs < passes:

            for i in np.arange(0, self.numImages, self.batchSize):
                imagPaths = self.imagePaths[i:i+self.batchSize]
                labPaths = self.labelPaths[i:i+self.batchSize]
                images = [aap.preprocess(cv2.imread(imagePath)) for imagePath in imagPaths]
                labels = [aap.preprocess(cv2.imread(labelPath)) for labelPath in labPaths]
                images_labels = [readAndGenerateImageSegmentation(image,label,self.transformers) for (image,label) in zip(images,labels)]
                images = [i[0] for i in images_labels]
                labels = [i[1] for i in images_labels]
                yield (images,labels)


            epochs += 1


