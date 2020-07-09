import cv2
import numpy as np

img = cv2.imread("Resources/card.png")

width,height =250,350

pts1 = np.float32([[208,541],[435,265],[570,762],[831,420]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("image",img)
cv2.imshow("output perspective",imgOutput)
cv2.waitKey(0)