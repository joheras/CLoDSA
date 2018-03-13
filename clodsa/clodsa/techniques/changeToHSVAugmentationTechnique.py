from technique import NonAlteringTechnique
import cv2
import numpy as np

class changeToHSVAugmentationTechnique(NonAlteringTechnique):


    def __init__(self,parameters):
        NonAlteringTechnique.__init__(self, parameters)


    def apply(self, image):

        image1 = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        return image1