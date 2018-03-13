from technique import NonAlteringTechnique
import cv2

class noneAugmentationTechnique(NonAlteringTechnique):

    # Valid values for kernel are 3,5,7,9, and 11
    def __init__(self,parameters=None):
        NonAlteringTechnique.__init__(self, parameters)


    def apply(self, image):
        return image.copy()