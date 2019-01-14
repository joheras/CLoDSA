from abc import ABCMeta, abstractmethod

class ITechnique:
    __metaclass__ = ABCMeta

    def __init__(self, parameters = None,changeLabel=False):
        self.changeLabel = changeLabel
        self.parameters = parameters

    @abstractmethod
    def apply(self, image):
        raise NotImplementedError