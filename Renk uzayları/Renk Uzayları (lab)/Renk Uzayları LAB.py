import cv2

image = cv2.imread("interstellar.jpg")

lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)

cv2.imshow("OrijinaL Görsel",image)
cv2.imshow("Lab Görsel", lab_image)

cv2.waitKey(0)
cv2.destroyAllWindows()