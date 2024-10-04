import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("sky.jpg",0)
plt.imshow(img,cmap="gray", interpolation="bicubic") # bicubic resmi yeniden boyutlandırmaya yarar.
plt.xticks([]) # x,y değerlerini yok eder
plt.yticks([]) # x,y değerlerini yok eder
plt.show()

