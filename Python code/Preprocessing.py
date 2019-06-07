import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
import cv2 as cv
import numpy as np

#clearing screen
unused_variable = os.system("cls")

I = cv.imread('Acquisition/1/05.jpg', cv.IMREAD_GRAYSCALE)

R,C = I.shape[:2] #R = height and C = width

#ROI
cropSize = 120
I = I[0:R, cropSize:R] # y , y2

(thresh, T) = cv.threshold(I,128,255,cv.THRESH_BINARY | cv.THRESH_OTSU)

plt.imshow(I)
plt.title('I in PREprocessing')
plt.show()




