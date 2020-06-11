import cv2
import numpy as np

def nothing(x):
    pass


while True:
    frame = cv2.imread("aa.jpg")
    frame = cv2.resize(frame, (400,400))
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_b = np.array([110,100,100])
    u_b = np.array([130,255,255])
    
    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame,frame, mask=mask)
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key==27:
        break
    
cv2.destroyAllWindows()

