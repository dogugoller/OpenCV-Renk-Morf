import cv2
import numpy as np

originalimage = cv2.imread("snowfall.jpeg") # Orijinal
imgedit1 = cv2.cvtColor(originalimage, cv2.COLOR_BGR2HSV) # BGR'den HSV'ye
imgedit2 = cv2.cvtColor(originalimage, cv2.COLOR_BGR2RGB) # BGR'den RGB'ye


cv2.imshow("Original",originalimage)
cv2.imshow("HSV",imgedit1)
cv2.imshow("RGB",imgedit2)



cv2.waitKey(0)
cv2.destroyAllWindows()