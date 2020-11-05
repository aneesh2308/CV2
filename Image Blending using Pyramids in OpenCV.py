import cv2
import numpy as np
apple = cv2.imread('img-1.jpg',-1)
orange = cv2.imread('img-2.jpg',-1)
apple = cv2.resize(apple,(512,512))
orange = cv2.resize(orange,(512,512))
# print(apple.shape)
# print(orange.shape)
apple_orange = np.hstack((apple[:,:256],orange[:,256:]))
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy=cv2.pyrUp(apple_copy)
    gp_apple.append(apple_copy)

orange_copy = orange.copy()
gp_orange = [orange_copy] 

for i in range(6):
    orange_copy=cv2.pyrUp(orange_copy)
    gp_orange.append(orange_copy)

apple_copy = apple.copy()
lp_apple = [apple_copy]

for i in range(6):
    gaussian_expanded = cv2.pyrUp(gp_apple[i]) 
    laplacian = cv2.subtract(gp_apple[i-1],gaussian_extended)
    lp_orange.append(laplacian)

orange_copy = orange.copy()
lp_orange = [orange_copy]

for i in range(6):
    gaussian_expanded = cv2.pyrUp(gp_orange[i]) 
    laplacian = cv2.subtract(gp_orange[i-1],gaussian_extended)
    lp_orange.append(laplacian)

apple_orange_pyramid = []
n = 0
for apple_lap,orange_lap in zip(lp_apple,lp_orange):
    n += 1
    cols,rows,ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:,0:int(cols/2)],orange_lap[:,:int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i],apple_orange_reconstruct)


cv2.imshow("apple",apple)
cv2.imshow("orange",orange)
cv2.imshow("apple_orange",apple_orange)
cv2.imshow("apple_orange_reconstruct",apple_orange_reconstruct)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()