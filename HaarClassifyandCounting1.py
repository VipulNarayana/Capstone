import cv2
import csv
from time import localtime ,strftime

car_cascade = cv2.CascadeClassifier('car-cascade.xml')
bike_cascade = cv2.CascadeClassifier('bike-cascade.xml')
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
count = 0
flag = 0
vc = cv2.VideoCapture('output9.mp4')
with open('VehicleCount.csv','w') as csvfile :
    flag = 0
bikeCount = 0
carCount = 0
carFlag = 0
bikeFlag = 0
while True :
    carFlagCheck = 0
    bikeFlagCheck = 0
    ret, img = vc.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    bike = bike_cascade.detectMultiScale(gray,1.04,200,minSize=(100,100), maxSize=(170,170))
    car = car_cascade.detectMultiScale(gray,1.04,130,minSize=(100,100), maxSize=(170,170))
    cv2.line(img,(100,230),(500,230),(255,255,0),3)
    #cv2.rectangle(img,(10,200),(600,600),(255,255,255),3)
    for (x,y,w,h) in bike:
        bikeFlagCheck = 1
        top = y
        if top  > 150 :
            if bikeFlag == 0 :
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                bikeCount = bikeCount + len(bike)
                with open('VehicleCount.csv','a') as csvfile :
                    fieldnames = ['Vehicle', 'flag','time','count']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    time =  strftime("%H:%M:%S", localtime())
                    count += 1
                    writer.writerow({'Vehicle': 'Bike', 'flag': flag,'time' : time,'count' : count})
                    
                print ("Bike Count " , bikeCount)
                bikeFlag = 145
                break
            else :
                bikeFlag = bikeFlag - 1
                break 

    for (x,y,w,h) in car :
        carFlagCheck = 1
        top = y
        if top  > 150 :
            if carFlag == 0 :
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                carCount = carCount + len(car) 
                print ("Car Count " , carCount)
                with open('VehicleCount.csv','a') as csvfile :
                    fieldnames = ['Vehicle', 'flag','time','count']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    time =  strftime("%H:%M:%S", localtime())
                    count += 1
                    writer.writerow({'Vehicle': 'Car', 'flag': flag,'time' : time,'count' : count})
                carFlag = 200
                break
            else :
                carFlag = carFlag - 1
                break

    if bikeFlagCheck == 0 and bikeFlag != 0 :
        bikeFlag = bikeFlag - 1

    if carFlagCheck == 0 and carFlag != 0 :
        carFlag = carFlag - 1
            
    cv2.imshow('img',img)
    #out.write(img)
    k = cv2.waitKey(1)
    
            
cv2.destroyAllWindows()


    
