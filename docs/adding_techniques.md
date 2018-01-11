# Adding techniques

It is possible to include a new augmentation technique into the library and use it for augmentation in object classification, localization, detection and semantic segmentation. 

## Implementing the technique

In order to add a new technique it is necessary to implement a class that extends the ITechnique abstract class. This abstract class has two methods:

* The constructor that expects a list of parameters, that will be employed to configure the augmentation technique, and a boolean that indicates whether the technique changes the annotation in the case of localization, detection and semantic segmentation.

* A method called apply that takes an image as input and applies the augmentation technique returning the modified image as output. 

## Adding the technique to the factory

To integrate the new technique with the rest of the framework, it is also necessary to modify the list of Techniques provided in the techniqueFactory.py file to add the class of the new technique. 

## Including the technique in the Java wizard

To include the new technique in the Java wizard, it is necessary to modify the configuration file of the wizard and include a line with the new method. 
