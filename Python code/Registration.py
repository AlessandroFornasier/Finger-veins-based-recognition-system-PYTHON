import os
import time
from preprocessing_function import preprocessing

#clearing screen
unused_variable = os.system("cls")

def TicTocGenerator():
    # Generator that returns time differences
    ti = 0           # initial time
    tf = time.time() # final time
    while True:
        ti = tf
        tf = time.time()
        yield tf-ti # returns the time difference

TicToc = TicTocGenerator() # create an instance of the TicTocGen generator

# This will be the main function through which we define both tic() and toc()
def toc(tempBool=True):
    # Prints the time difference yielded by generator instance TicToc
    tempTimeInterval = next(TicToc)
    if tempBool:
        print( "Elapsed time: %f seconds.\n" %tempTimeInterval )

def tic():
    # Records a time in TicToc, marks the beginning of a time interval
    toc(False)
    
tic()

N = 3 #Number of persons
M = 6 #Number of images per person

for x in range(1,N+1):
    pathname = 'Model/'+str(x)
    preprocessing(pathname,M) 
    
toc()


