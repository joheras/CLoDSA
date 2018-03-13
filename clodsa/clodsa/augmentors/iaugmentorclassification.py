from iaugmentor import IAugmentor
from abc import ABCMeta

class IAugmentorClassification(IAugmentor):
    __metaclass__ = ABCMeta

    def __init__(self,inputPath,outputPath):
        self.inputPath = inputPath
        self.outputPath = outputPath

