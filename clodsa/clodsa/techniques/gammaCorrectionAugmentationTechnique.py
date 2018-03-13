from technique import NonAlteringTechnique
import cv2
import numpy as np

class gammaCorrectionAugmentationTechnique(NonAlteringTechnique):

    # Valid values for gamma are in the range (0,2.5]
    def __init__(self,parameters):
        NonAlteringTechnique.__init__(self, parameters)
        if 'gamma' in parameters.keys():
            self.gamma = float(parameters["gamma"])
        else:
            self.gamma = 1.5

        if (self.gamma<=0 or self.gamma >2.5):
            raise NameError("Invalid value for gamma")

    def apply(self, image):
        invGamma = 1.0 / self.gamma
        table = np.array([((i / 255.0) ** invGamma) * 255
                          for i in np.arange(0, 256)]).astype("uint8")

        # apply gamma correction using the lookup table
        return cv2.LUT(image, table)