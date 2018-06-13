from detection import detectBox,detectBoxes
from ..techniques.technique import AlteringTechnique,NonAlteringTechnique


class Generator(object):

    def __init__(self,technique):
        if (isinstance(technique, AlteringTechnique)) or (isinstance(technique, NonAlteringTechnique)):
            self.technique = technique
        else:
            raise ValueError("The technique should be an object of the class Technique")

    def applyForClassification(self, image):
        return self.technique.apply(image)


    def applyForLocalization(self,image,box):
        if(isinstance(self.technique,AlteringTechnique)):
            return [self.technique.apply(image),
                    detectBox(image,box,self.technique.apply)]
        else:
            return [self.technique.apply(image),box]

    def applyForDetection(self, image, boxes):
        if (isinstance(self.technique, AlteringTechnique)):
            return [self.technique.apply(image),
                    detectBoxes(image, boxes, self.technique.apply)]
        else:
            return [self.technique.apply(image), boxes]

    def applyForSegmentation(self, image, imageLabel):
        if (isinstance(self.technique, AlteringTechnique)):
            return [self.technique.apply(image),
                    self.technique.apply(imageLabel)]
        else:
            return [self.technique.apply(image), imageLabel]


