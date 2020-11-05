import cv2 as cv
import numpy as np

img = cv.imread('img-2.jpg',-1)
_,th1 = cv.threshold(img,50,255,cv.THRESH_BINARY) # After Thresh it divides into black and white
_,th2 = cv.threshold(img,250,255,cv.THRESH_BINARY_INV) # Inverse of above
_,th3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)  # After Thresh it becomes constant color
_,th4 = cv.threshold(img,200,255,cv.THRESH_TOZERO)  # After Thresh it becomes constant color and before that only black
_,th5 = cv.threshold(img,200,255,cv.THRESH_TOZERO_INV) # Inverse of above
cv.imshow('image',img)
cv.imshow('th1',th1)
cv.imshow('th2',th2)
cv.imshow('th3',th3)
cv.imshow('th4',th4)
cv.imshow('th5',th5)
cv.waitKey(0)
cv.destroyAllWindows()