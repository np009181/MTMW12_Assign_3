#Intro to numerical modelling - Assignment 3#

#Question 1#
import numpy as np

def main():
    ymin = 0.                 #Setting values for fixed numbers#
    ymax = 1e6
    N = 10
    y = np.zeros(N + 1)

    
    dy = (ymax - ymin)/N      #The difference between each point#
    
    for i in range(N + 1):   
        y[i] = ymin + dy*i    #Evaluates y at every interval#
    
    print(y)
    
    pa = 1e5                  #Defining set values for pressure equation#
    pb = 200
    L = 2400000
    p = np.zeros(N + 1)
    
    for i in range (N + 1):
        p[i] = pa + pb*np.cos((y[i]*np.pi)/L)   #Evaluates the pressure at
                              #every interval y#
        
    print(p)
    
    
    
    
main()

