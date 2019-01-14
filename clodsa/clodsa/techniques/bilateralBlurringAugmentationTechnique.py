from __future__ import absolute_import
from .technique import PositionInvariantTechnique
import cv2
import numpy as np

class bilateralBlurringAugmentationTechnique(PositionInvariantTechnique):

    # Examples for values of diameter, sigmaColor, and sigmaSpace are
    # (11,21,7), (11,41,21), (11,61,39).
    def __init__(self,parameters):
        PositionInvariantTechnique.__init__(self, parameters)
        if 'diameter' in list(parameters.keys()):
            self.diameter = int(parameters["diameter"])
        else:
            self.diameter = 11
        if 'sigmaColor' in list(parameters.keys()):
            self.sigmaColor = int(parameters["sigmaColor"])
        else:
            self.sigmaColor = 21
        if 'sigmaSpace' in list(parameters.keys()):
            self.sigmaSpace = int(parameters["sigmaSpace"])
        else:
            self.sigmaSpace = 7



    def apply(self, image):
        blurred = cv2.bilateralFilter(image, self.diameter, self.sigmaColor, self.sigmaSpace)
        return blurred