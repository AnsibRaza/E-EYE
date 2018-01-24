import numpy as np
import cv2 
import time
import tracker_class

class activity_classifier():
    
    def __init__(self):
         self.simgnum = 1
         self.trackerObj = tracker_class.tracker()
         self.ptx = 0
         self.pty = 0
         self.status = False
         self.trackWindow = None
    
    def ModelInitializer(self, modelName):
        #imgNum = 1
        model = cv2.imread(modelName,0)
        size = np.size(model)

        skelt = np.zeros(model.shape,np.uint8)
        
        #temp_skelt = skelt
         
        ret,model = cv2.threshold(model,127,255,0)
        
        element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
        count = 0
        done = False 
        while( not done):
            eroded = cv2.erode(model,element)
            temp = cv2.dilate(eroded,element)
            temp = cv2.subtract(model,temp)
            skelt = cv2.bitwise_or(skelt,temp)
            model = eroded.copy()                 
            zeros = size - cv2.countNonZero(model)
            if zeros == size:
                done = True 
        w, h = skelt.shape[::-1]
        
        return skelt, w, h
  
    def classification(self, skelt, w, h, frame, frame2):    
        if self.status == False:
            threshold = 0.1
            ret, fgmask = cv2.threshold(frame,127,255,0)
            #cv2.imshow("test1",fgmask)
            size1 = np.size(fgmask)
            img_skelt = np.zeros(fgmask.shape,np.uint8)
             
            done = False
            element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
            while( not done):
                eroded = cv2.erode(fgmask,element)
                #eroded = cv2.erode(eroded,element)
                temp = cv2.dilate(eroded,element)
                temp = cv2.subtract(fgmask,temp)
                img_skelt = cv2.bitwise_or(img_skelt,temp)
                fgmask = eroded.copy()
                size1 = size1 - size1/4            
                if size1 < 30:
                    done = True        
                
            res = cv2.matchTemplate(img_skelt, skelt, cv2.TM_CCOEFF_NORMED)    
            loc = np.where( res >= threshold)
            minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
            print maxVal
            if maxVal > threshold:
                #loc = np.where( res >= threshold)
                for pt in zip(*loc[::-1]):
                    cv2.rectangle(frame2, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
                    self.ptx = pt[0]
                    self.pty = pt[1]
                    cv2.imwrite('savepic//('+str(self.simgnum)+').jpg',frame2)
                self.simgnum=self.simgnum+1      
                self.trackWindow = self.trackerObj.TrackerInitialization(self.ptx, self.pty, w, h, frame2)      
                self.status = True
            #         cv2.circle(img_rgb,(pt[0], pt[1]),3,100+(255),-1)
            
            
        elif self.status == True:
            self.trackWindow = self.trackerObj.Tracking(self.trackWindow, frame2)
            
                