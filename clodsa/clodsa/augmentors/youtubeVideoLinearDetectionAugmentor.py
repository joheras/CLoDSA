from __future__ import absolute_import
from builtins import str
from builtins import object
from .iaugmentor import IAugmentor
from imutils import paths
import os
import cv2
from joblib import Parallel, delayed
import pandas as pd
import numpy as np


# We need to define this function outside to work in parallel.
def readAndGenerateVideo(outputPath, transformers, i_and_videoPath, df):
    (i, videoPath) = i_and_videoPath
    name = videoPath.split(os.path.sep)[-1]
    ext = name[name.rfind("."):]
    name = name[0:name.rfind(".")]

    boxes = np.array(df[df[0] == name].iloc[:, 1:])
    boxesConverted = []

    vidcap = cv2.VideoCapture(videoPath)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    listImages = []
    success, image = vidcap.read()
    (hI, wI) = image.shape[:2]
    for box in boxes:
        if box[1] != -1.00:
            category = box[1]
            x = int(box[5] * wI)
            y = int(box[7] * hI)
            h = int((box[8] - y) * hI)
            w = int((box[6] - x) * wI)
            boxesConverted.append((category, (x, y, w, h)))
    listImages.append(image)
    while success:
        success, image = vidcap.read()
        listImages.append(image)
    vidcap.release()
    boxesOutput = []

    for (j, transformer) in enumerate(transformers):
        newListImages, newboxes = transformer.transform(listImages, boxesConverted)

        out = cv2.VideoWriter(outputPath + str(i) + "_" + str(j) + "_" + name + ext,
                              cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, (wI, hI))

        for image in newListImages:
            out.write(image)

        out.release()
        for box0, box1 in zip(boxes, newboxes):
            (c, (x, y, wb, hb)) = box1
            boxesOutput.append([str(i) + "_" + str(j) + "_" + name, box0[0], c,
                                box0[2], box0[3], box0[4], x / wI, (x + wb) / wI, y / hI, (y + hb) / hI])

    return boxesOutput


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
class YoutubeVideoLinearDetectionAugmentor(IAugmentor):

    def __init__(self, inputPath, parameters):
        IAugmentor.__init__(self)
        self.inputPath = inputPath
        # output path represents the folder where the images will be stored
        if parameters["outputPath"]:
            self.outputPath = parameters["outputPath"]
        else:
            raise ValueError("You should provide an output path in the parameters")
        if parameters["csv"]:
            self.csv = parameters["csv"]
        else:
            raise ValueError("You should provide a csv name containing the annotations")

    def readImagesAndAnnotations(self):
        self.imagePaths = list(paths.list_files(self.inputPath, validExts=(".avi", ".mp4")))

    def createOutputDirs(self):
        if not (os._exists(self.outputPath)):
            os.makedirs(self.outputPath)

    def applyAugmentation(self):
        self.readImagesAndAnnotations()
        self.createOutputDirs()
        df = pd.read_csv(self.inputPath + self.csv, header=None)

        # [readAndGenerateVideo(self.outputPath,self.generators,x) for x in enumerate(self.imagePaths)]
        boxesOutput = Parallel(n_jobs=-1)(
            delayed(readAndGenerateVideo)(self.outputPath, self.transformers, x, df) for x in
            enumerate(self.imagePaths))
        boxesOutput = [item for sublist in boxesOutput for item in sublist]

        df = pd.DataFrame(boxesOutput)
        df.to_csv(self.outputPath + self.csv, header=False, index=False)
