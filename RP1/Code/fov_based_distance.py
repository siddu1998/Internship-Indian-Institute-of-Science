#python imports
from mpl_toolkits.mplot3d import Axes3D
import cv2
import math
#Custom modules
from helper import *
import matplotlib.pyplot as plt


camera_cordinates_path=input('Please enter camera cordinates ')
camera_cordinates_df= load_df(camera_cordinates_path)

#this is from gps
camera_cordinates_df['lat'],camera_cordinates_df['lon']=utm_to_gps(camera_cordinates_df['x_gps'],camera_cordinates_df['y_gps'],32,'N')

#this is from gt_gps
camera_cordinates_df['lat_gt'],camera_cordinates_df['lon_gt']=utm_to_gps(camera_cordinates_df['x_gt'],camera_cordinates_df['y_gt'],32,'N')


fig=plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.scatter(camera_cordinates_df['lat'], camera_cordinates_df['lon'],camera_cordinates_df['z_gps'],s=3 ,color='r')
ax.scatter(camera_cordinates_df['lat_gt'], camera_cordinates_df['lon_gt'],camera_cordinates_df['z_gt'],s=3 ,color='b')

ax.set_title('Drone Path')
plt.show()





