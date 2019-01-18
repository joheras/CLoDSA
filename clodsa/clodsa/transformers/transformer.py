from abc import ABCMeta, abstractmethod
from future.utils import with_metaclass


class Transformer(with_metaclass(ABCMeta, object)):
    def __init__(self, technique,dictLabels=None):
        self.technique = technique
        self.dictLabels=dictLabels

    @abstractmethod
    def transform(self, T1,T2):
        raise NotImplementedError

    def transformLabel(self,label):
        if (self.dictLabels is not None) and (label in self.dictLabels.keys()):
            return self.dictLabels[label]
        else:
            return label

