import cv2

cap = cv2.VideoCapture('video.mp4')
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

out = cv2.VideoWriter("output/backgroundoutput.mp4", fourcc, 5.0, (1280,720))

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    
    ret, frame = cap.read()
    if frame is None:
        break
    
    fgmask = fgbg.apply(frame)
    
    cv2.imshow('Frame', frame)
    cv2.imshow('FG MASK Frame', fgmask)
    
    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
    
cap.release()
cv2.destroyAllWindows()

