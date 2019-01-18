from __future__ import absolute_import
from builtins import zip
from builtins import object
from .iaugmentor import IAugmentor
from sklearn.preprocessing import LabelEncoder
from imutils import paths
import os
import cv2
import progressbar
from .utils.aspectawarepreprocessor import AspectAwarePreprocessor
from .utils.hdf5datasetwriter import HDF5DatasetWriterSegmentation

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
class HDF5PowerSegmentationAugmentor(IAugmentor):

    # All images must have same width and height
    def __init__(self,inputPath,parameters):
        IAugmentor.__init__(self)
        self.inputPath = inputPath
        self.imagesPath = inputPath + "images/"
        self.labelsPath = inputPath + "labels/"
        # output path represents the folder where the images will be stored
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
        if parameters["labelsExtension"]:
            self.labelsExtension = parameters["labelsExtension"]
        else:
            self.labelsExtension = ".tiff"
        self.aw = AspectAwarePreprocessor(self.width, self.height)


    def readImagesAndAnnotations(self):
        self.imagePaths = list(
            paths.list_files(self.imagesPath, validExts=(".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif")))
        self.labelPaths = list(
            paths.list_files(self.labelsPath, validExts=(".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif")))
        if (len(self.imagePaths) != len(self.labelPaths)):
            raise Exception("The number of files is different in the folder of images and in the folder of labels")

    def applyAugmentation(self):
        self.readImagesAndAnnotations()
        widgets = ["Processing images: ", progressbar.Percentage(), " ",
                   progressbar.Bar(), " ", progressbar.ETA()]

        pbar = progressbar.ProgressBar(maxval=len(self.imagePaths),
                                   widgets=widgets).start()
        writer = HDF5DatasetWriterSegmentation((len(self.imagePaths)*(2**(len(self.transformers)-1)),self.width,self.height,3),
                                   self.outputPath)

        for i_and_imagePath in enumerate(self.imagePaths):
            (i, imagePath) = i_and_imagePath
            image = cv2.imread(imagePath)
            image = self.aw.preprocess(image)
            name = imagePath.split(os.path.sep)[-1]
            labelPath = '/'.join(imagePath.split(os.path.sep)[:-2]) + "/labels/" + name[
                                                                                   0:name.rfind(".")] + self.labelsExtension
            label = cv2.imread(labelPath)
            label = self.aw.preprocess(label)
            images = [image]
            labels = [label]
            for (j, transformer) in enumerate(self.transformers):

                newimages = []
                newlabels = []
                for (k, (im,la)) in enumerate(zip(images,labels)):
                    (newimage,newlabel) = transformer.transform(im,la)
                    newimage = self.aw.preprocess(newimage)
                    newlabel = self.aw.preprocess(newlabel)
                    writer.add([newimage], [newlabel])
                    newimages.append(newimage)
                    newlabels.append(newlabel)
                images = newimages
                labels = newlabels

            pbar.update(i)
        writer.close()
        pbar.finish()


# Example
# augmentor = HDF5PowerSegmentationAugmentor(
#     "/home/joheras/pythonprojects/ssai-cnn/maps/mass_buildings/test/",
#     "/home/joheras/pythonprojects/ssai-cnn/maps/mass_buildings/maps.hdf5",
#     224,224,".tif"
# )
#
# from techniques.averageBlurringAugmentationTechnique import averageBlurringAugmentationTechnique
# from techniques.bilateralBlurringAugmentationTechnique import bilateralBlurringAugmentationTechnique
# from techniques.gaussianNoiseAugmentationTechnique import gaussianNoiseAugmentationTechnique
# from techniques.rotateAugmentationTechnique import rotateAugmentationTechnique
# from techniques.flipAugmentationTechnique import flipAugmentationTechnique
# from techniques.noneAugmentationTechnique import noneAugmentationTechnique
# from generator import Generator
# import time
# augmentor.addGenerator(Generator(noneAugmentationTechnique()))
# augmentor.addGenerator(Generator(averageBlurringAugmentationTechnique()))
# augmentor.addGenerator(Generator(bilateralBlurringAugmentationTechnique()))
# augmentor.addGenerator(Generator(gaussianNoiseAugmentationTechnique()))
# augmentor.addGenerator(Generator(rotateAugmentationTechnique()))
# augmentor.addGenerator(Generator(flipAugmentationTechnique()))
# start = time.time()
# augmentor.applyAugmentation()
# end = time.time()
# print(end - start)

