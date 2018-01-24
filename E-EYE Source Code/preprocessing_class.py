# Imports
import cv2

class preprocessing():
    '''
    class for preprocessing on images.
    '''
# Definitions
    def __init__(self):
        '''
        Constructor
        '''
        
    def ConvertToGrayScale(self, frame):
        if frame is not None:
            grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            return grayImage
        else:
            print 'Image not found at preprocessing'
            return None