import cv2 as cv
import matplotlib.pyplot as plt
from fingerroi_function import fingerroi
from skimage.filters import threshold_niblack
from skimage.data import page
import numpy as np
import matplotlib
import skimage
from skimage import filters

def preprocessing(pathname,M):

    for j in range(1,M+1):
    
        #Image read
        I = cv.imread(pathname + '/' + '0' + str(j) + '.jpg', cv.IMREAD_GRAYSCALE)
        
        #ROI Extraction and size reduction
        ROI, BW = fingerroi(I,60)
        
        #Image enhancement
        normROI = cv.normalize(ROI, None, alpha=0, beta=1,
                                   norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)  
        
        #Thresholding
        nib = skimage.filters.threshold_niblack(normROI, window_size=31, k=0.1)
        niBlack = normROI > nib
        
        #Applying opening
        kernel = np.ones((6,3),np.uint8)
        niBlack = np.array(niBlack, dtype=np.uint8)
        TROIs = cv.morphologyEx(niBlack, cv.MORPH_OPEN, kernel)
        
        blur = cv.GaussianBlur(TROIs,(5,5),0)
        ret3,TROI = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
        
        #Resize
        #resize image so there are 200x50 pixels
        resizedTROI = cv.resize(TROI, (50, 200))
        
        #Save
        plt.imsave(pathname + '/' + 'MMM0' + str(j) + '.jpg',resizedTROI)
        

        