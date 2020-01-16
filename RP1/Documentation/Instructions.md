### Details and Instructions

The current research project to find the amount of area captured by a drone, through monocular images. The current dataset being used is the dataset generated by Universty of Zurich, using the MAV flown across the city of Zurich.

Images have been captured through a GoPro Hero4 camera. Though not mentioned specifically, exploring the specifications of the GoPro Hero4, we can consider the following mentioned on GoPro's official web store. The images captured are 1920 pixels wide and 1080 pixels in height. This when simplified leads to a ratio 16x9. A GoPro typically shoots in three modes of FOV and focal length. We do the following to identify the correct Focal Length by calculating the FOV. 

From the concept of photometry of a pinhole camera, we know that the image plane lies at a distance of focal_length (pixels) and the image center lies at cx(obtained form the camera matrix) using that we find the FOV along x-axis (horizontal) to be nearly 93.5 and simillary along the y-axis we found it to be 63.09 .

These values are subjected to little errors from the industry specified GoPro Specifications. We can easily correspond to the original values mentioned on their website which are as follows: 

focal length in mm = 21.9 mm
FOV along x-axis   = 94.4 mm
FOV along y-axis   = 55   mm
FOV along z-axis   = 107.1mm
