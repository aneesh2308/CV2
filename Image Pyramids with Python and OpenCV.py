import cv2
import numpy as np
img = cv2.imread('img-1.jpg',cv2.IMREAD_GRAYSCALE)
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i),layer)
# lr1 = cv2.pyrDown(img)
# lr2 = cv2.pyrDown(lr1)
# ur1 = cv2.pyrUp(lr1)
layer = gp[5]
cv2.imshow('Upper level Gaussian Pyramid',layer)
lp = [layer]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp[i]) 
    gaussian_extended = cv2.resize(gaussian_extended,(512,512))
    laplacian = cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),gaussian_extended)

# cv2.imshow('pyrDown1 Image',lr1)
# cv2.imshow('pyrDown2 Image',lr2)
# cv2.imshow('pyrUP1 Image',ur1)
cv2.imshow('Original Image',img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()