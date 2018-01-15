import cv2
import numpy as np
import math


def generateMosaic (images):

    imagemosaic = []
    maxheight = max([i.shape[0] for i in images])
    maxwidth = max([i.shape[1] for i in images])

    rows = int(math.ceil(len(images)/4.0))
    columns = 4
    mosaicImage = np.zeros((rows*maxheight,columns*maxwidth,3),dtype="uint8")
    for (i,image) in enumerate(images):
        mosaicImage[int(i/4)*maxheight:(int(i/4)*maxheight)+image.shape[0],
                    int(i%4)*maxwidth:(int(i%4)*maxwidth)+image.shape[1]] = image
    return mosaicImage
















