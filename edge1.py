import cv2 as cv
import numpy as np

#camera = cv.VideoCapture('C:/Users/Admin/Desktop/slab/New/VID_20241111_112614.mp4')
rtsp = "rtsp://192.168.0.2:554/PSIA/Streaming/channels/0"
camera = cv.VideoCapture(rtsp)
#camera = cv.VideoCapture(0)

fg_mask = cv.createBackgroundSubtractorMOG2()

while True:
    #نمایش تصویر دوربین
    ret, frame = camera.read()
    #تغییر سایز عکس
    img = cv.resize(frame,(0,0),fx=0.4,fy=0.4)
    cv.imshow('Camera',img)
    #خروج از برنامه
    if cv.waitKey(5) == ord('x'):
        break

    fg_mask_result = fg_mask.apply(img)
    cv.imshow('Remove BG', fg_mask_result)


    #اجرای تابع لاپلاسیون
    # laplacian = cv.Laplacian(frame, cv.CV_8U)
    laplacian = cv.Laplacian(img, cv.CV_64F)
    laplacian = np.uint8(laplacian)
    cv.imshow('Laplacian', laplacian)

    #اجرای تابع تشخیص لبه
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)    
    edge = cv.Canny(gray, 50, 100)
    cv.imshow('Edge', edge)

    #اجرای تابع تشخیص لبه
    #gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)    
    edge = cv.Canny(fg_mask_result, 50, 100)
    cv.imshow('Edge 2', fg_mask_result)    

camera.release()
cv.destroyAllWindows()