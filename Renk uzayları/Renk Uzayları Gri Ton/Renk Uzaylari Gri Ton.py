import cv2


image = cv2.imread("way.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Renkli",image)
cv2.imshow("Siyah Beyaz",gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()