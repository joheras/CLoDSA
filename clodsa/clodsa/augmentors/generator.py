from __future__ import absolute_import
from builtins import object
from .detection import detectBox,detectBoxes
from ..techniques.technique import PositionVariantTechnique,PositionInvariantTechnique,DecoratorTechnique
from sklearn.externals.joblib import Parallel, delayed


class Generator(object):

    def __init__(self,technique):
        if (isinstance(technique, DecoratorTechnique)):
            self.technique = technique
        else:
            raise ValueError("The technique should be an object of the class Technique")

    def applyForClassification(self, image,label):
        return (self.technique.apply(image),self.technique.transform_label(label))


    def applyForLocalization(self,image,box):
        if(isinstance(self.technique.technique,PositionVariantTechnique)):
            return [self.technique.apply(image),
                    detectBox(image,box,self.technique)]
        else:
            return [self.technique.apply(image),(self.technique.transform_label(box[0]),box[1])]

    def applyForDetection(self, image, boxes):
        if (isinstance(self.technique.technique, PositionVariantTechnique)):
            return [self.technique.apply(image),
                    detectBoxes(image, boxes, self.technique)]
        else:
            return [self.technique.apply(image),
                    [(self.technique.transform_label(box[0]),box[1]) for box in boxes]]

    def applyForSegmentation(self, image, imageLabel):
        if (isinstance(self.technique.technique, PositionVariantTechnique)):
            return [self.technique.apply(image),
                    self.technique.apply(imageLabel)]
        else:
            return [self.technique.apply(image), imageLabel]

    def applyForInstanceSegmentation(self,image,maskLabels):
        if (isinstance(self.technique.technique, PositionVariantTechnique)):
            return [self.technique.apply(image),
                    [(self.technique.apply(mask), self.technique.transform_label(label))
                     for mask,label in maskLabels ]]
        else:
            return [self.technique.apply(image),
                    [(mask, self.technique.transform_label(label))
                     for mask, label in maskLabels]]

    def applyForZStackClassification(self,listImages,label):
        newlistImages = Parallel(n_jobs=-1)(
            delayed(self.technique.apply)(image) for image in listImages)
        return [newlistImages,self.technique.transform_label(label)]





