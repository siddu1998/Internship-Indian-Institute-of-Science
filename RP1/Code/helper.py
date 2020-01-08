import matplotlib.pyplot as plt
import cv2
import pandas as pd

from scipy.spatial import distance


"""
input: take gps cordinates from Drone 

"""
def show_tranjectory(onboard_gps_x,on_board_gps_y,on_board_alt):
    pass

def read_npy(file_path):
    pass


#Get Distance between frames using onboard GPS Camera
def get_distance_between_frames(coordinate_1,coordinate_2):
    return distance.eucledian(coordinate_1,coordinate_2)






#Get image
def get_image(file_path):
    img=cv2.imread(file_path)
    return img

#Display Image
def show_image(image):
    cv2.imshow('{}'.format(image[:-6]), image)
    cv2.waitKey(0)

#Get width of image
def get_width(image):
    w,_,_=image.shape
    return w

#Get height of image
def get_height(image):
    _,h,_=image.shape
    return h



