import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import imutils

def fingerroi(I, cropSize):

    [R,C] = I.shape[:2]

    #Crop the image
    I = I[0:R, cropSize:R]
    [R,C] = I.shape[:2]
    
    (thresh, T) = cv.threshold(I,128,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    
    cnts = cv.findContours(T.copy(),cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv.contourArea)
    
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])
    
    #Getting one value from extreme points
    MinX, yy = extLeft
    MaxX, yyy = extRight
    xx, MaxY = extBot
    xxx, MinY = extTop
    
    #ROI box
    #cv.rectangle(I,(MinX,0),(MaxX,MaxY),(255,255,0),2)
    
    #RETURNS ROI AND MASK
    ROI = I[1:MaxY-10,MinX+20:MaxX-50]
    BW = T[1:MaxY-10,MinX+20:MaxX-50]

    
    return ROI,BW