import cv2 as cv
import numpy as np

#camera = cv.VideoCapture(0)

img = cv.imread('img.jpg')
#تغییر سایز عکس
img = cv.resize(img,(0,0),fx=0.3,fy=0.3)
#نمایش به صورت سیاه سفید
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('GRAY',img_gray)
cv.waitKey(0)