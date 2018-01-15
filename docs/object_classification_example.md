# Augmenting a dataset for object classification

In this section, we will use a subset of the [cats and dogs dataset](https://www.kaggle.com/c/dogs-vs-cats) to show how the library can be used for image augmentation for object classification. The dataset and the configuration files that we will employ for these examples is available at the [datasets folder](datasets/object_classification).

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
clodsa cats_dogs_folder_folder_linear.json
```

## Folder-Keras-Linear

In this second example, we show how we can use the library for augmenting a dataset of images saved in folders and use it to fed a Keras network. In this example, we use four augmentation techniques: equalize histogram, median blur, salt and pepper noise, and croping. The json file for this example (called cats_dogs_folder_keras_linear.json) is the following one. If you want to reproduce this example, you only need to change the value for the input_path.   

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
    "batchSize": 32,
    "width": 64,
    "height": 64
  },
  "annotation_mode":"folders",
  "input_path":"/home/joheras/Escritorio/Research/CLoDeSeAugmentor/docs/datasets/object_classification"
}
```

In this case, to run the augmentation we need to work in a python file where we define and use the network. The code of this example is available in the [project webpage](../clodsa/clodsa/keras_example.py).

We start by reading the configuration file that will be passed to the program as input. 

```python
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required=True, help="path to configuration file")
args = vars(ap.parse_args())

conf = Conf(args["conf"])
# First, we read the parameters
problem = conf["problem"]
annotationMode = conf["annotation_mode"]
outputMode = conf["output_mode"]

if not(outputMode=="keras"):
    exit()

generationMode = conf["generation_mode"]
inputPath = conf["input_path"]
parameters = conf["parameters"]
augmentationTechniques = conf["augmentation_techniques"]
```

Now, we create the augmentor:
```python
augmentor = createAugmentor(problem,annotationMode,outputMode,generationMode,inputPath,
                            parameters)

# Third, we load the techniques and add them to the augmentor
techniques = [createTechnique(technique,param) for (technique,param) in augmentationTechniques]

for technique in techniques:
    augmentor.addGenerator(Generator(technique))
```

Finally, the model is created and trained. 
```python
opt = SGD(lr=0.05)
model = MiniVGGNet.build(width=parameters["width"], height=parameters["height"], depth=3)
model.compile(loss="categorical_crossentropy", optimizer=opt,metrics=["accuracy"])

# Training the model
H = model.fit_generator(augmentor.applyAugmentation(),
                         steps_per_epoch= 32,
                         epochs=100, verbose=1)
```

In order to execute the above code, the python file must be invoked. 

```cmd
python keras_example.py -c cats_dogs_folder_keras_linear.json
```
