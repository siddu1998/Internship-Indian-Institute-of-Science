from PIL import Image
import numpy as np
from imageshuffle import imageshuffle
from imageshuffle import imagescramble
import cv2
import random

img = Image.open('2.jpg')
ar = np.asarray(img)

# key = 1234
# s = imageshuffle.Rand( key )
# enc = s.enc( ar )
# dec = s.dec( enc )

# cv2.imshow('enc',enc)
# cv2.imshow('dec',dec)
# cv2.waitKey(0)


# key = 1234
# s = imageshuffle.RandBlock( key, [8,8] )
# enc = s.enc( ar )
# dec = s.dec( enc )

# cv2.imshow('enc',enc)
# cv2.imshow('dec',dec)
# cv2.waitKey(0)


key = 1234
s = imageshuffle.Rand(key)
enc = s.enc( ar )

cv2.imshow('enc',enc)
cv2.imwrite('{}.jpg'.format(key),enc)
cv2.waitKey(0)



s=imageshuffle.RandBlock(key,[12,12])
dec = s.dec( enc )
cv2.imshow('dec',dec)

cv2.waitKey(0)



# key = 5678
# s = imageshuffle.RandBlock( key, [8,8] )
# enc = s.enc( ar )
# dec = s.dec( enc )


