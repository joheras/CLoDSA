from __future__ import absolute_import
from .technique import PositionVariantTechnique
import cv2

class flipAugmentationTechnique(PositionVariantTechnique):

    # Valid values for flip are -1,0,1
    def __init__(self,parameters):
        PositionVariantTechnique.__init__(self, parameters)
        if 'flip' in list(parameters.keys()):
            self.flip = int(parameters["flip"])
        else:
            self.flip = 1
        if (not(self.flip in [-1,1,0])):
            raise NameError("Invalid value for flip")

    def apply(self, image):
        flipped = cv2.flip(image, self.flip)
        return flipped


# Example
# technique = flipAugmentationTechnique(1)
# image = cv2.imread("LPR1.jpg")
# box = ('dog',(0,0,20,20))
# imageC=technique.applyForClassification(image)
# cv2.imshow("classification",technique.applyForClassification(image))
# (imageL,(_,(x,y,w,h)))=technique.applyForLocalization(image,box)
# cv2.rectangle(imageL,(x,y),(x+w,y+h),(255,255,255),1)
# cv2.imshow("localization",imageL)
# cv2.waitKey(0)