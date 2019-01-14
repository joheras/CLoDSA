from abc import ABCMeta,abstractmethod

class IAugmentor:
    __metaclass__ = ABCMeta

    def addGenerator(self, generator):
        self.generators.append(generator)

    @abstractmethod
    def readImagesAndAnnotations(self):
        raise NotImplementedError

    @abstractmethod
    def applyAugmentation(self):
        raise NotImplementedError
