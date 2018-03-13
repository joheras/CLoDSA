from technique import NonAlteringTechnique
import cv2
import numpy as np

class invertAugmentationTechnique(NonAlteringTechnique):


    def __init__(self,parameters):
        NonAlteringTechnique.__init__(self, parameters)


    def apply(self, image):

        image1 = cv2.bitwise_not(image)
        return image1