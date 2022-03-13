import numpy as np
import cv2 as cv

img = cv.imread('flower.jpg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img, equ))
cv.imwrite('NEWFlower.jpg',res)

