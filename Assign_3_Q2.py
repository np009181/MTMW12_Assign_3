#Intro to numerical modelling - Assignment 3#



#Question 2#

import numpy as np
import matplotlib.pyplot as plt

def main2():
    
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

    dp = np.zeros(N + 1)
    
    dp[0] = (p[2] - 4*p[1] + 3*p[0])/ 2*dy      #I know the formula for the end points so I# 
    dp[N] = (p[N] - p[N - 1])/ dy  #have put this formula outside of the loop#
    
    for i in range (1, N):     #Finds the other points using centred#
         dp[i] = (-p[i + 2] + 8*p[i + 1] - 8*p[i - 1] + p[i + 2])/ (12*dy)  #formula#
    
    print(dp)
    
    r = 1
    f = 1e-4
    
    u = -dp/(r*f)             #The formula for wind speed 
    
    print(u)
    
    U = np.sin(np.pi*y/L) * (np.pi*pb)/(r*f*L)    #Analytical solution#
    
    plt.figure(1)
    plt.plot(y, u, label = 'Numerical')    #Plot of numerical solution#
    plt.plot(y, U, label = 'Analytical',)   #Analytical solution to compare#
    plt.xlabel('Location (m)')
    plt.ylabel('Wind speed')   
    plt.legend()
    plt.title('Comparison of Numerical and Analytical solution of wind speed')
    
    
    
    
    
    
    
    
    
main2()
