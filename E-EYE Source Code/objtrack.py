import numpy as np
import cv2

class trackclass():

    def __init__(self):
        self.temp = None
    def run_main(self, c, r, w, h, frame):
        
        track_window = (c,r,w,h)
        return track_window
        
    def run_main2(self, track_window, frame):    
        
       
        c,r,w,h = track_window
        roi = frame[r:r+h, c:c+w]
        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_roi, np.array((0., 30.,32.)), np.array((180.,255.,255.)))
        roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
        cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
        term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 80, 1)
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        x,y,w,h = track_window
        cv2.rectangle(frame, (x,y), (x+w,y+h), 255, 2)
        cv2.putText(frame, 'Abnormal Activity', (x-25,y-10), cv2.FONT_HERSHEY_SIMPLEX,
            1, (0,0,255), 2, cv2.CV_AA)
        print "ok"
        return track_window
