# Imports
import cv2

class video:
    '''
    Class for video capture.
    '''
# Definitions
    def __init__(self):
        '''
        constructor
        '''
    
    def CaptureVideo(self, deviceId):
        capture = cv2.VideoCapture(deviceId)
        return capture
    
    def CovertToFrames(self, capture):
            # Capture frame-by-frame
            ret, frame = capture.read()
            return ret, frame
    
    def ShowVideo(self, title, frame):
        if frame is not None:
            cv2.imshow(title,frame)
            return True
        else:
            print 'Image not found at Video.'
            return False
        
#     def WindowResize(self, height, width, frame):
#         frame = frame.resize(height, width)
#         return resizedFrame
    
    def CloseVideo(self, capture):
        capture.release()
        cv2.destroyAllWindows()           
    
    def TestFunc(self):
        print 'ok'
    
        