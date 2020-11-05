import cv2
import numpy as np
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ',' + str(y)
        cv2.putText(img,strXY,(x,y),font,.5,(255,255,0),2)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strRBG = str(blue) + ',' + str(green) + ',' + str(green)
        cv2.putText(img,strRBG,(x,y),font,.5,(0,255,255),2)
        cv2.imshow('image',img)

img = cv2.imread('img-1.jpg',-1)
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)
cv2.waitKey()
cv2.destroyAllWindows()