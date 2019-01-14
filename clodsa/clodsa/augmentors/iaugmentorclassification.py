from __future__ import absolute_import
from .iaugmentor import IAugmentor
from abc import ABCMeta
from future.utils import with_metaclass

class IAugmentorClassification(with_metaclass(ABCMeta, IAugmentor)):
    def __init__(self,inputPath,outputPath):
        self.inputPath = inputPath
        self.outputPath = outputPath

