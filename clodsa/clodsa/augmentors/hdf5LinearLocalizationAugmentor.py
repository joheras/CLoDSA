from __future__ import absolute_import
from builtins import object
from .iaugmentor import IAugmentor
from sklearn.preprocessing import LabelEncoder
from imutils import paths
import os
import cv2
from .utils.aspectawarepreprocessor import AspectAwarePreprocessor
from .utils.hdf5datasetwriter import HDF5DatasetWriterClassification
import xml.etree.ElementTree as ET
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
class HDF5LinearLocalizationAugmentor(IAugmentor):

    # All images must have same width and height
    def __init__(self,inputPath,parameters):
        IAugmentor.__init__(self)
        self.inputPath = inputPath
        # output path represents the h5py file where dataset will be stored
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
        writer = HDF5DatasetWriterClassification((len(self.imagePaths)*len(self.transformers),self.width,self.height,3),
                                   self.outputPath)
        # We need to define this function outside to work in parallel.
        writer.storeClassLabels(le.classes_)
        widgets = ["Processing images: ", progressbar.Percentage(), " ",
                   progressbar.Bar(), " ", progressbar.ETA()]

        pbar = progressbar.ProgressBar(maxval=len(self.imagePaths),
                                   widgets=widgets).start()
        for i_and_imagePath in enumerate(self.imagePaths):
            (i, imagePath) = i_and_imagePath
            image = cv2.imread(imagePath)
            name = imagePath.split(os.path.sep)[-1]
            labelPath = '/'.join(imagePath.split(os.path.sep)[:-1]) + "/" + name[0:name.rfind(".")] + ".xml"
            tree = ET.parse(labelPath)
            root = tree.getroot()
            objects = root.findall('object')
            if (len(objects) != 1):
                raise Exception("Since this is a localization problem, the xml should only contain one object")
            object = objects[0]
            category = object.find('name').text
            bndbox = object.find('bndbox')
            x = int(bndbox.find('xmin').text)
            y = int(bndbox.find('ymin').text)
            w = int(bndbox.find('ymax').text) - y
            h = int(bndbox.find('xmax').text) - x

            for (j, transformer) in enumerate(self.transformers):
                (newimage, box) = transformer.transform(image, (category, (x, y, w, h)))
                writer.add([newimage],[0,box[1][0],box[1][1],box[1][2],box[1][3]])
            pbar.update(i)
        pbar.finish()
        writer.close()

# # Example
# augmentor = HDF5LinearClassificationAugmentor(
#     "/home/joheras/datasets/cats_and_dogs_small/train/",
#     "/home/joheras/datasets/cats_and_dogs_small/database.hdf5"
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
