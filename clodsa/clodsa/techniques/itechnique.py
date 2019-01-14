from builtins import object
from abc import ABCMeta, abstractmethod
from future.utils import with_metaclass

class ITechnique(with_metaclass(ABCMeta, object)):
    def __init__(self, parameters = None,changeLabel=False):
        self.changeLabel = changeLabel
        self.parameters = parameters

    @abstractmethod
    def apply(self, image):
        raise NotImplementedError