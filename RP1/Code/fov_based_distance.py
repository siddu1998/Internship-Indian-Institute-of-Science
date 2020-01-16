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


radian_theta_x=math.atan(cx/fx)
radian_theta_y=math.atan(cy/fy)


#1 radian is 57.296 degrees
radian_to_degree=57.296  

degree_theta_along_x=radian_theta_x*57.296
degree_theta_along_y=radian_theta_y*57.296


fov_x=2*degree_theta_along_x
fov_y=2*degree_theta_along_y

print("Field of view in degrees along x-axix:",fov_x)
print("Field of view in degrees along y-axix:",fov_y)

