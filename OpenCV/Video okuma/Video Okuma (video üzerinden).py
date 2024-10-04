import cv2
import numpy as np


#Video üzerinden oynatma


yakala = cv2.VideoCapture("reels.mp4")

while (yakala.isOpened()):
    deger, kare = yakala.read()
    gray = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY) # videoyu griye döndürür.
    cv2.imshow("Visuich",gray)

    if cv2.waitKey(1) & 0xff == ord("d"):
        break

yakala.release()
cv2.destroyAllWindows()

