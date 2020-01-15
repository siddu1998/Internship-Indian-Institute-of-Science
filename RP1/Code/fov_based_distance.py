#python imports
import cv2
import math

#Custom modules
import helper



img=cv2.imread('00001.jpg')
img_height,img_width,_=img.shape


cx=951.1
cy=551.1

fx=893.390
fy=898.32


radian_theta=math.atan(cx/fy)

#1 radian is 57.296 degrees
radian_to_degree=57.296  

degree_theta=radian_theta*57.296
fov=2*degree_theta

print("Field of view in degrees:",fov)