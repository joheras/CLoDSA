from __future__ import absolute_import
from .augmentorsList import Augmentors

def createAugmentor(problem,annotationmode,outputmode,generationmode,inputPath,parameters):
    Augmentor = Augmentors[problem][annotationmode][outputmode][generationmode]
    if Augmentor is None:
        raise ValueError("These parameters are not currently supported")

    return Augmentor(inputPath,parameters)
