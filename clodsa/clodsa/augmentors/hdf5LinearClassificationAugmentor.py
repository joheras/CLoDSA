from __future__ import absolute_import
from builtins import zip
from builtins import object
from .iaugmentor import IAugmentor
from sklearn.preprocessing import LabelEncoder
from imutils import paths
import os
import cv2
from joblib import Parallel, delayed
from .utils.aspectawarepreprocessor import AspectAwarePreprocessor
from .utils.hdf5datasetwriter import HDF5DatasetWriterClassification
import progressbar

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
class HDF5LinearClassificationAugmentor(IAugmentor):

    # All images must have same width and height
    def __init__(self,inputPath,parameters):
        IAugmentor.__init__(self)
        self.inputPath = inputPath
        # output path represents the h5py file where dataset will be stored
        if parameters["outputPath"]:
            self.outputPath = parameters["outputPath"]
        else:
            raise ValueError("You should provide an output path in the parameters")

        if parameters["width"]:
            self.width = parameters["width"]
        else:
            raise ValueError("You should provide a width in the parameters")
        if parameters["height"]:
            self.width = parameters["height"]
        else:
            raise ValueError("You should provide a height in the parameters")

        self.aw = AspectAwarePreprocessor(self.width,self.height)


    def readImagesAndAnnotations(self):
        self.imagePaths = list(paths.list_files(self.inputPath,validExts=(".jpg", ".jpeg", ".png", ".bmp",".tiff",".tif")))


    def applyAugmentation(self):
        self.readImagesAndAnnotations()
        le = LabelEncoder()
        labels = [p.split(os.path.sep)[-2] for p in self.imagePaths]
        labels = le.fit_transform(labels)
        writer = HDF5DatasetWriterClassification((len(self.imagePaths)*len(self.transformers),self.width,self.height,3),
                                   self.outputPath)
        # We need to define this function outside to work in parallel.
        writer.storeClassLabels(le.classes_)
        widgets = ["Processing images: ", progressbar.Percentage(), " ",
                   progressbar.Bar(), " ", progressbar.ETA()]
        pbar = progressbar.ProgressBar(maxval=len(self.imagePaths),
                                       widgets=widgets).start()
        for i_and_imagePath in enumerate(zip(self.imagePaths,labels)):
            (i, (imagePath,label)) = i_and_imagePath
            image = cv2.imread(imagePath)
            image = self.aw.preprocess(image)
            for (j, transformer) in enumerate(self.transformers):
                newimage,newlabel = transformer.transform(image,label)
                newimage = self.aw.preprocess(newimage)
                writer.add([newimage],[newlabel])
            pbar.update(i)
        writer.close()
        pbar.finish()
