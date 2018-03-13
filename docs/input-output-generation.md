# Adding input-output-generation modes

It is possible to include new modes for input, output and generation. 

## Implementing the new mode

In order to add a new mode, it is necessary to implement a class that extends the IAugmentor abstract class. This abstract class has two methods:

* The method readImagesAndAnnotations serves to indicate how the images and annotations are read from the hard drive.

* The method applyAugmentation must implement how the augmentation techniques are applied and how the result is saved.  

## Adding the mode to the factory

To integrate the new mode with the rest of the framework, it is also necessary to modify the list of Augmentors provided in the augmentorsList.py file to add the class of the new technique. 

## Including the mode in the Java wizard

To include the new mode in the Java wizard, it is necessary to modify the configuration file of the wizard and include a line with the new method. 
