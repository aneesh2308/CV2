import cv2
import numpy as np
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img,(x,y),3,(255,0,0),1,cv2.LINE_AA)
        mycolorimg = np.zeros((512,512,3),np.uint8)
        mycolorimg [:] = [blue,green,red]
        cv2.imshow('color',mycolorimg)

#img = np.zeros((512,512,3),np.uint8)
img = cv2.imread('img-1.jpg',-1)
cv2.imshow('image',img)
points= []
cv2.setMouseCallback('image',click_event)
cv2.waitKey()
cv2.destroyAllWindows()