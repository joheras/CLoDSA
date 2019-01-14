from __future__ import absolute_import
from __future__ import division
from past.utils import old_div
from .technique import PositionVariantTechnique
import cv2


class resizeAugmentationTechnique(PositionVariantTechnique):

    methods = {'INTER_NEAREST': cv2.INTER_NEAREST,
               'INTER_LINEAR': cv2.INTER_LINEAR,
               'INTER_AREA': cv2.INTER_AREA,
               'INTER_CUBIC': cv2.INTER_CUBIC,
               'INTER_LANCZOS4': cv2.INTER_LANCZOS4}

    # valid methods for interpolation methods: INTER_AREA, INTER_CUBIC,
    # INTER_NEAREST, INTER_LINEAR, INTER_LANCZOS4
    def __init__(self, parameters):
        PositionVariantTechnique.__init__(self, parameters)
        if 'percentage' in list(parameters.keys()):
            self.percentage = float(parameters["percentage"])
        else:
            self.percentage = 1.5
        if 'method' in list(parameters.keys()):
            method = parameters["method"]
        else:
            method = 'INTER_AREA'

        if (not(method in self.methods)):
            raise NameError("Invalid value for method")
        self.method = self.methods[method]

    def __resize(self,image, width=None, height=None,inter=cv2.INTER_AREA):
        # initialize the dimensions of the image to be resized and
        # grab the image size
        dim = None
        (h, w) = image.shape[:2]

        # if both the width and height are None, then return the
        # original image
        if width is None and height is None:
            return image

        # check to see if the width is None
        if width is None:
            # calculate the ratio of the height and construct the
            # dimensions
            r = old_div(height, float(h))
            dim = (int(w * r), height)

        # otherwise, the height is None
        else:
            # calculate the ratio of the width and construct the
            # dimensions
            r = old_div(width, float(w))
            dim = (width, int(h * r))

        # resize the image
        resized = cv2.resize(image, dim, interpolation=inter)

        # return the resized image
        return resized

    def apply(self, image):
        resize = self.__resize(image,width=int(image.shape[1]*self.percentage),inter=self.method)
        return resize


# technique = resizeAugmentationTechnique()
# image = cv2.imread("LPR1.jpg")
# print int(image.shape[1]*1.5)
# cv2.imshow("resized",technique.applyForClassification(image))
# cv2.waitKey(0)