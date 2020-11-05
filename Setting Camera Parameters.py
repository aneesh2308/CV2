import cv2
cap = cv2.VideoCapture(0);
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap.set(3,1280)
cap.set(4,720)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
# cv2.CAP_PROP_FRAME_WIDTH = 3
# cv2.CAP_PROP_FRAME_HEIGHT = 4 
print(cap.get(4))
print(cap.get(3))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        k = cv2.waitKey(1) & 0xFF
        if k== ord('q'):
            break
    else:
        break    

cap.release()
cv2.destroyAllWindows()