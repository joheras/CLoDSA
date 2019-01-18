from __future__ import absolute_import
from .transformer import Transformer



class TransformerForImageClassification(Transformer):

    def __init__(self,technique,dictLabels=None):
        Transformer.__init__(self,technique,dictLabels)


    def transform(self, image,label):
        newImage = self.technique.apply(image)
        newLabel = self.transformLabel(label)
        return (newImage,newLabel)


