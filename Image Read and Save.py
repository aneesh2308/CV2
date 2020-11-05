import cv2
img = cv2.imread('img-1.jpg',-1)
cv2.imshow('img',img)
k = cv2.waitKey(0) & 0xFF

if k==27 :
    cv2.destroyAllWindows()
elif k== ord('s'):
    cv2.imwrite('img-1_copy.jpg',img)
    cv2.destroyAllWindows()