from technique import NonAlteringTechnique
import cv2
import numpy as np
from keras.preprocessing.image import *

class shiftChannelAugmentationTechnique(NonAlteringTechnique):

    # Valid values for shift are positive values
    def __init__(self,parameters):
        NonAlteringTechnique.__init__(self, parameters)
        if 'shift' in parameters.keys():
            self.shift = float(parameters["shift"])
        else:
            self.shift = 0.2


    def apply(self, image):
        if(len(image.shape)!=3):
            raise NameError("Not applicable technique")

        image1 = random_channel_shift(image, self.shift, 2)
        return image1