import cv2
import numpy as np

#Resim Kaydetme

image = cv2.imread("../Matploblib/sky.jpg", 0) # ("technologypng" 1) yapılırsa resim kendi renginde '0' yapılırsa resim gri tonlamada açılır.
cv2.imshow("Tarsier Teknoloji",image)
"""
cv2.imwrite("Sky gri hali.jpg",image) # Resim yukarıda girilen tonlama değişkenine göre klasöre kaydedilir.
"""

e = cv2.waitKey(0)
if e == 27: # 27 klavyede esc tuşuna denk gelir.
    cv2.destryWindows()
elif e == ord("d"): # 'd' tuşuna basılırsa:
    cv2.imwrite("Sky d tusu.png",image)