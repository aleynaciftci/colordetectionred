import cv2 as cv
import numpy as np

 
cap = cv.VideoCapture(0) #connect to the camera

while True:
    ret, frame = cap.read() #read every frame
    frame = cv.flip(frame, 1) #mirror the camera

    hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV) #convert bgr to hsv 
    lowerlimit=np.array([141,155,84],np.uint8) 
    upperlimit=np.array([179,255,255],np.uint8) 

    mask = cv.inRange(hsvImage, lowerlimit, upperlimit) 
    cnt = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]  
    
    if len(cnt)>0:
        area = max(cnt, key=cv.contourArea)
        (xg,yg,wg,hg) = cv.boundingRect(area)
        cv.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,255,2), 2)

    cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release
cv.destroyAllWindows