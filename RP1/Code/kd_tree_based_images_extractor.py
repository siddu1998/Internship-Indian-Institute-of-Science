from scipy.spatial.ckdtree import cKDTree
import pandas as pd 
import navpy
import math
import numpy as np
import os
import matplotlib.pyplot as plt

from helper import *
import time

LAT_REF = constants.LAT_REF
LON_REF = constants.LON_REF
ALT_REF = constants.ALT_REF

print('[INFO] Enter Onboard GPS Data Sheet')
drone_cordinates_path=input("enter file path: ")

print('[INFO] Loading Data Sheet')
drone_cordinates_df= load_df(drone_cordinates_path)
drone_cordinates_in_cartesian_df=DataFrameLLA2Cartesian(drone_cordinates_df)


print("[INFO] Building a tree of all DRONE coordinates")

X = drone_cordinates_in_cartesian_df[["x_cart", "y_cart", "z_cart"]].values

start_time = time.time()
kdtree = cKDTree(X)
print("[INFO] Finished buidling the tree in {}".format(time.time() - start_time))
flag=0

while flag!=-1:
	print('[USER] Please enter your query points')
	query_point_lat=float(input("Lat: "))
	query_point_lon=float(input("Lon: "))
	query_point_alt=float(input("Alt: "))


	print('[INFO] Converting query points to cartesian')
	x_query, y_query, z_query = navpy.lla2ned(query_point_lat,query_point_lon,query_point_alt,
										LAT_REF, LON_REF, ALT_REF,
										latlon_unit='deg', alt_unit='m', model='wgs84')
		


	query_point = np.array([x_query,y_query,z_query]).reshape(1,-1)
	query_radius=int(input("[INFO] Please enter Query Radius in meteres: "))
	print("[INFO] Starting Spherical Search of {}".format(query_radius))	
	start_time = time.time()
	query_return = kdtree.query_ball_point(query_point,r=query_radius)
	exec_time=(time.time() - start_time)


	print(query_return)
	print('[INFO] Query exection done in {} '.format(exec_time) )
	if len(query_return[0])>1:
		user_option=input('[USER] Do you want to perform object detection on the query results Y/n: ')
		if user_option=='Y' or user_option=='y':
			print('[INFO] Detecting..... using model YOLOv2 on TF2.0')
		else:
			print('[INFO] Not executing detection')

	
	flag=int(input("[USER] Press -1 to STOP or anyother number for next query: "))


