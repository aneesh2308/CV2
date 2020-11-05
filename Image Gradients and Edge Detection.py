import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img-2.jpg',cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))
soblex = cv2.Sobel(img,cv2.CV_64F,1,0)
sobley = cv2.Sobel(img,cv2.CV_64F,0,1)

soblex = np.uint8(np.absolute(soblex))
sobley = np.uint8(np.absolute(sobley))
sobleCombined=cv2.bitwise_or(soblex,sobley)
titles = ['image','Laplacian','soblex','sobley','sobleCombined']
images = [img,lap,soblex,sobley,sobleCombined]

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()   
