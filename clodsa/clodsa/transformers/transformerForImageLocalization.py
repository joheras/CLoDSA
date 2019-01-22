from __future__ import absolute_import
from .transformer import Transformer
from .detection import detectBox
from ..techniques.technique import PositionVariantTechnique



class TransformerForImageLocalization(Transformer):

    def __init__(self,technique,dictLabels=None):
        Transformer.__init__(self,technique,dictLabels)


    def transform(self, image,box):
        newImage = self.technique.apply(image)
        if (isinstance(self.technique, PositionVariantTechnique)):
            newBox = detectBox(image.shape[:2], box, self.technique)
            newBox = (self.transformLabel(newBox[0]), newBox[1])
        else:
            newBox = (self.transformLabel(box[0]), box[1])

        return [newImage,newBox]


