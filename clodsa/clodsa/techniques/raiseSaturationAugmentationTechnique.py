from technique import NonAlteringTechnique
import cv2
import numpy as np

class raiseSaturationAugmentationTechnique(NonAlteringTechnique):

    # Valid values for pover are in the range (0.25,4]
    def __init__(self,parameters):
        NonAlteringTechnique.__init__(self, parameters)
        if 'power' in parameters.keys():
            self.power = float(parameters["power"])
        else:
            self.power = 1.5

        if (self.power<=0.25 or self.power >4):
            raise NameError("Invalid value for power")

    def apply(self, image):
        if(len(image.shape)!=3):
            raise NameError("Not applicable technique")
        imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        identityH = np.arange(256, dtype=np.dtype('uint8'))
        identityS = np.array([((i / 255.0) ** self.power) * 255
                              for i in np.arange(0, 256)]).astype("uint8")
        identityV = np.arange(256, dtype=np.dtype('uint8'))
        lut = np.dstack((identityH, identityS, identityV))

        # apply gamma correction using the lookup table
        imageHSV=cv2.LUT(imageHSV, lut)
        imageRGB = cv2.cvtColor(imageHSV, cv2.COLOR_HSV2BGR)
        return imageRGB