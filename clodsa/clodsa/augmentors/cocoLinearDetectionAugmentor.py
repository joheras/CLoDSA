from __future__ import absolute_import
from builtins import str
from builtins import object
import numpy as np

from .iaugmentor import IAugmentor
from .utils.readCOCOJSON import readCOCOJSONBoxes
from ..transformers.transformerFactory import transformerGenerator
from ..techniques.techniqueFactory import createTechnique
import json
import cv2
from joblib import Parallel, delayed
import imutils


def readAndGenerateInstanceSegmentation(outputPath, transformers, inputPath, imageInfo, boxes,ignoreClasses):
    name = imageInfo[0]
    imagePath = inputPath + "/" + name
    image = cv2.imread(imagePath)
    allNewImagesResult = []
    for (j, transformer) in enumerate(transformers):
        (newimage, newboxes) = transformer.transform(image, boxes,True)
        (hI,wI) =newimage.shape[:2]
        cv2.imwrite(outputPath + str(j) + "_" + name, newimage)
        newSegmentations = []
        for (label,box,_) in newboxes:
            newSegmentations.append((label, box, [], box[2]*box[3]))

        allNewImagesResult.append((str(j) + "_" + name, (wI, hI), newSegmentations))

    return allNewImagesResult


# This class serves to generate images for an instance segmentation
# problem where all the images are organized in a folder called
# images and there is a json file with the annotations of the images
# using the COCO format called annotation.json

class COCOLinearDetectionAugmentor(IAugmentor):

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
            = readCOCOJSONBoxes(self.annotationFile)

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

        with open(self.outputPath + "annotation.json", 'w') as outfile:
            json.dump(data, outfile)

