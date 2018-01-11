# Configuration

In this section, we present the different options to configure the framework. In order to use this library, it is necessary to fix, in a configuration file, five parameters: the dataset of images, the kind of problem, the input, the ouput, the generation mode, and the techniques to be applied. Since generating a configuration file might be cumbersome for some users, we have created a ![Java program](java_program.md) to simplify this task. 


## Dataset

The dataset of images is given by the path where the images are located.

## The kind of problem

The kind of problem is either classification, localization, detection, or segmentation. 


## Input-Output-Generation

Before explaining the input, output and generatio modes, it is important to understand how the images are annotated in each of the four problems. In the case of object classification, each image is labeled with a prefixed category; for object localization, a bounding box indicating the position of the object in the image is provided; for object detection, a list of bounding boxes and the category of the objects inside those boxes are given; finally, in semantic segmentation, each pixel of the image is labeled with the class of its enclosing object.

### Object Classification

There are several options to augment a dataset for an object classification problem.

#### Folders-Folders-Linear

In this mode, the input dataset of images is organized by folders, and the label of an image is given by the name of the containing folder. The output produced is the dataset of augmented images organized with the same structure as the input folder. The generation mode in this case is linear; that is, given a dataset of n images, and a list of m augmentation techniques, each technique is applied to the n images.

#### Folders-hdf5-Linear

In this mode, the input dataset of images is organized by folders, and the label of an image is given by the name of the containing folder. The output produced is the dataset of augmented images stored in an hdf5 file. The generation mode in this case is linear; that is, given a dataset of n images, and a list of m augmentation techniques, each technique is applied to the n images.

#### Folders-hdf5-Power

In this mode, the input dataset of images is organized by folders, and the label of an image is given by the name of the containing folder. The output produced is the dataset of augmented images stored in an hdf5 file. The generation mode in this case is power. The power mode is a pipeline approach where augmentation techniques are chained together. 
In this approach, the images produced in one step of the pipeline are added to the dataset that will be fed in the step of the pipeline.

#### Folders-keras-linear

In this mode, the input dataset of images is organized by folders, and the label of an image is given by the name of the containing folder. The output produced is a batch of images that can be fed to Keras. The generation mode in this case is linear; that is, given a dataset of n images, and a list of m augmentation techniques, each technique is applied to the n images.


### Localization

#### PascalVOC-PascalVOC-Linear

In this mode, the input dataset of images is given by an image and its annotation using the [PascalVOC format](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/). The output produced is the dataset of augmented images together with its annotation using the PascalVOC format. The generation mode in this case is linear; that is, given a dataset of n images, and a list of m augmentation techniques, each technique is applied to the n images.


#### PascalVOC-hdf5-Linear

In this mode, the input dataset of images is given by an image and its annotation using the [PascalVOC format](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/). The output produced is the dataset of augmented images stored in an hdf5 file. The generation mode in this case is linear; that is, given a dataset of n images, and a list of m augmentation techniques, each technique is applied to the n images.

#### PascalVOC-keras-Linear

In this mode, the input dataset of images is given by an image and its annotation using the [PascalVOC format](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/). The output produced is a batch of images that can be fed to Keras. The generation mode in this case is linear; that is, given a dataset of n images, and a list of m augmentation techniques, each technique is applied to the n images.


### Detection 

#### PascalVOC-PascalVOC-Linear

In this mode, the input dataset of images is given by an image and its annotation using the [PascalVOC format](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/). The output produced is the dataset of augmented images together with its annotation using the PascalVOC format. The generation mode in this case is linear; that is, given a dataset of n images, and a list of m augmentation techniques, each technique is applied to the n images.

#### PascalVOC-keras-Linear

In this mode, the input dataset of images is given by an image and its annotation using the [PascalVOC format](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/). The output produced is a batch of images that can be fed to Keras. The generation mode in this case is linear; that is, given a dataset of n images, and a list of m augmentation techniques, each technique is applied to the n images.


### Semantic Segmentation

#### Folders-Folders-Linear

In this mode, the input dataset of images is organized by folders, one folder containing the images and other folder containing the annotation images (the names must match). The output produced is the dataset of augmented images organized with the same structure as the input folder. The generation mode in this case is linear; that is, given a dataset of n images, and a list of m augmentation techniques, each technique is applied to the n images.

#### Folders-hdf5-Linear

In this mode, the input dataset of images is organized by folders, one folder containing the images and other folder containing the annotation images (the names must match). The output produced is the dataset of augmented images stored in an hdf5 file. The generation mode in this case is linear; that is, given a dataset of n images, and a list of m augmentation techniques, each technique is applied to the n images.

#### Folders-hdf5-Power

In this mode, the input dataset of images is organized by folders, one folder containing the images and other folder containing the annotation images (the names must match). The output produced is the dataset of augmented images stored in an hdf5 file. The generation mode in this case is power. The power mode is a pipeline approach where augmentation techniques are chained together. 
In this approach, the images produced in one step of the pipeline are added to the dataset that will be fed in the step of the pipeline.

#### Folders-keras-linear

In this mode, the input dataset of images is organized by folders, one folder containing the images and other folder containing the annotation images (the names must match). The output produced is a batch of images that can be fed to Keras. The generation mode in this case is linear; that is, given a dataset of n images, and a list of m augmentation techniques, each technique is applied to the n images.

### Adding input-output-generation modes

It is possible to add new input-output-generation modes easily as explained in [Adding input-output-generation-modes](input-output-generation.md)

## Techniques

![Several techniques](augmentation_techniques.md) can be applied to augment the dataset of images.

* Average Blurring 
* Bilateral Blurring
* Blurring 
* Change color space to HSV
* Change color space to LAB
* Cropping
* Dropout 
* Elastic deformations
* Equalize Histogram
* Flip
* Gamma correction
* Gaussian Blurring
* Gaussian Noise
* Invert
* Median Blurring
* None
* Raise blue channel
* Raise green channel
* Raise hue channel
* Raise red channel
* Raise saturation channel
* Raise value channel
* Resize
* Rotate
* Salt and pepper noise
* Sharpen 
* Shift channel
* Shearing
* Translation

It is possible to add new techniques easily as explained in [Adding input-output-generation-modes](adding_techniques.md)

