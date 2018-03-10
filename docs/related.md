# Related projects

Image augmentation techniques have been successfully applied in the literature; and most of those techniques can be simply implemented using image processing and computer vision libraries, such as [OpenCV](https://opencv.org/) or [SciPy](https://www.scipy.org/), or even without the help of third-party libraries. However, this means reinventing the wheel; and, hence, several libraries and frameworks have appear over the years to deal with image augmentation for object classification. 

Some of those libraries, like [Data-Augmentation](https://github.com/outlace/Data-Augmentation) or [CodeBox](https://codebox.net/pages/image-augmentation-with-python), provide a few basic augmentation techniques such as  rotation, shifting and flipping. There are other libraries with more advanced features. [Augmentor](http://arxiv.org/abs/1708.04680) uses a stochastic, pipeline-based approach for image augmentation featuring the most common techniques applied in the literature. [Imgaug](https://github.com/aleju/imgaug) provides more than 40 augmentation techniques that can be applied to both images and keypoints on images. CLoDSA includes almost all the augmentation techniques implemented in those libraries (some of the Imgaug techniques are not available in CLoDSA) and also others that have been employed in the literature but were not included in those libraries. A comparison of the techniques featured in each library is available at the end of this page. 

All the aforementioned libraries are independent from any particular machine learning framework, but there are also image augmentation libraries integrated in several deep learning frameworks. The advantage of those libraries is that, in addition to save the images to disk, they can directly fed the augmented images to a training model without storing them. 

The main deep learning frameworks provide data augmentation techniques. [Keras](https://keras.io/preprocessing/image/) can generate batches of image data with real-time data augmentation using 10 different augmentation techniques. There is a branch of [Caffe](https://github.com/ShaharKatz/Caffe-Data-Augmentation) that features image augmentation using a configurable stochastic combination of 7 data augmentation techniques. Tensorflow has [TFLearn's DataAugmentation](https://github.com/tflearn/tflearn), MXNet has [Augmenter classes](http://arxiv.org/abs/1512.01274), DeepLearning4J has [ImageTransform classes](http://deeplearning4j.org), and Pytorch has [transforms](http://pytorch.org/). The list of techniques available in these libraries is available at the end of this page. 

In addition to these integrated libraries for image augmentation, the [Augmentor](http://arxiv.org/abs/1708.04680) library, that can be used independently of the machine learning framework, can be integrated into Keras and Pytorch. This is the same approach followed in CLoDSA where we have developed a library that is independent of any framework but that can be integrated into them -- currently such an integration is only available for the Keras framework. 

All these libraries, both the ones that are independent of any framework and those that are integrated into a deep learning library, are focused on the problem of object classification, and none of them can be directly applied to the problems of localization, detection or semantic segmentation. The closer library is [Imgaug](https://github.com/aleju/imgaug) that can apply augmentation techniques to keypoints on images. Hence, we can consider CLoDSA as the first image augmentation framework for classification, localization, detection and semantic segmentation. 

## Techniques available in the different libraries

||CLoDSA|Keras|Caffe-Data-Augmentation|TFLearn|Augmenter|Imgaug|Augmentor|Keras-transform|Codebox|Data-augmentation|ImageTransform|transforms pytorch|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|Average blur|✓|||||✓|||||✓||
|Bilateral blur|✓|||||✓|||||||
|Brightness noising|||✓||✓||||||||
|Channel shift|✓|✓||||||✓|||||
|Color noising|✓||✓||✓|||||✓|||
|Color conversion|✓||||||||||✓|✓|
|Contrast noising|||||✓|✓|||||||
|Crop|✓|||✓|✓|✓|✓||||✓|✓|
|Dropout|✓|||||✓|✓||||||
|Elastic|✓||✓|||✓|✓||||||
|Equalize histogram|✓||||||||||✓||
|Gaussian Blur|✓|||||✓|||||||
|Gaussian noise|✓|||||✓|||||||
|Horizontal flip|✓|✓|✓|✓|✓|✓|✓|✓|✓|✓|✓|✓|
|Hue jitter|✓||||✓|✓|||||||
|Invert|✓|||||✓|||||||
|Lighting|✓||||✓||||||||
|Median blur|✓|||||✓|||||||
|Normalization|✓|✓|||✓|✓|||||||
|Rescale|✓|✓|✓|||✓|||||✓|✓|
|Rotation|✓|✓||✓||✓|✓|✓|✓|✓|✓||
|Salt and pepper|✓|||||✓|||✓||||
|Saturation jitter|✓||||✓|✓|||||||
|Sharpen|✓|||||✓|||||||
|Shear|✓|✓||||✓|✓|✓|||||
|Skew|✓||||||✓||||||
|Small Blurring|✓||✓|✓|||||✓||||
|Translation|✓|✓|✓|||✓||✓|✓|✓|||
|Vertical flip|✓|✓|✓|✓||✓|✓|✓|✓|✓|✓|✓|
|ZCA whitening||✓|||||||||||
|Zoom||✓|||✓|||✓|||||
