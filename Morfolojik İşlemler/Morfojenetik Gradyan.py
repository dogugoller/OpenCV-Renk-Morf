import cv2
import numpy as np

image = cv2.imread("image.jpg")

kernel = np.ones((5,5), np.uint8)
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

cv2.imshow("Orijinal", image)
cv2.imshow("Gradyan", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()