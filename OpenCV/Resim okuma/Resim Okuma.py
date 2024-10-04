import cv2
import numpy as np

#Resim Okuma

image = cv2.imread("technology.png",0) # ("technologypng" 1) yapılırsa resim kendi renginde '0' yapılırsa resim gri tonlamada açılır.
cv2.imshow("Tarsier Teknoloji",image)
cv2.waitKey(0)
cv2.destroyWindow()