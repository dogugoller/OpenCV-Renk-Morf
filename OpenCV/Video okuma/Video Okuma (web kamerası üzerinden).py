import cv2
import numpy as np

# Web kamerası üzerinden oynatma
yakala = cv2.VideoCapture(0) # 0 yazıldığında webcamı algılar.,


while (True):
    deger, kare = yakala.read()
    cv2.imshow("Eas",kare)

    if  cv2.waitKey(1) & 0xFF == ord("d"):
        break

yakala.release()
cv2.destroyAllWindows()




