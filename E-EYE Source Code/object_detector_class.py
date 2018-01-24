# Imports
import cv2
import preprocessing_class
import postprocessing_class
import numpy as np
import activity_classifier_class

# Definitions
class object_detector():
    '''
    This is class of functionalities of object detection.
    '''

    def __init__(self):
        '''
        Constructor of object_detector class.
        '''
        self.frameNum = 1
        self.mask = None
        self.preProcessObj = preprocessing_class.preprocessing()
        self.postProcessObj = postprocessing_class.postprocessing()
        self.activityClassifierObj = activity_classifier_class.activity_classifier()
        self.frame = None
        
    def GenerateMask(self):
        self.mask = cv2.BackgroundSubtractorMOG2()
        return self.mask
    
    def ApplyMask(self, mask, grayScale):
        backgroundSubtracted = self.mask.apply(grayScale)
        return backgroundSubtracted
    
    def SetFrame(self, frame):
        self.frame = frame
        return self.frame
    
    def GetFrame(self):
        return self.frame
    
    def Detection(self, frame2):
        if self.frameNum == 1 :
            self.mask = self.GenerateMask()
            self.skelt, self.w, self.h = self.activityClassifierObj.ModelInitializer('gun.png')
            self.frameNum+= 1
            return None
        else:
            if frame2 is not None:
                frame = self.GetFrame()
                
                grayscaleFrame = self.preProcessObj.ConvertToGrayScale(frame2)
                
                backgroundSubtracted = self.ApplyMask(self.mask, grayscaleFrame)
                
#                 kernel = self.postProcessObj.GenerateKernel(3, 3)
#                 erodedObjects = self.postProcessObj.ErodeObjects(backgroundSubtracted, kernel, 2)
#                 dilatedObjects = self.postProcessObj.DilateObjects(erodedObjects, kernel, 2)
                
                ret, binaryObjects = self.postProcessObj.Thresholding(backgroundSubtracted, 127, 255)
                
#                 kernel = self.postProcessObj.GenerateKernel(7, 2)
#                 temp_crop__img = dilatedObjects = self.postProcessObj.DilateObjects(binaryObjects, kernel, 2)
                
                #cv2.imshow("test", binaryObjects)
                self.activityClassifierObj.classification(self.skelt, self.w, self.h, binaryObjects, frame2)
#                 contours = self.postProcessObj.Countours(binaryObjects)
#                 
#                 for cnt in contours:
#                     x,y,w,h = cv2.boundingRect(cnt)
#                     if w > 5 | h > 5:
#                         #cv2.rectangle(frame2,(x,y),(x+w,y+h),(0,255,0),2)
#                                                 
#                         temp_crop_img = dilatedObjects[y:(y+h),x:(x+w)]
#                         #self.activityClassifierObj.classification(self.skelt, self.w, self.h, temp_crop__img, frame2)
#                         #cv2.imshow("test2",temp_crop_img)
#                         
#                         #cv2.imshow("croped",crop_img)
#                         #cv2.circle(frame2, (x+3,y-4), 20, (255,0,0), 1)
#                         #features = self.trackerObj.ExtractFeatures(self.frame, x,y,w,h, 50)
#                         #self.trackerObj.Tracking(self.frame, modifyedFrame, frame2, features, x,y,w,h)
#                         #cv2.imshow('camera', frame2)
#                             
#                 return self.frame
            else:
                print 'Image not found at Object Detection.'
                return None
        