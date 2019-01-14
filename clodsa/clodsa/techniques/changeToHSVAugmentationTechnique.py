from __future__ import absolute_import
from .technique import PositionInvariantTechnique
import cv2
import numpy as np

class changeToHSVAugmentationTechnique(PositionInvariantTechnique):


    def __init__(self,parameters):
        PositionInvariantTechnique.__init__(self, parameters)


    def apply(self, image):

        image1 = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        return image1