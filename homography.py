# Ref: https://learnopencv.com/homography-examples-using-opencv-python-c/#download
import cv2
import numpy as np
 
# Read source image.
im_src = cv2.imread('images/book1.jpg')
# Four corners of the book in source image
pts_src = np.array([[528, 241], [734, 607], [228, 868], [46, 482]])

# Read destination image.
im_dst = cv2.imread('images/book2.jpg')
# Four corners of the book in destination image.
pts_dst = np.array([[120, 402], [549, 415], [538, 970],[110, 965]])

# Calculate Homography
h, status = cv2.findHomography(pts_src, pts_dst)
 
# Warp source image to destination based on homography
im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))
 
# Save and display wrap result
cv2.imwrite('images/warp_result.jpg', im_out)
cv2.imshow("Warped Source Image", im_out)
 
cv2.waitKey(0)