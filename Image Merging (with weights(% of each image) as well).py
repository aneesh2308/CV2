import cv2
img = cv2.imread('img-1.jpg',-1)
img1 = cv2.imread('img-2.jpg',-1)
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340,330:390]
img[280:340,330:390] = ball

img = cv2.resize(img,(512,512))
img1 = cv2.resize(img1,(512,512))

#dst = cv2.add(img,img1);
dst = cv2.addWeighted(img,.5,img1,.5,0);

cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
