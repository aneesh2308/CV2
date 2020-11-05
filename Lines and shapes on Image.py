import cv2 
img = cv2.imread('img-1.jpg',-1)

img = cv2.line(img,(0,0),(255,255),(255,0,0),thickness=10)
img = cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),thickness=10)
img = cv2.rectangle(img,(384,0),(510,128),(255,0,0),-1)
img = cv2.circle(img,(447,63),63,(255,255,255),-1)
font = cv2.FONT_HERSHEY_SIMPLEX 
img = cv2.putText(img,"How Are You",(10,500),font,4,(0,255,255),10,cv2.LINE_AA)

cv2.imshow('img',img)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()