import numpy as np
import cv2

car_cascade = cv2.CascadeClassifier('car-cascade.xml')
bike_cascade = cv2.CascadeClassifier('bike-cascade.xml')

for num in range(5,25) :
    
    img = cv2.imread('Random/pos'+str(num)+'.bmp')
    img = img[80:444,0:535]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bike = bike_cascade.detectMultiScale(gray,1.04,100,minSize=(100,100), maxSize=(170,170))
    car = car_cascade.detectMultiScale(gray,1.07,50,minSize=(100,100), maxSize=(170,170))

    for (x,y,w,h) in bike:
        print (num)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('img',img)
        cv2.waitKey(0)

    for (x,y,w,h) in car:
        print (num)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('img',img)
        cv2.waitKey(0)


        
cv2.waitKey(0)
cv2.destroyAllWindows()

