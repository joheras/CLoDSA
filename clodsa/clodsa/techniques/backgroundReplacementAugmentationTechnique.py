from __future__ import absolute_import
from .technique import BackgroundReplaceTechnique
import cv2
import numpy as np
import os
import random

class backgroundReplacementAugmentationTechnique(BackgroundReplaceTechnique):

    # Valid values for kernel are 3,5,7,9, and 11
    def __init__(self,parameters):
        BackgroundReplaceTechnique.__init__(self, parameters)
        self.parameters = parameters

    def apply(self, image):
        #blurred = cv2.blur(image, (self.kernel, self.kernel))
        return image

    def apply2(self, image, maskLabels):
        
        # list all files and get only images
        bkg_img_files = os.listdir(self.parameters["background_images_dir"])
        bkg_img_files = [f for f in bkg_img_files if ((".jpg" in f) or (".png" in f))]
        # load and resize one random background image
        bkg_img = cv2.imread(os.path.join(self.parameters["background_images_dir"], random.sample(bkg_img_files,1)[0]))
        bkg_img = cv2.resize(bkg_img, (image.shape[1],image.shape[0]), interpolation = cv2.INTER_AREA)

        instance_mask = np.ones(maskLabels[0][0].shape)
        instance_mask = (instance_mask == 0)
        instance_mask = np.dstack((instance_mask,instance_mask,instance_mask))
        #background = np.full(image.shape,np.array([0,255,0]))
        for mask, label in maskLabels:
            bool_mask = mask > 0
            bool_mask = np.dstack((bool_mask,bool_mask,bool_mask))
            np.logical_or(instance_mask, bool_mask, instance_mask)
        image = np.where(instance_mask, image, bkg_img)
        return image