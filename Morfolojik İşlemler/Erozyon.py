import cv2
import numpy as np

image = cv2.imread("image.jpg")

kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(image, kernel, iterations=1)
cv2.imshow("Orijinal", image)
cv2.imshow("Erozyon", erosion)

cv2.waitKey()
cv2.destroyAllWindows()