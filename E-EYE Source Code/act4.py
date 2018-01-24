import numpy as np
import cv2 
import time

simgnum = 1
imgNum = 1
template = cv2.imread('manback.png',0)
wrframe = False

size = np.size(template)
skelt = np.zeros(template.shape,np.uint8)
 
ret,img = cv2.threshold(template,127,255,0)
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
done = False
 
while( not done):
    eroded = cv2.erode(template,element)
    temp = cv2.dilate(eroded,element)
    temp = cv2.subtract(template,temp)
    skelt = cv2.bitwise_or(skelt,temp)
    template = eroded.copy()
 
    zeros = size - cv2.countNonZero(template)
    if zeros==size:
        done = True

#cv2.imshow('Backgr',skelt)
#cv2.waitKey(0)

w, h = skelt.shape[::-1]
print w
print h

threshold = 0.2

fgbg = cv2.BackgroundSubtractorMOG()

cap = cv2.VideoCapture("walking.avi")

while(1):
    
    
    ret, img_rgb = cap.read()
    fgmask = fgbg.apply(img_rgb)
    #cv2.imshow('FGmsk',fgmask)
    
    size = np.size(fgmask)
    skel = np.zeros(fgmask.shape,np.uint8)
 
    ret,fgmask = cv2.threshold(fgmask,127,255,0)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    done = False
 
    while( not done):
        eroded = cv2.erode(fgmask,element)
        temp = cv2.dilate(eroded,element)
        temp = cv2.subtract(fgmask,temp)
        skel = cv2.bitwise_or(skel,temp)
        fgmask = eroded.copy()
 
        zeros = size - cv2.countNonZero(fgmask)
        if zeros==size:
            done = True
    
    #cv2.imshow('Backgr',skel)
    
    imgNum+= 1
    
 
    res = cv2.matchTemplate(skel,skelt,cv2.TM_CCOEFF_NORMED)
    
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
        wrframe = True
        
        
#         cv2.circle(img_rgb,(pt[0], pt[1]),3,100+(255),-1)

    
    if(wrframe == True):
        cv2.imwrite('savepic//('+str(simgnum)+').jpg',img_rgb)
        simgnum=simgnum+1
        wrframe = False
 
      #  cv2.imwrite('res.png',img_rgb)
       # cv2.imshow('Detected Val',img_rgb)
        
    k = cv2.waitKey(True)
    if k == 27:
        break
    elif k == 48:
            time.sleep(10.0)
            
    cv2.imshow('Detected Val',img_rgb)

cv2.destroyAllWindows()