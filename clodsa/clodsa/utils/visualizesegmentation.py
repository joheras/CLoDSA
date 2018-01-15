import os
import cv2
import xml.etree.ElementTree as ET
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
ap.add_argument("-l", "--label", required=True, help="path to the label")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
label = cv2.imread(args["label"])

blending = cv2.addWeighted(image,1,label,0.2,0.0)
# cv2.imshow("Blending",blending)
# cv2.waitKey(0)
cv2.imwrite("blending3.jpg",blending)