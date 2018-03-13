from abc import ABCMeta, abstractmethod

class Technique:
    __metaclass__ = ABCMeta

    def __init__(self, parameters = None):
        self.parameters = parameters

    @abstractmethod
    def apply(self, image):
        raise NotImplementedError


class AlteringTechnique(Technique):
    __metaclass__ = ABCMeta

    def __init__(self, parameters=None):
        Technique.__init__(self, parameters)

    @abstractmethod
    def apply(self, image):
        raise NotImplementedError

class NonAlteringTechnique(Technique):
    __metaclass__ = ABCMeta

    def __init__(self, parameters=None):
        Technique.__init__(self, parameters)

    @abstractmethod
    def apply(self, image):
        raise NotImplementedError