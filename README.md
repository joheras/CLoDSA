# CLoDSA

CLoDSA is an open-source image augmentation library for object classification, localization, detection and semantic segmentation. It supports a wide variety of augmentation techniques and allows the user to easily combine them. 


## Features

* Several augmentation techniques are provided.
* Augmentation techniques can be applied for object classification, localization, detection, and semantic segmentation.
* A Java wizard to configure the library.
* Several input modes for reading the datasets.
* Several output modes to generate the augmented dataset. 
* It is possible to easily add new augmentation techniques and apply them for object classification, localization, detection, and semantic segmentation. 


## Requirements and installation of the library

The library uses Python 2.7, which must be installed. 

The following packages must be installed:

  * numpy
  * scipy
  * scikit-image
  * mahotas
  * imutils
  * keras
  * commentjson
  * h5py
  * scikit_learn
  * progressbar2
  * OpenCV (i.e. `cv2` must be available in python). 

When executing the installer, these packages will be automatically installed/upgraded where needed. This is not the case for OpenCV, which must be installed manually. A good tutorial explaining how to install OpenCV and Ubuntu is available at [Pyimagesearch](https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/).

Once the packages are available, `clodsa` can be installed using the following command

    pip install clodsa

This installs the latest version directly from github. If any error pops up, try adding ``sudo`` in front (i.e. ``sudo pip install clodsa``).

Alternatively, you can install the latest version which was added to pypi via ``pip install clodsa``. That version can sometimes be behind the version on github.

To uninstall the library use ``pip uninstall clodsa``.

## Requirements and installation of the wizard

To install the wizard, you need to follow the instructions provided in the [wizard page](java_wizard/).


## Documentation

* [Method for augmenting images in classification, localization, detection and semantic segmentation](docs/method.md)
* [Augmentation techniques](docs/augmentation_techniques.md)
* [Configuration options](docs/configuration.md)
* [Input-output options](docs/input-output-generation.md)
* [Adding new techniques](docs/adding_techniques.md)
* [Previsualization](docs/preview.md)
* [Related projects](docs/related.md)


## Examples

* [Object classification](docs/object_classification_example.md)
* [Localization](docs/localization_example.md)
* [Detection](docs/detection_example.md)
* [Semantic Segmentation](docs/semantic_segmentation_example.md)


## List of augmentation techniques

The following table presents the list of augmenters available in the library and the parameters to configure them. We split them into two groups: those that change the label in the problems of localization, detection and semantic segmentation, and those that do not change the annotation.


| Technique | Description | Parameters | Change annotation |
| --- | --- | --- | --- |
| Average blurring| Smoothes the image using an average filter. | *kernel*: Kernel size for average blurring (either 3, 5, 7, 9 or 11).| No |
| Bilateral blurring | Applies bilateral blurring to the image. | *diameter*: Diameter size for bilateral blurring (integer value). *sigmaColor*: sigma color for bilateral blurring (integer value). *sigmaSpace*: sigma space for bilateral blurring (integer value)  | No |
| Blurring | Blurs an image using the normalized box filter. | *ksize*: Kernel size for blurring (either 3, 5, 7, 9 or 11).  | No |
| Change to HSV | Changes the color space from RGB to HSV. | No parameters. | No |
| Change to LAB | Changes the color space from RGB to LAB. | No parameters.| No |
| Crop | Crops pixels at the sides of the image. | *percentage*:  Percentage to keep during cropping (value between 0 and 1). *startFrom*: Position to start the cropping ("TOPLEFT", "TOPRIGHT", "BOTTOMLEFT", "BOTTOMRIGHT", "CENTER","TOPLEFT")  | Yes |
| Dropout | Sets some pixels in the image to zero. | *percentage*: Percentage of pixels to drop (value between 0 and 1). | No |
| Elastic deformation | Applies elastic deformation as explained in the paper:  P. Simard, D. Steinkraus, and J. C. Platt. Best practices for convolutional neural networks applied to visual document analysis. Proceedings of the 12th International Conference on Document Analysis and Recognition (ICDAR'03) vol. 2, pp. 958--964. IEEE Computer Society. 2003. | *alpha*:  Alpha value for elastic deformation. *sigma*: Sigma value for elastic deformation | Yes |
| Equalize histogram | Applies histogram equalization to the image. | No parameters. | No |
| Flip | Flips the image horizontally, vertically or both. | *flip*: Flip value: 1 for vertical flip, 0 for horizontal flip, -1 for both | Yes | 
| Gamma correction | Applies gamma correction to the image.| *gamma*: Gamma value (should be between 0 and 2.5)| No |
| Gaussian blurring | Blurs an image using a Gaussian filter.| *kernel*: Kernel size for Gaussian blurring (either 3, 5, 7, 9 or 11).| No |
| Gaussian noise | Adds Gaussian noise to the image.  | *mean*: Mean value for Gaussian noise (an integer). *sigma*: Sigma value for Gaussian noise (an integer). | No |
| Invert | Inverts all values in images, i.e. sets a pixel from value v to 255-v | No parameters. | No |
| Median blurring | Blurs an image using the median filter. | *kernel*: Kernel size for median blurring (either 3, 5, 7, 9 or 11). | No |
| None | This augmentation technique does not change the image. | No parameters. | No |
| Raise blue channel | Raises the values in the blue channel. | *power*: Power for raising blue channel (value between 0.25 and 4) | No |
| Raise green channel | Raises the values in the green channel. | *power*: Power for raising green channel (value between 0.25 and 4) | No |
| Raise hue | Raises the hue value. | *power*: Power for raising hue channel (value between 0.25 and 4) | No |
| Raise red channel | Raises the value in the red channel. | *power*: Power for raising red channel (value between 0.25 and 4)| No |
| Raise saturation | Raises the saturation. | *power*: Power for raising saturation channel (value between 0.25 and 4) | No |
| Raise value | Raise the value of pixels. | *power*: Power for raising value channel (value between 0.25 and 4) | No |
| Resize | Resizes the image. | *percentage*: Percentage for resizing (double value). *method*: Method for resizing ("INTER_NEAREST", "INTER_LINEAR", "INTER_AREA", "INTER_CUBIC", "INTER_LANCZOS4","INTER_AREA") |  Yes |
| Rotate | Rotates the image. | *angle*: Angle for rotation (value between 0 and 360) | Yes |
| Salt and Pepper | Adds salt and pepper noise to the image. | *low*: Low value for salt and pepper (positive integer). *up*: Up value for salt and pepper (positive integer). | No |
| Sharpen | Sharpens the image. | No parameters. | No |
| Shift channels | Shifts the channels of the image. | "shift": Shifts input image channels in the range given (value between 0 and 1). | No |
| Shearing | Shears the image.| *a* : value for shearing (positive double). | Yes |
| Translation | Translates the image. | *x*: x transltation (integer). *y*: y translation (integer). | Yes |
