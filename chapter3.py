import cv2

img= cv2.imread("Resources/lambo.png")
print(img.shape)

imgResize = cv2.resize(img,(500,500))
print(imgResize.shape)

imgCropped = img[0:200,200:500]

cv2.imshow("image",img)
cv2.imshow("resize image",imgResize)
cv2.imshow("crop image",imgCropped)

cv2.waitKey(0)