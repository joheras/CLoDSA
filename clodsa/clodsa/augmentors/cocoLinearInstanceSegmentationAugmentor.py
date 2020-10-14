from __future__ import absolute_import
from builtins import str
from builtins import object
import numpy as np
import os

from .iaugmentor import IAugmentor
from .utils.readCOCOJSON import readCOCOJSON
from ..transformers.transformerFactory import transformerGenerator
from ..techniques.techniqueFactory import createTechnique
import json
import cv2
from joblib import Parallel, delayed
import imutils


def readAndGenerateInstanceSegmentation(outputPath, transformers, inputPath, imageInfo, annotationsInfo,ignoreClasses):
    name = imageInfo[0]
    imagePath = inputPath + "/" + name
    (w, h) = imageInfo[1]
    image = cv2.imread(imagePath)
    maskLabels = []
    labels = set()
    for (c, annotation) in annotationsInfo:
        mask = np.zeros((h, w), dtype="uint8")
        annotation = [[annotation[2 * i], annotation[2 * i + 1]] for i in range(0, int(len(annotation) / 2))]
        pts = np.array([[int(x[0]), int(x[1])] for x in annotation], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.fillPoly(mask, [pts], True, 255)
        maskLabels.append((mask, c))
        labels.add(c)

    if not(labels.isdisjoint(ignoreClasses)):
        newtransformer = transformerGenerator("instance_segmentation")
        none = createTechnique("none",{})
        transformers = [newtransformer(none)]

    allNewImagesResult = []
    for (j, transformer) in enumerate(transformers):
        try:
            (newimage, newmasklabels) = transformer.transform(image, maskLabels)
        except:
            print("Error in image: " + imagePath)
        (hI,wI) =newimage.shape[:2]
        cv2.imwrite(outputPath + str(j) + "_" + name, newimage)
        newSegmentations = []
        for (mask, label) in newmasklabels:
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            cnts = cnts[0] if imutils.is_cv2() or imutils.is_cv4() else cnts[1]
            if len(cnts)>0:
                segmentation = [[x[0][0], x[0][1]] for x in cnts[0]]
                # Closing the polygon
                segmentation.append(segmentation[0])

                newSegmentations.append((label, cv2.boundingRect(cnts[0]), segmentation, cv2.contourArea(cnts[0])))

        allNewImagesResult.append((str(j) + "_" + name, (wI, hI), newSegmentations))

    return allNewImagesResult


# This class serves to generate images for an instance segmentation
# problem where all the images are organized in a folder called
# images and there is a json file with the annotations of the images
# using the COCO format called annotation.json

class COCOLinearInstanceSegmentationAugmentor(IAugmentor):

    def __init__(self, inputPath, parameters):
        IAugmentor.__init__(self)
        self.imagesPath = inputPath
        self.annotationFile = inputPath + "/annotations.json"
        # output path represents the folder where the images will be stored
        if parameters["outputPath"]:
            self.outputPath = parameters["outputPath"]
        else:
            raise ValueError("You should provide an output path in the parameters")
        
        self.ignoreClasses = parameters.get("ignoreClasses",set())



    def readImagesAndAnnotations(self):
        (self.info, self.licenses, self.categories, self.dictImages, self.dictAnnotations) \
            = readCOCOJSON(self.annotationFile)

    def applyAugmentation(self):
        self.readImagesAndAnnotations()

        newannotations = Parallel(n_jobs=-1)(delayed(readAndGenerateInstanceSegmentation)
                                             (self.outputPath, self.transformers, self.imagesPath, self.dictImages[x],
                                              self.dictAnnotations[x],self.ignoreClasses)
                                             for x in self.dictImages.keys())

        data = {}
        data['info'] = self.info
        data['licenses'] = self.licenses
        data['categories'] = self.categories
        data['images'] = []
        data['annotations'] = []
        imageId = 1
        annotationId = 1
        newannotations = [item for sublist in newannotations for item in sublist]
        for (fil, (w, h), annotations) in newannotations:
            data['images'].append({'id': imageId,
                                   'file_name': fil,
                                   'width': w,
                                   'height': h,
                                   'date_captured': '',
                                   'license': 1,
                                   'coco_url': '',
                                   'flickr_url': ''})

            for annotation in annotations:

                label = annotation[0]
                rect = annotation[1]
                segmentation = annotation[2]
                area = annotation[3]
                segmentationCOCO = []
                for x in segmentation:
                    segmentationCOCO.append(int(x[0]))
                    segmentationCOCO.append(int(x[1]))
                data['annotations'].append({'id': annotationId,
                                            'image_id': imageId,
                                            'category_id': label,
                                            'iscrowd': 0,
                                            'area': area,
                                            'bbox': [rect[0], rect[1], rect[2], rect[3]],
                                            'segmentation': [segmentationCOCO],
                                            'width': w,
                                            'height': h})
                annotationId += 1
            imageId += 1

        os.makedirs(self.outputPath,exist_ok=True)
        with open(self.outputPath + "annotation.json", 'w') as outfile:
            json.dump(data, outfile)

