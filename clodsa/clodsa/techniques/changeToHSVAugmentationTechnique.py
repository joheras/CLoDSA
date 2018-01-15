from itechnique import ITechnique
import cv2
import numpy as np

class changeToHSVAugmentationTechnique(ITechnique):


    def __init__(self,parameters):
        ITechnique.__init__(self,parameters,False)


    def apply(self, image):

        image1 = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        return image1