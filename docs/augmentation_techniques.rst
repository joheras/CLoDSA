======================
Overview of Augmentation techniques
======================

We present the different techniques that can be applied to augment a dataset of images. In order to generate the samples presented in this section, it is necessary to load some libraries.

::
from techniques.techniqueFactory import createTechnique
import cv2
import numpy as np
..


----------------------
Average blurring
----------------------

Smoothes the image using an average filter. 

.. figure:: images/average_blurring.jpg
    :alt: Average blurring

----------------------
Bilateral blurring
----------------------

Applies bilateral blurring to the image. 

.. figure:: images/bilateral_blurring.jpg
    :alt: Bilateral blurring

----------------------
Blurring
----------------------

Blurs an image using the normalized box filter.

.. figure:: images/blurring.jpg
    :alt: Blurring

----------------------
Change to HSV
----------------------

Changes the color space from RGB to HSV. 

.. figure:: images/change_to_hsv.jpg
    :alt: Change color space to HSV

----------------------
Change to LAB
----------------------

Changes the color space from RGB to LAB. 

.. figure:: images/change_to_lab.jpg
    :alt: Change color space to LAB


----------------------
Crop
----------------------

Crops pixels at the sides of the image.

.. figure:: images/crop.jpg
    :alt: Crop the image

----------------------
Dropout
----------------------

Sets some pixels in the image to zero.

.. figure:: images/dropout.jpg
    :alt: Dropout

----------------------
Elastic deformation
----------------------

Applies elastic deformation as explained in the paper:  P. Simard, D. Steinkraus, and J. C. Platt. Best practices for convolutional neural networks applied to visual 
document analysis. Proceedings of the 12th International Conference on Document Analysis and Recognition (ICDAR'03) vol. 2, pp. 958--964. IEEE Computer Society. 2003.

.. figure:: images/elastic.jpg
    :alt: Elastic


----------------------
Equalize histogram
----------------------

Applies histogram equalization to the image.

.. figure:: images/equalize.jpg
    :alt: Equalize histogram


----------------------
Flip
----------------------

Flips the image horizontally, vertically or both. 

.. figure:: images/flip.jpg
    :alt: Flip

----------------------
Gamma correction
----------------------

Applies gamma correction to the image.

.. figure:: images/gamma.jpg
    :alt: Gamma correction

----------------------
Gaussian blurring
----------------------

Blurs an image using a Gaussian filter.

.. figure:: images/gaussian_blurring.jpg
    :alt: Gaussian blurring

----------------------
Gaussian noise
----------------------

Adds Gaussian noise to the image. 

.. figure:: images/gaussian_noise.jpg
    :alt: Gaussian noise

----------------------
Invert
----------------------

Inverts all values in images, i.e. sets a pixel from value v to 255-v

.. figure:: images/invert.jpg
    :alt: Invert


----------------------
Median blurring
----------------------

Blurs an image using the median filter.

.. figure:: images/median_blurring.jpg
    :alt: Median blurring

----------------------
None
----------------------

This augmentation technique does not change the image. 

.. figure:: images/none.jpg
    :alt: None

----------------------
Raise blue channel
----------------------

Raises the values in the blue channel.

.. figure:: images/raise_blue.jpg
    :alt: Raise blue


----------------------
Raise green channel
----------------------

Raises the values in the green channel.

.. figure:: images/raise_green.jpg
    :alt: Raise green

----------------------
Raise hue
----------------------

Raises the hue value.

.. figure:: images/raise_hue.jpg
    :alt: Raise hue

----------------------
Raise red channel
----------------------

Raises the value in the red channel.

.. figure:: images/raise_red.jpg
    :alt: Raise red

----------------------
Raise saturation
----------------------

Raises the saturation.

.. figure:: images/raise_saturation.jpg
    :alt: Raise saturation

----------------------
Raise value
----------------------

Raise the value of pixels.

.. figure:: images/raise_value.jpg
    :alt: Raise value


----------------------
Resize
----------------------

Resizes the image.

.. figure:: images/resize.jpg
    :alt: Resize

----------------------
Rotate
----------------------

Rotates the image.

.. figure:: images/rotate.jpg
    :alt: Rotate

----------------------
Salt and Pepper
----------------------

Adds salt and pepper noise to the image.

.. figure:: images/salt_and_pepper.jpg
    :alt: Salt and pepper

----------------------
Sharpen
----------------------

Sharpens the image. 

.. figure:: images/sharpen.jpg
    :alt: Sharpen

----------------------
Shift channel
----------------------

Shifts the channels of the image.

.. figure:: images/shift_channel.jpg
    :alt: Shift channel

----------------------
Shearing
----------------------

Shears the image.

.. figure:: images/shearing.jpg
    :alt: Shearing


----------------------
Translation
----------------------

Translates the image. 

.. figure:: images/translation.jpg
    :alt: Translation



