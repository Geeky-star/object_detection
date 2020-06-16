import cv2

img1 = cv2.imread('star.png',0)
img2 = cv2.imread('rectangle.png',0)
img3 = cv2.imread('star1.png',0)
img4 = cv2.imread('W.png',0)
img5 = cv2.imread('M.png',0)

ret, thresh = cv2.threshold(img1, 127, 255, 0)
ret, thresh2 = cv2.threshold(img2, 127, 255, 0)
ret, thresh3 = cv2.threshold(img3, 127, 255, 0)
ret, thresh4 = cv2.threshold(img4, 127, 255, 0)
ret, thresh5 = cv2.threshold(img5, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours[0]

contours, hierarchy = cv2.findContours(thresh2, 2, 1)
cnt2 = contours[0]

contours, hierarchy = cv2.findContours(thresh3, 2, 1)
cnt3 = contours[0]

contours, hierarchy = cv2.findContours(thresh4, 2, 1)
cnt4 = contours[0]

contours, hierarchy = cv2.findContours(thresh5, 2, 1)
cnt5 = contours[0]

ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
print(ret)

ans = cv2.matchShapes(cnt1, cnt3, 1, 0.0)
print(ans)


result = cv2.matchShapes(cnt4, cnt5, 1, 0.0)
print(result)




















