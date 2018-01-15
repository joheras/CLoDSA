# import the necessary packages
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import numpy as np
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from keras.applications import imagenet_utils
from keras.applications.inception_v3 import preprocess_input
import cv2

def prepare_image(imagePath,model):

	if model in ("inception", "xception", "vgg16","vgg19","resnet","densenet"):
		fixedSize = (224, 224)
		preprocess = imagenet_utils.preprocess_input
		if model in ("inception", "xception"):
			fixedSize = (299, 299)
			preprocess = preprocess_input
		if model in ("densenet"):
			fixedSize = (32,32)

		image = load_img(imagePath, target_size=fixedSize)
		image = img_to_array(image)
		image = np.expand_dims(image, axis=0)

		if model not in ("densenet"):
			image = preprocess(image)

		# return the image
		return image
	else:
		fixedSize = [231,231]
		image = cv2.imread(imagePath)
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		image = cv2.resize(image, tuple(fixedSize))

		# return the image
		return image


def build_batch(paths,model):
	# load the images from disk, prepare them for extraction, and convert
	# the list to a NumPy array
	images = [prepare_image(p,model) for p in paths]
	if model in ("inception", "xception", "vgg16","vgg19","resnet","inception", "xception","densenet"):
		images = np.array(images, dtype="float")


	# extract the labels from the image paths
	labels = [":".join(p.split("/")[-2:]) for p in paths]

	# return the labels and images
	return (labels, images)

def chunk(l, n):
	# loop over the list `l`, yielding chunks of size `n`
	for i in np.arange(0, len(l), n):
		yield l[i:i + n]