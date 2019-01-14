from __future__ import absolute_import
from .technique import PositionInvariantTechnique
import cv2
import numpy as np

class gaussianNoiseAugmentationTechnique(PositionInvariantTechnique):


    def __init__(self,parameters):
        PositionInvariantTechnique.__init__(self, parameters)
        if 'mean' in list(parameters.keys()):
            self.mean = float(parameters["mean"])
        else:
            self.mean = 0
        if 'sigma' in list(parameters.keys()):
            self.sigma = float(parameters["sigma"])
        else:
            self.sigma = 10

    def apply(self, image):
        im = np.zeros(image.shape, np.uint8)
        if(len(image.shape)==2):
            m = self.mean
            s = self.sigma
        else:
            m = (self.mean,self.mean,self.mean)
            s = (self.sigma,self.sigma,self.sigma)
        cv2.randn(im, m, s)
        image_noise = cv2.add(image, im)
        return image_noise



