from __future__ import absolute_import
from .technique import PositionInvariantTechnique
import cv2
import numpy as np

class sharpenAugmentationTechnique(PositionInvariantTechnique):

    # Valid values for kernel are 3,5,7,9, and 11
    def __init__(self,parameters):
        PositionInvariantTechnique.__init__(self, parameters)

    def apply(self, image):
        kernel = np.array([[0,-1,0],
                           [-1, 5, -1],
                           [0, -1, 0]])

        sharpen = cv2.filter2D(image, -1, kernel)
        return sharpen


# technique = sharpenAugmentationTechnique()
# image = cv2.imread("LPR1.jpg")
# cv2.imshow("resized",technique.apply(image))
# cv2.waitKey(0)