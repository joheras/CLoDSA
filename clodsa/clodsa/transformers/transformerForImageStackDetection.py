from __future__ import absolute_import
from .transformer import Transformer
from joblib import Parallel, delayed
from ..techniques.technique import PositionVariantTechnique
from .detection import detectBoxes



class TransformerForImageStackDetection(Transformer):

    def __init__(self,technique,dictLabels=None):
        Transformer.__init__(self,technique,dictLabels)


    def transform(self, listImages, boxes):
        imageShape = listImages[0].shape[:2]

        if (isinstance(self.technique, PositionVariantTechnique)):
            newBoxes = detectBoxes(imageShape, boxes, self.technique)
            newBoxes = [(self.transformLabel(box[0]),box[1]) for box in newBoxes]
        else:
            newBoxes= [(self.transformLabel(box[0]),box[1]) for box in boxes]

        newlistImages = Parallel(n_jobs=-1)(
            delayed(self.technique.apply)(image) for image in listImages if image is not None)
        return [newlistImages,newBoxes]
