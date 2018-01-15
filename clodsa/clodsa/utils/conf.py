# import the necessary packages
import commentjson as json

class Conf:
	def __init__(self, confPath):
		# load and store the configuration and update the object's dictionary
		conf = json.loads(open(confPath).read())
		self.__dict__.update(conf)

	def __getitem__(self, k):
		# return the value associated with the supplied key
		return self.__dict__.get(k, None)