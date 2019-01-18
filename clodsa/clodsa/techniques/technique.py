from builtins import object
from abc import ABCMeta, abstractmethod
from future.utils import with_metaclass

class Technique(with_metaclass(ABCMeta, object)):
    def __init__(self, parameters = None):
        self.parameters = parameters

    @abstractmethod
    def apply(self, image):
        raise NotImplementedError




class PositionVariantTechnique(with_metaclass(ABCMeta, Technique)):
    def __init__(self, parameters=None):
        Technique.__init__(self, parameters)

    @abstractmethod
    def apply(self, image):
        raise NotImplementedError

class PositionInvariantTechnique(with_metaclass(ABCMeta, Technique)):
    def __init__(self, parameters=None):
        Technique.__init__(self, parameters)

    @abstractmethod
    def apply(self, image):
        raise NotImplementedError

