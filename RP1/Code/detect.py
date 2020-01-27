"""
Original Support:
OpenCV Documentations

Modifications:
1. Loading Model from constants.py
2. Making it modular, so this function can be called in other cases
3. Knocking out time consuming operations

-Sai Siddartha Maram

"""

import numpy as np
import argparse
import time
import cv2
import os

# MY CUSTOM IMPORTS
import constants

options = constants.options
np.random.seed(42)
LABELS = open(options['labelsPath']).read().strip().split("\n")
color = (255, 0, 255)


"""
We will use opencv's dnn module to perform object detection,
I have read various blogs, which state that running YOLO on opencv  
is faster then the traditional way of predicting objects on darknet
Reference :

https://www.learnopencv.com/deep-learning-based-object-detection-using-yolov3-with-opencv-python-c/
The above reference has a table indicating the performance metrics

"""


"""
Load the darknet model using readNetFromDarkent(), feel free to try other DL models
"""
net = cv2.dnn.readNetFromDarknet(options['model'], options['load'])

"""
Test Image
"""
image = cv2.imread('check_output.jpg')
(H, W) = image.shape[:2]


"""
 In CV2.dnn you load a model and then forward propgate the image for prediction, 
 the forwad function expects you give the layer till which you want the image to be 
 propgated, in our case since we want the final result, we want the image to be 
 propgated till the last layer. 


 The .getLayerNames() gives the list of all layers. From here to identify the last layer,
 we need to get last unconnected layer, the unconnected layers can be found by
 .getUnconnectedOutLayers().
"""
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]


"""
blob : the cv.dnn does not take a raw image, instead takes a blob,
A blob is an image which is modified and smoothed as per the network requirments

For Ex: YOLO takes in an image only of the size 416 x 416 (single channel) hence we reduce each color
from [0-255] to [0-1] and image size (416,416)
"""
blob = cv2.dnn.blobFromImage(
    image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
net.setInput(blob)
start = time.time()
layerOutputs = net.forward(ln)
end = time.time()

# show timing information on YOLO
print("[INFO] YOLO took {:.6f} seconds".format(end - start))

boxes = []
confidences = []
classIDs = []
for output in layerOutputs:
    for detection in output:
        scores = detection[5:]
        classID = np.argmax(scores)
        confidence = scores[classID]
        if confidence > options['confidence']:
            box = detection[0:4] * np.array([W, H, W, H])
            (centerX, centerY, width, height) = box.astype("int")
            x = int(centerX - (width / 2))
            y = int(centerY - (height / 2))
            boxes.append([x, y, int(width), int(height)])
            confidences.append(float(confidence))
            classIDs.append(classID)

idxs = cv2.dnn.NMSBoxes(
    boxes, confidences, options['confidence'], options['threshold'])

if len(idxs) > 0:
    for i in idxs.flatten():
        # extract the bounding box coordinates
        (x, y) = (boxes[i][0], boxes[i][1])
        (w, h) = (boxes[i][2], boxes[i][3])
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 3)
        text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
        print(text)
        cv2.putText(image, text, (x, y - 5),cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

image=cv2.resize(image,(600,600))
cv2.imshow("Image", image)
cv2.waitKey(0)
