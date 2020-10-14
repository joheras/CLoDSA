from __future__ import absolute_import
from builtins import str
from builtins import object
from .iaugmentor import IAugmentor
from imutils import paths
import os
import cv2
from joblib import Parallel, delayed

# We need to define this function outside to work in parallel.
def readAndGenerateImage(outputPath, transformers, i_and_imagePath):
    (i, imagePath) = i_and_imagePath
    image = cv2.imread(imagePath)
    label = imagePath.split(os.path.sep)[-2]
    name = imagePath.split(os.path.sep)[-1]
    for (j, transformer) in enumerate(transformers):
        newimage,newlabel = transformer.transform(image,label)
        cv2.imwrite(outputPath + newlabel + "/" + str(i) + "_" + str(j) + "_" + name,
                    newimage)

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
class FolderLinearClassificationAugmentor(IAugmentor):

    def __init__(self,inputPath,parameters):
        IAugmentor.__init__(self)
        self.inputPath = inputPath
        # output path represents the folder where the images will be stored
        if parameters["outputPath"]:
            self.outputPath = parameters["outputPath"]
        else:
            raise ValueError("You should provide an output path in the parameters")

    def readImagesAndAnnotations(self):
        self.imagePaths = list(paths.list_files(self.inputPath,validExts=(".jpg", ".jpeg", ".png", ".bmp",".tiff",".tif")))

    def createOutputDirs(self):
        dirs = [d for d in os.listdir(self.inputPath) if os.path.isdir(os.path.join(self.inputPath, d))]
        for dir in dirs:
            os.makedirs(self.outputPath + dir + "/")

    def applyAugmentation(self):
        self.readImagesAndAnnotations()
        self.createOutputDirs()
        len1 = len(self.imagePaths)
        Parallel(n_jobs=-1)(delayed(readAndGenerateImage)(self.outputPath,self.transformers,x) for x in enumerate(self.imagePaths))

