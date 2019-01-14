from __future__ import absolute_import
from .techniques.techniqueFactory import createTechnique
import cv2
import numpy as np

# In this file, it is shown how the different techniques can be applied
# individually to an image.


# Loading the image
img = cv2.imread("sample_images/cat1.jpg")

t = createTechnique("cropSize", {"x" : 0,"y":0,"width":20,"height":20})
img1 = t.apply(img)
cv2.imshow("cropSize",np.hstack([img,img1]))
cv2.waitKey(0)
#
# t = createTechnique("bilateral_blurring", {"diameter" : 11, "sigmaColor": 21, "sigmaSpace":7})
# img1 = t.apply(img)
# cv2.imwrite("bilateral_blurring.jpg",np.hstack([img,img1]))
#
# t = createTechnique("blurring", {"ksize" : 5})
# img1 = t.apply(img)
# cv2.imwrite("blurring.jpg",np.hstack([img,img1]))
#
# t = createTechnique("change_to_hsv",{})
# img1 = t.apply(img)
# cv2.imwrite("change_to_hsv.jpg",np.hstack([img,img1]))
#
# t = createTechnique("change_to_lab",{})
# img1 = t.apply(img)
# cv2.imwrite("change_to_lab.jpg",np.hstack([img,img1]))
#
# t = createTechnique("crop",{"percentage":0.8,"startFrom": "TOPLEFT"})
# img1 = t.apply(img)
# cv2.imwrite("crop.jpg",img1)
#
# t = createTechnique("dropout",{"percentage":0.05})
# img1 = t.apply(img)
# cv2.imwrite("dropout.jpg",np.hstack([img,img1]))
#
# t = createTechnique("elastic",{"alpha":5,"sigma":0.05})
# img1 = t.apply(img)
# cv2.imwrite("elastic.jpg",np.hstack([img,img1]))
#
# t = createTechnique("equalize_histogram",{})
# img1 = t.apply(img)
# cv2.imwrite("equalize.jpg",np.hstack([img,img1]))
#
# t = createTechnique("flip",{"flip":0})
# t1 = createTechnique("flip",{"flip":1})
# t2 = createTechnique("flip",{"flip":-1})
# img1 = t.apply(img)
# img2 = t1.apply(img)
# img3 = t2.apply(img)
# cv2.imwrite("flip.jpg",np.hstack([img,img1,img2,img3]))
#
#
# t = createTechnique("gamma",{"gamma":1.5})
# img1 = t.apply(img)
# cv2.imwrite("gamma.jpg",np.hstack([img,img1]))
#
# t = createTechnique("gaussian_blur", {"kernel" : 5})
# img1 = t.apply(img)
# cv2.imwrite("gaussian_blurring.jpg",np.hstack([img,img1]))
#
# t = createTechnique("gaussian_noise", {"mean" : 0,"sigma":10})
# img1 = t.apply(img)
# cv2.imwrite("gaussian_noise.jpg",np.hstack([img,img1]))
#
# t = createTechnique("invert",{})
# img1 = t.apply(img)
# cv2.imwrite("invert.jpg",np.hstack([img,img1]))
#
# t = createTechnique("median_blur", {"kernel" : 5})
# img1 = t.apply(img)
# cv2.imwrite("median_blurring.jpg",np.hstack([img,img1]))
#
#
# t = createTechnique("none",{})
# img1 = t.apply(img)
# cv2.imwrite("none.jpg",np.hstack([img,img1]))
#
#
# t = createTechnique("raise_blue", {"power" : 0.9})
# img1 = t.apply(img)
# cv2.imwrite("raise_blue.jpg",np.hstack([img,img1]))
#
# t = createTechnique("raise_green", {"power" : 0.9})
# img1 = t.apply(img)
# cv2.imwrite("raise_green.jpg",np.hstack([img,img1]))
#
# t = createTechnique("raise_red", {"power" : 0.9})
# img1 = t.apply(img)
# cv2.imwrite("raise_red.jpg",np.hstack([img,img1]))
#
# t = createTechnique("raise_hue", {"power" : 0.9})
# img1 = t.apply(img)
# cv2.imwrite("raise_hue.jpg",np.hstack([img,img1]))
#
# t = createTechnique("raise_saturation", {"power" : 0.9})
# img1 = t.apply(img)
# cv2.imwrite("raise_saturation.jpg",np.hstack([img,img1]))
#
# t = createTechnique("raise_value", {"power" : 0.9})
# img1 = t.apply(img)
# cv2.imwrite("raise_value.jpg",np.hstack([img,img1]))
#
#
# t = createTechnique("resize", {"percentage" : 0.9,"method":"INTER_NEAREST"})
# img1 = t.apply(img)
# cv2.imwrite("resize.jpg",img1)
#
# t = createTechnique("rotate", {"angle" : 90})
# img1 = t.apply(img)
# cv2.imwrite("rotate.jpg",img1)
#
# t = createTechnique("salt_and_pepper", {"low" : 0,"up":25})
# img1 = t.apply(img)
# cv2.imwrite("salt_and_peper.jpg",np.hstack([img,img1]))
#
#
# t = createTechnique("sharpen", {})
# img1 = t.apply(img)
# cv2.imwrite("sharpen.jpg",np.hstack([img,img1]))
#
# t = createTechnique("shift_channel", {"shift":0.2})
# img1 = t.apply(img)
# cv2.imwrite("sharpen.jpg",np.hstack([img,img1]))
#
# t = createTechnique("shearing", {"a":0.5})
# img1 = t.apply(img)
# cv2.imwrite("shearing.jpg",np.hstack([img,img1]))
#
# t = createTechnique("translation", {"x":10,"y":10})
# img1 = t.apply(img)
# cv2.imwrite("translation.jpg",np.hstack([img,img1]))

