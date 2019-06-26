# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:36:24 2019

@author: ROJA MOGILI
"""

import cv2

img=cv2.imread("C:\\Users\\ROJA MOGILI\\Downloads\\standard_test_images\\standard_test_images\\1.tiff")
#cv2.imshow("img",img)
gray_color=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

eye_cas=cv2.CascadeClassifier('haarcascade_eye.xml')
face_cas=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face=face_cas.detectMultiScale(gray_color,2,8)


for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    roi_gray=gray_color[y:y+h,x:x+w]
    roi_color=img[y:y+h,x:x+w]
    eyes=eye_cas.detectMultiScale(roi_gray)
    for (x,y,w,h) in eyes:
        cv2.rectangle(roi_color,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow('img',img)
    
cv2.waitKey(0)
cv2.destroyAllWindows()