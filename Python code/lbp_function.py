import numpy as np

def lbp(I):

    [r,c] = I.shape[:2]
    LBPM = np.zeros((r-2, c-2),np.uint32)

    xmask = [[1, 2, 4],
            [128, 0, 8],
            [64, 32, 16]]
    
    mask = np.array(xmask, np.uint16);
    
    for j in range(2,r-1):
        for k in range(2,c-1):
            temp = I[j-2:j+1, k-2:k+1] // 255
            temp = np.multiply(mask,temp) 
            LBPM[j-1,k-1] = np.sum(temp)
                       
    return LBPM