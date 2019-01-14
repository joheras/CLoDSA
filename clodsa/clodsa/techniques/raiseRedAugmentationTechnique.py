from __future__ import absolute_import
from __future__ import division
from past.utils import old_div
from .technique import PositionInvariantTechnique
import cv2
import numpy as np

class raiseRedAugmentationTechnique(PositionInvariantTechnique):

    # Valid values for pover are in the range (0.25,4]
    def __init__(self,parameters):
        PositionInvariantTechnique.__init__(self, parameters)
        if 'power' in list(parameters.keys()):
            self.power = float(parameters["power"])
        else:
            self.power = 0.9

        if (self.power<=0.25 or self.power >4):
            raise NameError("Invalid value for power")

    def apply(self, image):
        if(len(image.shape)!=3):
            raise NameError("Not applicable technique")
        identityB = np.arange(256, dtype=np.dtype('uint8'))
        identityR = np.array([((old_div(i, 255.0)) ** self.power) * 255
                              for i in np.arange(0, 256)]).astype("uint8")
        identityG = np.arange(256, dtype=np.dtype('uint8'))
        lut = np.dstack((identityB, identityG, identityR))

        # apply gamma correction using the lookup table
        image = cv2.LUT(image, lut)
        return image