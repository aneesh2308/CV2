import cv2
from matplotlib import pyplot as plt
img = cv2.imread('img-1.jpg',-1)
cv2.imshow('img',img)

plt.imshow(img)
plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()