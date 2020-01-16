import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('00001.jpg')
img_height,img_width,_=img.shape


IMAGE_H = img_height
IMAGE_W = img_width

src = np.float32([[0, IMAGE_H], [2000, IMAGE_H], [0, 0], [IMAGE_W, 0]])
dst = np.float32([[500, IMAGE_H], [700, IMAGE_H], [0, 0], [IMAGE_W, 0]])
M = cv2.getPerspectiveTransform(src, dst) # The transformation matrix
Minv = cv2.getPerspectiveTransform(dst, src) # Inverse transformation

img = img[450:(450+IMAGE_H), 0:IMAGE_W] # Apply np slicing for ROI crop
warped_img = cv2.warpPerspective(img, M, (IMAGE_W, IMAGE_H)) # Image warping
plt.imshow(cv2.cvtColor(warped_img, cv2.COLOR_BGR2RGB)) # Show results
plt.show()