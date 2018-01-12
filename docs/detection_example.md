# Augmenting a dataset for object detection

In this section, we will use a small set of images annotated with the position of stomas show how the library can be used for image augmentation for object detection. The dataset and the configuration file that we will employ for this example is available at the [datasets folder](datasets/detection).

## PascalVOC-PascalVOC-Linear

In this example, we show how we can use the library for augmenting a dataset of images that are annotated using the PascalVOC format to generate a new dataset with the same format. In this example, we use four augmentation techniques: equalize histogram, median blur, rotation, and croping. The former two techniques do not modify the annotation of the image, but the latter two modify the annotation. 

The json file for this example (called stoma_pascalvoc_pascalvoc_linear.json) is the following one. If you want to reproduce this example, you only need to change the value for the input_path and output_path parameters.   

```json
{
  "augmentation_techniques":[
    [
      "equalize_histogram",
      {
        
      }
    ],
    [
      "median_blur",
      {
        "kernel":"3"
      }
    ],
    [
      "rotate",
      {
        "angle":"90"
      }
    ],
    [
      "crop",
      {
        "startFrom":"TOPLEFT",
        "percentage":"0.8"
      }
    ]
  ],
  "generation_mode":"linear",
  "problem":"detection",
  "output_mode":"pascalvoc",
  "parameters":{
    "outputPath":"/home/joheras/Escritorio/augmented/"
  },
  "annotation_mode":"pascalvoc",
  "input_path":"/home/joheras/Escritorio/Research/CLoDeSeAugmentor/docs/datasets/detection/stoma"
}
```

To run the augmentation process, the following command must be executed from the terminal.

```cmd
python augment.py -c violins_pascalvoc_pascalvoc_linear.json
```

We can see that the position of the violin is computed correctly in all the cases. 

Original image
![Original](images/stoma.jpg)

Image with equalized histogram (non-altering technique)
![Equalize histogram](images/stoma0.jpg)

Image with median blurring (non-altering technique)
![Median blurring](images/stoma1.jpg)

Image with rotation (altering technique)
![Rotation](images/stoma2.jpg)

Image with croping (altering technique)
![Cropping](images/stoma3.jpg)
