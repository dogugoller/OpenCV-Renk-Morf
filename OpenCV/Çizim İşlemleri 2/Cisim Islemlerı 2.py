import cv2
import numpy as np

img = cv2.imread("feel.jpeg",0)
img2 = cv2.rectangle(img,(10,10),(600,800),(0,255,0),10) # son parametreye -" girilirse içi boyalı gelir
cv2.imshow("Feel",img)
img3 = cv2.circle(img2,(500,300),80,(0,0,255),10) # son parametreye -" girilirse içi boyalı gelir
cv2.imshow("Feel", img3)

font = cv2.FONT_HERSHEY_DUPLEX
img4 = cv2.putText(img3,"Greek Mythology",(25,400),font,2,(255,255,255),5,cv2.LINE_AA) # Resmin üzerine yazı yazdırma
cv2.imshow("Feel",img4)

cv2.waitKey()
cv2.destroyAllWindows()