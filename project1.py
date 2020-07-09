import cv2
import numpy as np
frameWidth = 400
frameHeight = 300
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)

myColors = [[51,80,62 ,255,0,255],
            [133,169,55,167,100,255]
            ]


def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array(myColors[0][0:3])
    upper = np.array(myColors[0][3:6])
    mask = cv2.inRange(imgHSV, lower, upper)
    cv2.imshow("img",mask)


while True:
    success,img =cap.read()
    findColor(img,myColors)
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break