import cv2
import numpy as np

image = cv2.imread("image.jpg")

kernel = np.ones((5,5), np.uint8)
top_hat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("Orijinal", image)
cv2.imshow("Top Hat", top_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()