from __future__ import absolute_import
from .transformerList import Transformers



def transformerGenerator(problem):
    transformer = Transformers[problem]
    if transformer is None:
        raise ValueError("That type of problem is not available")

    return lambda technique,dictLabels=None : transformer(technique,dictLabels)