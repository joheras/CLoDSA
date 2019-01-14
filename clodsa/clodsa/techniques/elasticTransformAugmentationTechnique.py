from __future__ import absolute_import
from .technique import PositionVariantTechnique
import cv2
import numpy as np
from scipy.ndimage.interpolation import map_coordinates
from scipy.ndimage.filters import gaussian_filter

class elasticTransformAugmentationTechnique(PositionVariantTechnique):

    def __init__(self,parameters):
        PositionVariantTechnique.__init__(self, parameters)
        if 'alpha' in list(parameters.keys()):
            self.alpha = float(parameters["alpha"])
        else:
            self.alpha = 5
        if 'sigma' in list(parameters.keys()):
            self.sigma = float(parameters["sigma"])
        else:
            self.sigma = 0.05

    def __elastic_transform(self,image):
        """Elastic deformation of images as described in [Simard2003]_.
        .. [Simard2003] Simard, Steinkraus and Platt, "Best Practices for
           Convolutional Neural Networks applied to Visual Document Analysis", in
           Proc. of the International Conference on Document Analysis and
           Recognition, 2003.
        """
        random_state = np.random.RandomState(None)
        if len(image.shape) == 3:
            (b,g,r) = cv2.split(image)

            shape = b.shape

            dx = gaussian_filter((random_state.rand(*shape) * 2 - 1), self.sigma, mode="constant", cval=0) * self.alpha
            dy = gaussian_filter((random_state.rand(*shape) * 2 - 1), self.sigma, mode="constant", cval=0) * self.alpha

            x, y = np.meshgrid(np.arange(shape[0]), np.arange(shape[1]), indexing='ij')
            indices = np.reshape(x + dx, (-1, 1)), np.reshape(y + dy, (-1, 1))

            return cv2.merge([map_coordinates(b, indices, order=1).reshape(shape),
                              map_coordinates(g, indices, order=1).reshape(shape),
                              map_coordinates(r, indices, order=1).reshape(shape)])
        else:
            shape = image.shape

            dx = gaussian_filter((random_state.rand(*shape) * 2 - 1), self.sigma, mode="constant", cval=0) * self.alpha
            dy = gaussian_filter((random_state.rand(*shape) * 2 - 1), self.sigma, mode="constant", cval=0) * self.alpha

            x, y = np.meshgrid(np.arange(shape[0]), np.arange(shape[1]), indexing='ij')
            indices = np.reshape(x + dx, (-1, 1)), np.reshape(y + dy, (-1, 1))

            return map_coordinates(image, indices, order=1).reshape(shape)

    def apply(self, image):
        translation = self.__elastic_transform(image)
        return translation

# technique = elasticTransformAugmentationTechnique(2,0.5)
# image = cv2.imread("LPR1.jpg")
# cv2.imshow("t",technique.applyForClassification(image))
# cv2.waitKey(0)
