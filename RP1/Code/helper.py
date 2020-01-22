import cv2
import pandas as pd
import utm
from scipy.spatial import distance
import navpy
import os

#custom util imports
import constants

#load data frame from csv
def load_df(path):
    df=pd.read_csv(path)
    return df

#get gps cordinates from utm
def utm_to_gps(easting,northing,zone_number,zone_letter):
    return utm.to_latlon(easting,northing, zone_number,zone_letter)

#get Distance between frames using onboard GPS Camera
def get_distance_between_frames(coordinate_1,coordinate_2):
    return distance.eucledian(coordinate_1,coordinate_2)

#get image
def get_image(file_path):
    img=cv2.imread(file_path)
    return img

#display Image
def show_image(image):
    cv2.imshow('{}'.format(image[:-6]), image)
    cv2.waitKey(0)

#get width of image
def get_width(image):
    w,_,_=image.shape
    return w

#Get height of image
def get_height(image):
    _,h,_=image.shape
    return h
#calculate field of views horizontal 
def get_fov_horizantal(cx,fx):
    radian_theta_x=math.atan(cx/fx)
    degree_theta_along_x=radian_theta_x*57.296
    fov_x=2*degree_theta_along_x
    return fov_x
#calculate field of views horizontal 
def get_fov_horizantal(cy,fy):
    radian_theta_y=math.atan(cy/fy)
    degree_theta_along_y=radian_theta_y*57.296
    fov_y=2*degree_theta_along_y
    return fov_y



def DataFrameLLA2Cartesian(df):
    LAT_REF = constants.LAT_REF
    LON_REF = constants.LON_REF
    ALT_REF = constants.ALT_REF
    lon = df["lon"].values
    lat = df["lat"].values
    alt = df["alt"].values
    cartesian = navpy.lla2ned(lat, lon, alt,LAT_REF, LON_REF, ALT_REF,latlon_unit='deg', alt_unit='m', model='wgs84')
    df['x_cart'] = cartesian[:, 0]
    df['y_cart'] = cartesian[:, 1]
    df['z_cart'] = cartesian[:, 2]
    return df

def batch_detection(folder):   

    tfnet_model = TFNet(constants.options)
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            print(filename,tfnet_model.return_predict(img))
