import numpy as np
import matplotlib.pyplot as plt

def lbpmatch(I1,I2):

    if I1.shape == I2.shape:  
        
        [r,c] = I1.shape[:2]
        match = np.zeros((r,c), np.uint8)
        tempSum = 0
        
        for j in range(1,r):
            for k in range(1,c):
                
                I1bin = bin(I1[j,k])
                I2bin= bin(I2[j,k])
                
                y = int(I1bin, 2)^int(I2bin,2)
                xor = bin(y)[2:].zfill(len(I1bin))
                match[j,k] = xor.count("1")
                tempSum += match[j,k]
                 
        match = tempSum
        
        return match