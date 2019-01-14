from __future__ import absolute_import
from .technique import PositionInvariantTechnique
import cv2
import numpy as np
from keras.preprocessing.image import *

class shiftChannelAugmentationTechnique(PositionInvariantTechnique):

    # Valid values for shift are positive values
    def __init__(self,parameters):
        PositionInvariantTechnique.__init__(self, parameters)
        if 'shift' in list(parameters.keys()):
            self.shift = float(parameters["shift"])
        else:
            self.shift = 0.2


    def apply(self, image):
        if(len(image.shape)!=3):
            raise NameError("Not applicable technique")

        image1 = random_channel_shift(image, self.shift, 2)
        return image1