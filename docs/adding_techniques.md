# Adding techniques

It is possible to include a new augmentation technique into the library and use it for augmentation in object classification, localization, detection and semantic segmentation. 

## Implementing the technique

In order to add a new technique it is necessary to implement a class that extends one of the two abstract classes AlteringTechnique and NonAlteringTechnique. The former should be employed to implement techniques that change the annotation in the case of localization, detection and semantic segmentation; otherwise, the latter should be used. In both cases, these two classes have two methods:

* The constructor that expects a list of parameters, that will be employed to configure the augmentation technique.

* A method called apply that takes an image as input and applies the augmentation technique returning the modified image as output. 

## Adding the technique to the factory

To integrate the new technique with the rest of the framework, it is also necessary to modify the list of Techniques provided in the techniqueList.py file to add the class of the new technique. 

## Including the technique in the Java wizard

To include the new technique in the Java wizard, it is necessary to modify the configuration file of the wizard and include a line with the new method. 
