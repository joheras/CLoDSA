from itechnique import ITechnique
import cv2
import numpy as np

class invertAugmentationTechnique(ITechnique):


    def __init__(self,parameters):
        ITechnique.__init__(self,parameters,False)


    def apply(self, image):

        image1 = cv2.bitwise_not(image)
        return image1