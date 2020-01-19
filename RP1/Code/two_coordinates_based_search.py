from scipy.spatial.ckdtree import cKDTree
import pandas as pd 
import navpy
import math
import numpy as np
import os
import matplotlib.pyplot as plt

from helper import *


LAT_REF = 33.79588248
LON_REF = -84.24924553
ALT_REF = 200

print('[INFO] Enter Onboard GPS Data Sheet')
drone_cordinates_path=input("enter file path")

print('[INFO] Loading Data Sheet')
drone_cordinates_df= load_df(drone_cordinates_path)
drone_cordinates_in_cartesian_df=DataFrameLLA2Cartesian(drone_cordinates_df)


print("[INFO] Building a tree of all DRONE coordinates")

X = drone_cordinates_in_cartesian_df[["x_cart", "y_cart"]].values
print(X)
kdtree = cKDTree(X)
print("[INFO] Finished buidling the tree")


print('[USER] Please enter your query points')
query_point_lat=float(input())
query_point_lon=float(input())
query_point_alt=int(input())


print('[INFO] Converting query points to cartesian')
x_query, y_query,_ = navpy.lla2ned(query_point_lat,query_point_lon,query_point_alt,
									LAT_REF, LON_REF, ALT_REF,
									latlon_unit='deg', alt_unit='m', model='wgs84')
	

print("[INFO] Starting Spherical Search of 20meters")
query_point = np.array([x_query,y_query]).reshape(1,-1)
print(query_point)
query_return = kdtree.query_ball_point(query_point,r=30)
#the query will return indices from the onboard gps sheets which are nearly
# at a distance of 20 meters from the query point
print(len(query_return))