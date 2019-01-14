from __future__ import absolute_import
from .technique import PositionInvariantTechnique
import cv2

class averageBlurringAugmentationTechnique(PositionInvariantTechnique):

    # Valid values for kernel are 3,5,7,9, and 11
    def __init__(self,parameters):
        PositionInvariantTechnique.__init__(self, parameters)
        if 'kernel' in list(parameters.keys()):
            self.kernel = int(parameters["kernel"])
        else:
            self.kernel = 3
        if (not (self.kernel in [3,5,7,9,11])):
            raise NameError("Invalid value for kernel")

    def apply(self, image):
        blurred = cv2.blur(image, (self.kernel, self.kernel))
        return blurred