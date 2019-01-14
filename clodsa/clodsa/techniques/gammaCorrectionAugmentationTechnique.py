from __future__ import absolute_import
from __future__ import division
from past.utils import old_div
from .technique import PositionInvariantTechnique
import cv2
import numpy as np

class gammaCorrectionAugmentationTechnique(PositionInvariantTechnique):

    # Valid values for gamma are in the range (0,2.5]
    def __init__(self,parameters):
        PositionInvariantTechnique.__init__(self, parameters)
        if 'gamma' in list(parameters.keys()):
            self.gamma = float(parameters["gamma"])
        else:
            self.gamma = 1.5

        if (self.gamma<=0 or self.gamma >2.5):
            raise NameError("Invalid value for gamma")

    def apply(self, image):
        invGamma = old_div(1.0, self.gamma)
        table = np.array([((old_div(i, 255.0)) ** invGamma) * 255
                          for i in np.arange(0, 256)]).astype("uint8")

        # apply gamma correction using the lookup table
        return cv2.LUT(image, table)