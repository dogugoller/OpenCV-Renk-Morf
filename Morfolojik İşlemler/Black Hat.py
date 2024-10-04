import cv2
import numpy as np

image = cv2.imread("image.jpg")

kernel = np.ones((5,5), np.uint8)
black_hat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Orijinal", image)
cv2.imshow("Black Hat", black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()