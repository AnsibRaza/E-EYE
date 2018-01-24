# Imports
import cv2
import numpy as np
from matplotlib import pyplot as plt

class postprocessing():
    '''
    classdocs
    '''
# Definitions

    def __init__(self):
        '''
        Constructor
        '''
    def GenerateKernel(self, rows, columns):
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3)) #np.ones((rows,columns),np.uint8)
        return kernel 
        
    def ErodeObjects(self, frame, kernel, iteration):
        eroded = cv2.erode(frame, kernel, iterations = iteration)   
        return eroded
    
    def DilateObjects(self, frame, kernel, iteration):
        dilated = cv2.dilate(frame, kernel, iterations = iteration)
        return dilated
    
    def Thresholding(self, frame, threshold, value):
        ret,binaryImage = cv2.threshold(frame,threshold,value,cv2.THRESH_BINARY)
        return ret, binaryImage
    
    def Countours(self, frame):
        contours, hierarchy = cv2.findContours(frame, 2, 3)
        return contours
    
    def DrawRectangle(self, frame, contours, color, thickness):
        x,y,w,h = cv2.boundingRect(contours)
        cv2.rectangle(frame,(x,y),(x+w,y+h),color,thickness)
        return x, y, w, h
            