from __future__ import absolute_import
from .transformer import Transformer
from joblib import Parallel, delayed


class TransformerForImageStackClassification(Transformer):

    def __init__(self,technique,dictLabels=None):
        Transformer.__init__(self,technique,dictLabels)


    def transform(self, listImages,label):
        newlistImages = Parallel(n_jobs=-1)(
            delayed(self.technique.apply)(image) for image in listImages if image is not None)
        return [newlistImages,self.transformLabel(label)]


