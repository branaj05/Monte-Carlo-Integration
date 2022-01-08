"""
Austin Brandenberger-Pys 325
Python 3.7.7
13 October 2020

Goal is to use a new integration method by plotting random numbers within some square area.
If I plot a million points within my area, compare the point's position with f(x), and find the ratio of above
vs below f(x) I can find what percentage of my square area is underneath f(x). This method is great for dealing with
sudden/irregular functions
"""
import numpy as np
import setuptools
import matplotlib.pyplot as plt
import random as rand

nint = 1000

a = 0
da = 1e-5
b = 2
db = 1e-5
height = 1
width = (b-a)

def f(x): #integrating this function the normal way would be difficult and inaccurate-plot it if you want to see why. 
    return (np.sin(1/(x*(2-x)))**2)
xarr = np.linspace(a+da, b-db, nint)
yarr = np.zeros(nint, float)

for i in range(nint-1):
    yarr[i] = f(xarr[i])


lt_x = []
lt_y = []

N = 10000
def check(N):
    less_than = 0
    for i in range(N):
        x0 = rand.random()
        x = a + x0*(b-a) #this shifts it from a random number between 0,1 to 0,2
        y = rand.random() #this is a random number between 0 and 1
        if y < f(x):
            less_than +=1
            lt_x.append(x)
            lt_y.append(y) #these are lists to store the co-ordinates populated
    A_random = height*width
    A_curve = A_random*(less_than/N)
    return A_curve, less_than ,'vs', N

#call_func= check(N) #have to call the function in order to populate lt_x and lt_y
print(check(N))



plt.plot(lt_x, lt_y, 'r.')
plt.plot(xarr, yarr)
plt.show()




