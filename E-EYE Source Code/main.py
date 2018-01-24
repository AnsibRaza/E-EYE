# imports
import video_class
import cv2
import object_detector_class
import time

class main_class():

    # Definations
    def Start(self):                                                
        videoObj = video_class.video()
        detectionObj = object_detector_class.object_detector()
        capture = cv2.VideoCapture("edited.mp4")
        #capture = videoObj.CaptureVideo(0)
        ret = True
        frameNum = 1
        imgNum = 1
        
        while(ret == True):
            ret, frame = videoObj.CovertToFrames(capture)
            imgNum+= 1
            #frame = cv2.imread('Video1// ('+str(imgNum)+').jpg')
            frame2 = frame
            #frame = videoObj.WindowResize(200, 200, frame)
            detectionObj.SetFrame(frame)
            modifyedFrame = detectionObj.Detection(frame2)
            ret = videoObj.ShowVideo('Camera', frame)
            k = cv2.waitKey(140) & 0xff
            if k == 27:
                break
            elif k == 48:
                time.sleep(5.0)       
        
        videoObj.CloseVideo(capture)
    
    if __name__ == '__main__':    
        Start()