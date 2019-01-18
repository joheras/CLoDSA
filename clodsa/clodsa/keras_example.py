from __future__ import absolute_import
from keras.optimizers import SGD
import argparse
from .utils.conf import Conf
from .augmentors.augmentorFactory import createAugmentor
from .transformers.transformerFactory import transformerGenerator
from .techniques.techniqueFactory import createTechnique
from .utils.minivgg import MiniVGGNet

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required=True, help="path to configuration file")
args = vars(ap.parse_args())

conf = Conf(args["conf"])
# First, we read the parameters
problem = conf["problem"]
annotationMode = conf["annotation_mode"]
outputMode = conf["output_mode"]

if not(outputMode=="keras"):
    exit()

generationMode = conf["generation_mode"]
inputPath = conf["input_path"]
parameters = conf["parameters"]
augmentationTechniques = conf["augmentation_techniques"]

# Second, we create the augmentor
augmentor = createAugmentor(problem,annotationMode,outputMode,generationMode,inputPath,
                            parameters)

# Third, we load the techniques and add them to the augmentor
techniques = [createTechnique(technique,param) for (technique,param) in
              augmentationTechniques]

transformer = transformerGenerator(problem)

for technique in techniques:
    augmentor.addTransformer(transformer(technique))


# Definition of the model
opt = SGD(lr=0.05)
model = MiniVGGNet.build(width=parameters["width"], height=parameters["height"], depth=3)
model.compile(loss="categorical_crossentropy", optimizer=opt,metrics=["accuracy"])

# Training the model
H = model.fit_generator(augmentor.applyAugmentation(),
                         steps_per_epoch= parameters["batchSize"],
                         epochs=100, verbose=1)
