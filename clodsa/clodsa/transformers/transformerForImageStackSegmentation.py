from __future__ import absolute_import
from .transformer import Transformer
from joblib import Parallel, delayed
from ..techniques.technique import PositionVariantTechnique



class TransformerForImageStackSegmentation(Transformer):

    def __init__(self,technique,dictLabels=None):
        Transformer.__init__(self,technique,dictLabels)


    def transform(self, listImages, listMasks):


        newlistImages = Parallel(n_jobs=-1)(
            delayed(self.technique.apply)(image) for image in listImages if image is not None)
        if (isinstance(self.technique, PositionVariantTechnique)):
            newListMasks = Parallel(n_jobs=-1)(
            delayed(self.technique.apply)(image) for image in listMasks if image is not None)
            return [newlistImages,newListMasks]
        else:
            return [newlistImages, listMasks]
