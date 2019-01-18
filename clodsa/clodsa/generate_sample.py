from __future__ import print_function
from __future__ import absolute_import
from .augmentors.augmentorFactory import createAugmentor
from .transformers.transformerFactory import transformerGenerator
from .techniques.techniqueFactory import createTechnique
import argparse
from .utils.conf import Conf
import cv2
from .mosaic import generateMosaic


def main(conffile,imfile):
	#ap = argparse.ArgumentParser()
	#ap.add_argument("-c", "--conf", required=True, help="path to configuration file")
	#ap.add_argument("-i", "--image", required=True, help="path to the image to generate the sample")
	#args = vars(ap.parse_args())


	conf = Conf(conffile)
	image = cv2.imread(imfile)

	# First, we read the parameters
	problem = conf["problem"]
	annotationMode = conf["annotation_mode"]
	outputMode = conf["output_mode"]
	generationMode = conf["generation_mode"]
	inputPath = conf["input_path"]
	parameters = conf["parameters"]
	augmentationTechniques = conf["augmentation_techniques"]
	print(augmentationTechniques)
	# Second, we create the augmentor
	augmentor = createAugmentor(problem,annotationMode,outputMode,generationMode,inputPath,
		                    parameters)


	# We apply the augmentation
	images = []
	transformer = transformerGenerator(problem)
	for (technique,parameters) in augmentationTechniques:
	    tech = createTechnique(technique,parameters)
	    im = transformer(tech).transform(image)
	    cv2.putText(im,technique,(10,10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
	    images.append(im)

	cv2.imshow("Mosaic",generateMosaic(images))
	cv2.waitKey(0)

