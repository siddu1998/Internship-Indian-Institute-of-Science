#python imports
from mpl_toolkits.mplot3d import Axes3D
import cv2
import math
#Custom modules
from helper import *
import matplotlib.pyplot as plt


camera_cordinates_path=input('Please enter camera cordinates ')
camera_cordinates_df= load_df(camera_cordinates_path)
camera_cordinates_df['lat'],camera_cordinates_df['lon']=utm_to_gps(camera_cordinates_df['x_gps'],camera_cordinates_df['y_gps'],32,'N')

fig=plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.scatter(camera_cordinates_df['lat'], camera_cordinates_df['lon'],camera_cordinates_df['z_gps'],s=3 ,color='r')
ax.set_title('Drone Path')
plt.show()





