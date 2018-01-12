# Augmenting a dataset for object classification

In this section, we will use a subset of the [cats and dogs dataset]() to show how the library can be used for image augmentation for object classification. The dataset and the configuration files that we will employ for these examples is available at the [datasets folder](datasets/object_classification).

## Folder-Folder-Linear

In this first example, we show how we can use the library for augmenting a dataset of images saved in folders and store the result in another folder. In this example, we use four augmentation techniques: equalize histogram, median blur, salt and pepper noise, and croping. The json file for this example (called cats_dogs_folder_folder_linear.json) is the following one. If you want to reproduce this example, you only need to change the value for the input_path and output_path parameters.   

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
      "salt_and_pepper",
      {
        "low":"0",
        "up":"25"
      }
    ],
    [
      "crop",
      {
        "startFrom":"TOPLEFT",
        "percentage":"0.9"
      }
    ]
  ],
  "generation_mode":"linear",
  "problem":"classification",
  "output_mode":"folders",
  "parameters":{
    "outputPath":"/home/joheras/cats_dogs/"
  },
  "annotation_mode":"folders",
  "input_path":"/home/joheras/Escritorio/Research/CLoDeSeAugmentor/docs/datasets/object_classification"
}
```

To run the augmentation process, the following command must be executed from the terminal.

```cmd
python ...
```



