import cv2 as cv
import numpy as np

rtsp = "rtsp://192.168.0.2:554/PSIA/Streaming/channels/0"
camera = cv.VideoCapture(rtsp)

while True:
    ret, frame = camera.read()
    small_frame = cv.resize(frame,(0,0),fx=0.3,fy=0.3)
    cv.imshow('JVC Camera', small_frame)

    #blur = cv.GaussianBlur(small_frame, (5,5), 2, 2, cv.BORDER_DEFAULT)
    blur = cv.GaussianBlur(small_frame, (3,3), 10)
    cv.imshow('JVC Blur', blur)

    edge = cv.Canny(small_frame,100,150)
    cv.imshow('JVC Canny', edge)

    sobel_x = cv.Sobel(small_frame,)

    if cv.waitKey(1) == ord('q'):
        break

camera.release()
cv.destroyAllWindows()