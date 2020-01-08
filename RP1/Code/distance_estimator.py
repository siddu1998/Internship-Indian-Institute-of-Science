from helper import *
import pandas as pd


#image at height
image1=get_image('../Data/AGZ_subset/MAV Images/00350.jpg')

#image at lower height
image2=get_image('../Data/AGZ_subset/MAV Images/00001.jpg')


print('[INFO] Height and Width of Image:',get_width(image1),get_height(image1))


#show images
show_image(image1)
show_image(image2)
