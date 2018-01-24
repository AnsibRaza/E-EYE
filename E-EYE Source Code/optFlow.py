import cv2
import numpy as np

capture = cv2.VideoCapture(0)

ret, prev_frame = capture.read()
    
#Setting the parameters.

lk_params = dict( winSize  = (10, 10), 
                  maxLevel = 5, 
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))   

feature_params = dict( maxCorners = 3000, 
                       qualityLevel = 0.2,
                       minDistance = 3,
                       blockSize = 3)

prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
prev_pt = cv2.goodFeaturesToTrack(prev_frame, **feature_params)
prev_pt = np.float32(prev_pt).reshape(-1, 1, 2)
next_pt = None    

while(True):
    #Get the good features to track.
    
    ret, img1 = capture.read()
    
    next_frame = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) # get grayscale image
   
    
    p1, st, err = cv2.calcOpticalFlowPyrLK(prev_frame, next_frame, prev_pt, next_pt, **lk_params)
    
    p1 = np.int0(p1)
    print p1
    for i in p1:
        fX,fY = i.ravel()
        cv2.circle(frame,(fX,fY),3,255,-1)
        
    cv2.imshow('title',frame)
    
    prev_pt = None
    next_pt = np.float32(next_pt).reshape(-1, 1, 2)
    prev_pt = next_pt
    prev_frame = next_frame
    k = cv2.waitKey(150) & 0xff
    if k == 27:
        break
    elif k == 48:
        time.sleep(5.0)