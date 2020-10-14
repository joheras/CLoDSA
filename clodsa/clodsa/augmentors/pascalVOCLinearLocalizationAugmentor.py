from __future__ import absolute_import
from builtins import str
from builtins import object
from .iaugmentor import IAugmentor
from imutils import paths
import os
import cv2
from joblib import Parallel, delayed
import xml.etree.ElementTree as ET
from .utils import prettify



def generateXML(filename,outputPath,w,h,d,boxes):
    top = ET.Element('annotation')
    childFolder = ET.SubElement(top, 'folder')
    childFolder.text = 'images'
    childFilename = ET.SubElement(top, 'filename')
    childFilename.text = filename[0:filename.rfind(".")]
    childPath = ET.SubElement(top, 'path')
    childPath.text = outputPath + "/" + filename
    childSource = ET.SubElement(top, 'source')
    childDatabase = ET.SubElement(childSource, 'database')
    childDatabase.text = 'Unknown'
    childSize = ET.SubElement(top, 'size')
    childWidth = ET.SubElement(childSize, 'width')
    childWidth.text = str(w)
    childHeight = ET.SubElement(childSize, 'height')
    childHeight.text = str(h)
    childDepth = ET.SubElement(childSize, 'depth')
    childDepth.text = str(d)
    childSegmented = ET.SubElement(top, 'segmented')
    childSegmented.text = str(0)
    for box in boxes:
        (category, (x,y,wb,hb)) = box
        childObject = ET.SubElement(top, 'object')
        childName = ET.SubElement(childObject, 'name')
        childName.text = category
        childPose = ET.SubElement(childObject, 'pose')
        childPose.text = 'Unspecified'
        childTruncated = ET.SubElement(childObject, 'truncated')
        childTruncated.text = '0'
        childDifficult = ET.SubElement(childObject, 'difficult')
        childDifficult.text = '0'
        childBndBox = ET.SubElement(childObject, 'bndbox')
        childXmin = ET.SubElement(childBndBox, 'xmin')
        childXmin.text = str(x)
        childYmin = ET.SubElement(childBndBox, 'ymin')
        childYmin.text = str(y)
        childXmax = ET.SubElement(childBndBox, 'xmax')
        childXmax.text = str(x+wb)
        childYmax = ET.SubElement(childBndBox, 'ymax')
        childYmax.text = str(y+hb)
    return prettify(top)

#
def readAndGenerateImage(outputPath, transformers, i_and_imagePath):
    (i, imagePath) = i_and_imagePath
    image = cv2.imread(imagePath)
    name = imagePath.split(os.path.sep)[-1]
    labelPath = '/'.join(imagePath.split(os.path.sep)[:-1]) + "/"+name[0:name.rfind(".")] + ".xml"
    tree = ET.parse(labelPath)
    root = tree.getroot()
    objects = root.findall('object')
    if(len(objects)!=1):
        raise Exception("Since this is a localization problem, the xml should only contain one object")
    object = objects[0]
    category = object.find('name').text
    bndbox = object.find('bndbox')
    x  = int(bndbox.find('xmin').text)
    y = int(bndbox.find('ymin').text)
    h = int(bndbox.find('ymax').text)-y
    w = int(bndbox.find('xmax').text) - x

    for (j, transformer) in enumerate(transformers):
        (newimage, box) = transformer.transform(image, (category, (x, y, w, h)))
        if box is not None:
            cv2.imwrite(outputPath + "/" + str(i) + "_" + str(j) + "_" + name,
                        newimage)
            (hI,wI) =image.shape[:2]
            if(len(image.shape)==3):
                d = 3
            else:
                d=1
            file = open(outputPath + "/" + str(i) + "_" + str(j) + "_" + name[0:name.rfind(".")]+".xml", "w")
            file.write(generateXML(str(i) + "_" + str(j) + "_" + name,outputPath,wI,hI,d,[box]))
            file.close()


# # This class serves to generate images for a localization
# # problem where all the images in the given folder, and the labels
# # are given in the same folder with the same name and using the PASCAL VOC format.
# # Example:
# # - Folder
# # |- image1.jpg
# # |- image1.xml
# # |- image2.jpg
# # |- image2.xml
# # |- ...
# #
#
class PascalVOCLinearLocalizationAugmentor(IAugmentor):

    def __init__(self,inputPath,parameters):
        IAugmentor.__init__(self)
        self.inputPath = inputPath
        # output path represents the folder where the images will be stored
        if parameters["outputPath"]:
            self.outputPath = parameters["outputPath"]
        else:
            raise ValueError("You should provide an output path in the parameters")


    def readImagesAndAnnotations(self):
        self.imagePaths = list(paths.list_files(self.inputPath,validExts=(".jpg", ".jpeg", ".png", ".bmp",".tiff",".tif")))
        self.labelPaths = list(paths.list_files(self.inputPath,validExts=(".xml")))
        if (len(self.imagePaths) != len(self.labelPaths)):
            raise Exception("The number of images is different to the number of annotations")

    def applyAugmentation(self):
        self.readImagesAndAnnotations()
        #[readAndGenerateImage(self.outputPath, self.generators, x) for x in enumerate(self.imagePaths)]
        Parallel(n_jobs=-1)(delayed(readAndGenerateImage)(self.outputPath,self.transformers,x) for x in enumerate(self.imagePaths))

