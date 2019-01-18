from __future__ import absolute_import
from .transformer import Transformer
from ..techniques.technique import PositionVariantTechnique



class TransformerForImageSegmentation(Transformer):

    def __init__(self,technique,dictLabels=None):
        Transformer.__init__(self,technique,dictLabels)

    def transform(self, image, imageLabel):
        if (isinstance(self.technique, PositionVariantTechnique)):
            return [self.technique.apply(image),
                    self.technique.apply(imageLabel)]
        else:
            return [self.technique.apply(image), imageLabel]