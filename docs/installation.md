# Installation


The library uses Python 2.7 and Java, which must be installed. 

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

Once the packages are available, `clodeseaugmentor` can be installed using the following
command::

    pip install ....

This installs the latest version directly from github. If any error pops up, try adding ``sudo`` in front (i.e. ``sudo pip install ...``).

Alternatively, you can install the latest version which was added to pypi via ``pip install ...``. That version can sometimes be behind the version on github.

To uninstall the library use ``pip uninstall ...``.

