from __future__ import absolute_import
from builtins import str
from builtins import object
import numpy as np

from .iaugmentor import IAugmentor
from .utils.readCOCOJSON import readCOCOJSON
import json
import cv2
from joblib import Parallel, delayed
import imutils
from imutils import paths
import os


def readAndGenerateInstanceSegmentation(outputPath, transformers, imagePath):
    image = cv2.imread(imagePath)
    name = imagePath.split(os.path.sep)[-1]
    labelPath = '/'.join(imagePath.split(os.path.sep)[:-1]) + "/" + name[0:name.rfind(".")] + ".txt"
    maskLabels = []
    (h,w)=image.shape[:2]
    with open(labelPath) as f:
        data = json.load(f)

    annotations = data['annotations']


    for annotation in annotations:
        mask = np.zeros((w, h), dtype="uint8")
        key = list(annotation)[0]

        if key == 'rectangle':
            x = annotation['rectangle']['x']
            y = annotation['rectangle']['y']
            width = annotation['rectangle']['width']
            height = annotation['rectangle']['height']
            label = annotation['rectangle']['label']
            cv2.rectangle(mask,(x,y),(x+width,y+height),255,-1)
            maskLabels.append((mask, label))

        if key == 'circle':
            x = annotation['circle']['x']
            y = annotation['circle']['y']
            diameter = annotation['circle']['radius']
            label = annotation['circle']['label']
            cv2.circle(mask,(int(x+diameter/2),int(y+diameter/2)),int(diameter/2),255,-1)
            maskLabels.append((mask, label))

        if key == 'polygon':
            xpoints = annotation['polygon']['xpoints']
            ypoints = annotation['polygon']['ypoints']
            label = annotation['polygon']['label']
            pts = np.array([[x,y] for x,y in zip(xpoints,ypoints)], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.fillPoly(mask, [pts], True, 255)

            maskLabels.append((mask, label))

    for (j, transformer) in enumerate(transformers):
        (newimage, newmasklabels) = transformer.transform(image, maskLabels)

        cv2.imwrite(outputPath + str(j) + "_" + name, newimage)
        newSegmentations = []
        for (mask, label) in newmasklabels:
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if imutils.is_cv2() else cnts[1]
            segmentation = [[x[0][0], x[0][1]] for x in cnts[0]]
            # Closing the polygon
            segmentation.append(segmentation[0])

            newSegmentations.append((label,  segmentation))
        data = {}
        data['name'] = name
        data['width'] = w
        data['height'] = h
        data['annotations'] = []
        for (l,segmentation) in newSegmentations:
            xpoints = [int(x[0]) for x in segmentation]
            ypoints = [int(x[1]) for x in segmentation]
            data['annotations'].append({'polygon':{'ypoints':ypoints,
                                                   'xpoints':xpoints,
                                                   'label':label}})


        with open(outputPath + str(j) + "_" + name[0:name.rfind(".")]+ ".txt", 'w') as outfile:
            json.dump(data, outfile)


# This class serves to generate images for an instance segmentation
# problem where all the images are organized in a folder together with
# a special purpose json (a json file for each image).

class JSONLinearInstanceSegmentationAugmentor(IAugmentor):

    def __init__(self, inputPath, parameters):
        IAugmentor.__init__(self)
        self.inputPath = inputPath
        # output path represents the folder where the images will be stored
        if parameters["outputPath"]:
            self.outputPath = parameters["outputPath"]
        else:
            raise ValueError("You should provide an output path in the parameters")


    def readImagesAndAnnotations(self):
        self.imagePaths = list(
            paths.list_files(self.inputPath, validExts=(".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif")))
        self.labelPaths = list(paths.list_files(self.inputPath, validExts=(".txt")))
        if (len(self.imagePaths) != len(self.labelPaths)):
            raise Exception("The number of images is different to the number of annotations")

    def applyAugmentation(self):
        self.readImagesAndAnnotations()

        Parallel(n_jobs=-1)(delayed(readAndGenerateInstanceSegmentation)
                                             (self.outputPath, self.transformers, imagePath)
                                             for imagePath in self.imagePaths)


