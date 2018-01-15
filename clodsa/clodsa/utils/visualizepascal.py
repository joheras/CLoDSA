import os
import cv2
import xml.etree.ElementTree as ET
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image, there must be also an xml file with the same name (but with xml extension)")
args = vars(ap.parse_args())



def readAndShowAnnotatedImage(imagePath):

    image = cv2.imread(imagePath)
    name = imagePath.split(os.path.sep)[-1]
    labelPath = '/'.join(imagePath.split(os.path.sep)[:-1]) + "/"+name[0:name.rfind(".")] + ".xml"
    tree = ET.parse(labelPath)
    root = tree.getroot()
    objects = root.findall('object')
    boxes = []
    for object in objects:
        category = object.find('name').text
        bndbox = object.find('bndbox')
        x  = int(bndbox.find('xmin').text)
        y = int(bndbox.find('ymin').text)
        w = int(bndbox.find('ymax').text)-y
        h = int(bndbox.find('xmax').text) - x
        boxes.append((category, (x, y, w, h)))

    for box in enumerate(boxes):
        box = box[1][1]
        cv2.rectangle(image,(box[0],box[1]),(box[0]+box[3],box[1]+box[2]),(0,0,255),2)

    cv2.imshow("Annotated image",image)
    cv2.waitKey(0)
    # cv2.imwrite("im.jpg",image)

readAndShowAnnotatedImage(args["image"])