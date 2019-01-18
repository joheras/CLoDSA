from builtins import object
from abc import ABCMeta,abstractmethod
from future.utils import with_metaclass

class IAugmentor(with_metaclass(ABCMeta, object)):
    def __init__(self):
        self.transformers = []

    def addTransformer(self, transformer):
        self.transformers.append(transformer)

    @abstractmethod
    def readImagesAndAnnotations(self):
        raise NotImplementedError

    @abstractmethod
    def applyAugmentation(self):
        raise NotImplementedError
