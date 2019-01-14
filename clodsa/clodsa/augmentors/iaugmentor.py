from builtins import object
from abc import ABCMeta,abstractmethod
from future.utils import with_metaclass

class IAugmentor(with_metaclass(ABCMeta, object)):
    def addGenerator(self, generator):
        self.generators.append(generator)

    @abstractmethod
    def readImagesAndAnnotations(self):
        raise NotImplementedError

    @abstractmethod
    def applyAugmentation(self):
        raise NotImplementedError
