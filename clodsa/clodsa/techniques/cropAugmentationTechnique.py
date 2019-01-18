from __future__ import absolute_import
from __future__ import division
from past.utils import old_div
from .technique import PositionVariantTechnique
import cv2

class cropAugmentationTechnique(PositionVariantTechnique):

    # percentage is a value between 0 and 1
    # startFrom indicates the starting point of the cropping,
    # the possible values are TOPLEFT, TOPRIGHT, BOTTOMLEFT,
    # BOTTOMRIGHT, and CENTER
    def __init__(self,parameters):
        PositionVariantTechnique.__init__(self, parameters)
        if 'percentage' in list(parameters.keys()):
            self.percentage = float(parameters["percentage"])
        else:
            self.percentage = 0.9
        if 'startFrom' in list(parameters.keys()):
            self.startFrom = parameters["startFrom"]
        else:
            self.startFrom = 'TOPLEFT'

        if (self.percentage <0 or self.percentage >1):
            raise NameError("Invalid value for cropping")
        if self.startFrom not in ['TOPLEFT', 'TOPRIGHT', 'BOTTOMLEFT', 'BOTTOMRIGHT', 'CENTER']:
            raise NameError("Invalid value for cropping")


    def apply(self, image):
        (h,w) = image.shape[:2]
        newW = int(w*self.percentage)
        newH = int(h * self.percentage)
        if self.startFrom == 'TOPLEFT':
            crop = image[0:newH,0:newW]
        if self.startFrom == 'BOTTOMLEFT':
            crop = image[h-newH:h, 0:newW]
        if self.startFrom == 'TOPRIGHT':
            crop = image[0:newH,w-newW:w]
        if self.startFrom == 'BOTTOMRIGHT':
            crop = image[h-newH:h, w - newW:w]
        if self.startFrom == 'CENTER':
            crop = image[int(old_div(h,2) - old_div(newH,2)):int(old_div(h,2) + old_div(newH,2)),
                   int(old_div(w,2) - old_div(newW,2)):int(old_div(w,2) + old_div(newW,2))]
        return crop


# Example
# technique = cropAugmentationTechnique(0.5,'TOPRIGHT')
# image = cv2.imread("LPR1.jpg")
# cv2.imshow("original",image)
# cv2.imshow("new",technique.apply(image))
# cv2.waitKey(0)