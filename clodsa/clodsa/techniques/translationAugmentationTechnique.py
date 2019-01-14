from __future__ import absolute_import
from .technique import PositionVariantTechnique
import cv2
import numpy as np

class translationAugmentationTechnique(PositionVariantTechnique):

    def __init__(self,parameters):
        PositionVariantTechnique.__init__(self, parameters)
        if 'x' in list(parameters.keys()):
            self.x = int(parameters["x"])
        else:
            self.x = 10
        if 'y' in list(parameters.keys()):
            self.y = int(parameters["y"])
        else:
            self.y = 10

    def __translate(self,image, x, y):
        # define the translation matrix and perform the translation
        M = np.float32([[1, 0, x], [0, 1, y]])
        shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

        # return the translated image
        return shifted

    def apply(self, image):
        translation = self.__translate(image, self.x,self.y)
        return translation

# technique = translationAugmentationTechnique(5,5)
# image = cv2.imread("LPR1.jpg")
# cv2.imshow("t",technique.applyForClassification(image))
# cv2.waitKey(0)
