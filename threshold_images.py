import cv2

img = cv2.imread('aa.jpg')
_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

img= cv2.resize(img, (400,400))
th1= cv2.resize(th1, (400,400))
th2= cv2.resize(th2, (400,400))
th3= cv2.resize(th3, (400,400))
th4= cv2.resize(th4, (400,400))
th5= cv2.resize(th5, (400,400))


cv2.imshow("Image", img)
cv2.imshow("th1", th1)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)
cv2.imshow("th4", th4)
cv2.imshow("th5", th5)

cv2.waitKey(0)
cv2.destroyAllWindows()