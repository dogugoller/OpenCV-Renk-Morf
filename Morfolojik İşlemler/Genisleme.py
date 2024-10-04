import cv2
import numpy as np

image = cv2.imread("image.jpg")

kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(image, kernel, iterations=1)

cv2.imshow("Orijinal", image)
cv2.imshow("Genişleme", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()