import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('img-2.jpg',-1)
_,th1 = cv.threshold(img,50,255,cv.THRESH_BINARY) # After Thresh it divides into black and white
_,th2 = cv.threshold(img,250,255,cv.THRESH_BINARY_INV) # Inverse of above
_,th3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)  # After Thresh it becomes constant color
_,th4 = cv.threshold(img,200,255,cv.THRESH_TOZERO)  # After Thresh it becomes constant color and before that only black
_,th5 = cv.threshold(img,200,255,cv.THRESH_TOZERO_INV) # Inverse of above
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZEROES','TOZERO_INV']
images = [img,th1,th2,th3,th4,th5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
# cv.imshow('image',img)
# cv.imshow('th1',th1)
# cv.imshow('th2',th2)
# cv.imshow('th3',th3)
# cv.imshow('th4',th4)
# cv.imshow('th5',th5)
plt.show()  
