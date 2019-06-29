import numpy as np
import cv2
def human():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    img=cv2.imread("human_faces\\16.jpg")

    #img=cv2.resize(img,(600,450))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]    
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


    cat_cascade=cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
    cat_extended=cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')

    SF=1.3
    N=2
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cats=cat_cascade.detectMultiScale(gray,scaleFactor=SF,minNeighbors=N)
    cat_ext=cat_extended.detectMultiScale(gray,scaleFactor=SF,minNeighbors=N)

    for (x,y,w,h) in cats:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    for (x,y,w,h) in cat_ext:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("img",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
human()
