from __future__ import absolute_import
from builtins import str
from builtins import object
from .iaugmentor import IAugmentor
from imutils import paths
import os
import cv2
from joblib import Parallel, delayed

# We need to define this function outside to work in parallel.
def readAndGenerateVideo(outputPath, transformers, i_and_videoPath):
    (i, videoPath) = i_and_videoPath

    vidcap = cv2.VideoCapture(videoPath)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    listImages = []
    success, image = vidcap.read()
    (h,w) = image.shape[:2]
    listImages.append(image)
    while success:
        success, image = vidcap.read()
        listImages.append(image)
    vidcap.release()

    label = videoPath.split(os.path.sep)[-2]
    name = videoPath.split(os.path.sep)[-1]
    for (j, transformer) in enumerate(transformers):
        newListImages,newlabel = transformer.transform(listImages,label)

        out = cv2.VideoWriter(outputPath + newlabel + "/" + str(i) + "_" + str(j) + "_" + name,
                          cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, (w, h))

        for image in newListImages:
            out.write(image)

        out.release()

# This class serves to generate videos for a classification
# problem where all the videos are organized by folders
# distributed by labels. Example:
# - Folder
# |- cats
#    |- video1.mp4
#    |- video2.mp4
#    |- ...
# |- dogs
#    |- video1.mp4
#    |- video2.mp4
#    |- ...
class FolderVideoLinearClassificationAugmentor(IAugmentor):

    def __init__(self,inputPath,parameters):
        IAugmentor.__init__(self)
        self.inputPath = inputPath
        # output path represents the folder where the images will be stored
        if parameters["outputPath"]:
            self.outputPath = parameters["outputPath"]
        else:
            raise ValueError("You should provide an output path in the parameters")




    def readImagesAndAnnotations(self):
        self.imagePaths = list(paths.list_files(self.inputPath,validExts=(".avi", ".mp4")))

    def createOutputDirs(self):
        dirs = [d for d in os.listdir(self.inputPath) if os.path.isdir(os.path.join(self.inputPath, d))]
        for dir in dirs:
            os.makedirs(self.outputPath + dir + "/")

    def applyAugmentation(self):
        self.readImagesAndAnnotations()
        self.createOutputDirs()

        #[readAndGenerateVideo(self.outputPath,self.generators,x) for x in enumerate(self.imagePaths)]
        Parallel(n_jobs=-1)(delayed(readAndGenerateVideo)(self.outputPath,self.transformers,x) for x in enumerate(self.imagePaths))

