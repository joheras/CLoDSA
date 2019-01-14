from __future__ import absolute_import
from __future__ import division
from past.utils import old_div
from .technique import PositionVariantTechnique
import cv2
import numpy as np
import random

class rotateAugmentationTechnique(PositionVariantTechnique):

    # Valid angle is in the range [0,360), or it can also be a pair
    # indicating the range of angles
    def __init__(self,parameters):
        PositionVariantTechnique.__init__(self, parameters)
        if 'angle' in list(parameters.keys()):
            angle = int(parameters["angle"])
        else:
            angle = random.randint(0,360)

        if (isinstance(angle,list) and len(angle)==2):
            self.angle = random.randint(angle[0],angle[1])
        elif (isinstance(angle,int)):
            self.angle = angle
        else:
            raise ValueError("You must introduce either an integer or a pair")

    def __rotate_bound(self,image):
        # grab the dimensions of the image and then determine the
        # center
        (h, w) = image.shape[:2]
        (cX, cY) = (w // 2, h // 2)

        # grab the rotation matrix (applying the negative of the
        # angle to rotate clockwise), then grab the sine and cosine
        # (i.e., the rotation components of the matrix)
        M = cv2.getRotationMatrix2D((cX, cY), -self.angle, 1.0)
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])

        # compute the new bounding dimensions of the image
        nW = int((h * sin) + (w * cos))
        nH = int((h * cos) + (w * sin))

        # adjust the rotation matrix to take into account translation
        M[0, 2] += (old_div(nW, 2)) - cX
        M[1, 2] += (old_div(nH, 2)) - cY

        # perform the actual rotation and return the image
        return cv2.warpAffine(image, M, (nW, nH))

    def apply(self, image):
        rotated = self.__rotate_bound(image)
        return rotated


# Example
# technique = rotateAugmentationTechnique(25)
# image = cv2.imread("LPR1.jpg")
# # box = ('dog',(0,0,20,20))
# # imageC=technique.applyForClassification(image)
# # cv2.imshow("classification",technique.applyForClassification(image))
# # (imageL,(_,(x,y,w,h)))=technique.applyForLocalization(image,box)
# # cv2.rectangle(imageL,(x,y),(x+w,y+h),(255,255,255),1)
# cv2.imshow("rotation",technique.apply(image))
# cv2.waitKey(0)