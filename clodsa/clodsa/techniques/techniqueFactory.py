from __future__ import absolute_import
from .techniqueList import  Techniques
from .technique import DecoratorTechnique

def createTechnique(technique,parameters,dictLabels=None):
    Technique = Techniques[technique]
    if Technique is None:
        raise ValueError("That technique is not available")
    return DecoratorTechnique(Technique(parameters),dictLabels)