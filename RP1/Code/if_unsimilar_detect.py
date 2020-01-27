"""
Simillarity Measurment between images
--------------------------------------
Author: Sai Siddartha Maram
email : msaisiddartha1@gmail.com | smaram_be16@thapar.edu
--------------------------------------
Objectives:
1. Develop an evaluation metric to check how simillar two images are
2. Based on the level of similarity, choose to propogate the image through the neural network
"""
from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
import numpy as np

import cv2
from matplotlib import pyplot as plt
import helper


import imutils


from skimage.measure import compare_ssim
from PIL import Image
import imagehash
import time

def histogram_matching(path_image1, path_image2):
    img1 = cv2.imread(path_image1)
    img2 = cv2.imread(path_image2)
    plt.hist(img1.ravel(),256,[0,256])
    plt.show()
    plt.hist(img2.ravel(),256,[0,256])
    plt.show()

    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    start_time=time.time()

    hist1 = cv2.calcHist(img1, [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist1 = cv2.normalize(hist1, hist1).flatten()

    hist2 = cv2.calcHist(img2, [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist2 = cv2.normalize(hist2, hist2).flatten()

    #a = cv2.compareHist(hist1, hist2, cv2.HISTCMP_INTERSECT) ----> WASTE!
    #a = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL) ----->Waste!
    a = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR)
    print('time histogram mapping',time.time()-start_time)

    print(a)


def image_hashing(path_image1,path_image2):
    start_time=time.time()

    hash0 = imagehash.average_hash(Image.open(path_image1)) 
    hash1 = imagehash.average_hash(Image.open(path_image2)) 
    print('time image hashing',time.time()-start_time)
    print('hash0: ',hash0)
    print('hash1: ',hash1)


    return hash0-hash1




def image_subtraction(path_image1,path_image2):
    img1 = cv2.imread(path_image1)
    img2 = cv2.imread(path_image2)

    img1=cv2.resize(img1,(800,600))
    img2=cv2.resize(img2,(800,600))

    start_time=time.time()
    grayA = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))
    

    thresh = cv2.threshold(diff, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1] 
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    if len(cnts)>0:
        #print(len(cnts))
        biggest_cnt=max(cnts, key = cv2.contourArea)
        print("Difference in scene")
        print('biggest_difference',cv2.contourArea(biggest_cnt))
    else:
        print('No Difference!')
    
    print(time.time()-start_time)
    
    """
    Uncomment below to visualize
    """

    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        
        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    cv2.imshow("Scene 1", img1)
    cv2.imshow("Scene 2", img2)
    #cv2.imwrite('save.jpg',diff)
    cv2.imshow("Diff", diff)
    cv2.waitKey(0)
    
 


image_path_1='2.jpg'
image_path_2='4360.jpg'

print(histogram_matching(image_path_1,image_path_2))
print(image_hashing(image_path_2,image_path_2))

image_subtraction(image_path_1,image_path_2)
