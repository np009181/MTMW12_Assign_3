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
    
    dp = np.zeros(N + 1)
    
    dp[0] = (p[1] - p[0])/ dy      #I know the formula for the end points so I# 
    dp[N] = (p[N] - p[N - 1])/ dy  #have put this formula outside of the loop#
    
    for i in range (1, N):     #Finds the other points using centred#
        dp[i] = (p[i + 1] - p[i - 1])/ (2*dy)  #formula#
        
        
    print(dp)
    
    r = 1
    f = 1e-4
    
    u = -dp/(r*f)             #The formula for wind speed# 
    
    print(u)
    
    U = np.sin(np.pi*y/L) * (np.pi*pb)/(r*f*L)    #Analytical solution#
    
    plt.figure(1)
    plt.plot(y, u, label = 'Numerical')    #Plot of numerical solution#
    plt.plot(y, U, label = 'Analytical',)   #Analytical solution to compare#
    plt.xlabel('Location (m)')
    plt.ylabel('Wind speed')    
    plt.legend()
    plt.title('Comparison of Numerical and Analytical solution of wind speed')
    
    e = U - u    #Finding the errors of the numerical solution#
    
    plt.figure(2)
    plt.plot(y, e)
    plt.xlabel('Location (m)')
    plt.ylabel('Error in numerical solution')
    plt.title('Error of numerical solution compared with analytical')
    
    
    
main()

