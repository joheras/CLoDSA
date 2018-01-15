from detection import detectBox,detectBoxes



class Generator(object):

    def __init__(self,technique):
        self.changeLabel = technique.changeLabel
        self.technique = technique

    def applyForClassification(self, image):
        return self.technique.apply(image)


    def applyForLocalization(self,image,box):
        if(self.changeLabel):
            return [self.technique.apply(image),
                    detectBox(image,box,self.technique.apply)]
        else:
            return [self.technique.apply(image),box]

    def applyForDetection(self, image, boxes):
        if (self.changeLabel):
            return [self.technique.apply(image),
                    detectBoxes(image, boxes, self.technique.apply)]
        else:
            return [self.technique.apply(image), boxes]

    def applyForSegmentation(self, image, imageLabel):
        if (self.changeLabel):
            return [self.technique.apply(image),
                    self.technique.apply(imageLabel)]
        else:
            return [self.technique.apply(image), imageLabel]


