import os
from Registration import TicTocGenerator
from Registration import tic
from Registration import toc
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

from preprocessing_function import preprocessing
from lbp_function import lbp
from lbpmatch_function import lbpmatch

#clearing screen
clear = lambda: os.system('cls')
clear()

tic()

N = 2   #Person id
M = 6   #Number of image per person
P = 3   #Number of person in database
R = 6   #Number of model per person

pathname = 'Acquisition/'+str(N)
preprocessing(pathname, M)

toc()

print("-----------Authentication-----------")

tic()

T = 22000
flag = 0

minmatch = 1000000

#Acqusition images
for j in range(1,M+1):
    
    #Image read
    img = cv.imread(pathname + '/' + 'MMM0' + str(j) + '.jpg',cv.IMREAD_GRAYSCALE)
    
    # Otsu's thresholding after Gaussian filtering
    blurI = cv.GaussianBlur(img,(5,5),0)
    ret3,I = cv.threshold(blurI,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    
    #LBP calculation
    LBP = lbp(I)
            
    #LBP Matching with every model
    for k in range(1,P+1):
        if flag == 1:
            break
        
        for r in range(1,R+1):
            MI = cv.imread("Model" + '/' + str(k) + '/' + 'MMM0'+ str(r) + '.jpg',cv.IMREAD_GRAYSCALE)
            blurMI = cv.GaussianBlur(MI,(5,5),0)
            ret3,MI = cv.threshold(blurMI,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
            MLBP = lbp(MI)
            match = lbpmatch(LBP,MLBP)
            
            if match < T:
                flag = 1
                acqI = j
                mod = k
                modI = r
                break
            
print('---------Matching result----------')

if flag == 1:
    print("Match value: ", match)
    print("Person ID: ",N)
    print("Acquisition image used: ",acqI)
    print("Matched model: ",mod)
    print("Model image used: ",modI)
    
    #show images
    plt.imshow(cv.imread(pathname + '/' + '0' + str(acqI) + '.jpg'))
    plt.title('Acquisition image used')
    plt.show()
    
    plt.imshow(I, cmap = 'gray')
    plt.title('Acquisition image template')
    plt.show()

    
    plt.imshow(cv.imread("Model" + '/' + str(mod) + '/' + '0'+ str(modI) + '.jpg'))
    plt.title('Model image used')
    plt.show()
    
    plt.imshow(MI, cmap = 'gray')
    plt.title('Model image template')
    plt.show()
    
else:
    print("Match value: ", match)
    print("No matching")
    
    #show images
    plt.imshow(I, cmap = 'gray')
    plt.title('Acquisition image used')
    plt.show()
    
    plt.imshow(cv.imread(pathname + '/' + '0' + str(acqI) + '.jpg'))
    plt.title('Acquisition image template')
    plt.show()
    
toc()
