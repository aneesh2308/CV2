import cv2
import numpy as np

img = cv2.imread('img-1.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Number of countours"+"  "+str(len(contours)))
# for i in range(738):
#     print(contours[i])
cv2.drawContours(img,contours,-1,(0,255,0),3)

cv2.imshow('Image',img)
cv2.imshow('Image Gray',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()