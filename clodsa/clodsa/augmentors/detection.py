import cv2
import numpy as np
import imutils

# A box is a tuple (category,(x,y,w,h)) where category is the category of the
# object, x and y represent the top-left corner, w is the width and h is the height.
def detectBox(image,box,technique):
    mask = np.zeros(image.shape[:2], dtype="uint8")
    (category,(x,y,w,h)) = box
    cv2.rectangle(mask, (x, y), (x+w, y+h), 255, -1)
    newmask = technique.apply(*[mask])

    cnts = cv2.findContours(newmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    if(len(cnts)==0):
        return None
    return (technique.transform_label(*[category]),cv2.boundingRect(cnts[0]))


# Boxes is a list of boxes with the following format: (category,(x,y,w,h))
def detectBoxes(image,boxes,function):
    return [detectBox(image,box,function) for box in boxes if detectBox(image,box,function) is not None]








