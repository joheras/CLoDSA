from __future__ import absolute_import
from .technique import PositionInvariantTechnique
import cv2

class noneAugmentationTechnique(PositionInvariantTechnique):

    # Valid values for kernel are 3,5,7,9, and 11
    def __init__(self,parameters=None):
        PositionInvariantTechnique.__init__(self, parameters)


    def apply(self, image):
        if image is not None:
            return image.copy()
        return None