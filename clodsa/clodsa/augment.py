from __future__ import absolute_import
from .augmentors.augmentorFactory import createAugmentor
from .transformers.transformerFactory import transformerGenerator
from .techniques.techniqueFactory import createTechnique
import argparse
from .utils.conf import Conf


def main(conf):
	#ap = argparse.ArgumentParser()
	#ap.add_argument("-c", "--conf", required=True, help="path to configuration file")
	#args = vars(ap.parse_args())


	conf = Conf(conf)

	# First, we read the parameters
	problem = conf["problem"]
	annotationMode = conf["annotation_mode"]
	outputMode = conf["output_mode"]
	generationMode = conf["generation_mode"]
	inputPath = conf["input_path"]
	parameters = conf["parameters"]
	augmentationTechniques = conf["augmentation_techniques"]

	# Second, we create the augmentor
	augmentor = createAugmentor(problem,annotationMode,outputMode,generationMode,inputPath,
		                    parameters)

	# Third, we load the techniques and add them to the augmentor
	techniques = [createTechnique(technique,parameters) for (technique,parameters) in
		      augmentationTechniques]

	transformer = transformerGenerator(problem)

	for technique in techniques:
	    augmentor.addTransformer(transformer(technique))

	# Finally, we apply the augmentation
	augmentor.applyAugmentation()

