#%matplotlib inline
import numpy as np
from matplotlib import pyplot as plt
from math import sin, cos, exp, pi, sqrt
import math


"""
Fourier series here

"""
x = np.linspace(0,5,500)



def step(x):
    """
    so this is like a function that aj gives where you just have to use this (as in nobody knows how it works)
    """
    return 0.0 if x%3>(3./2) else 1.0

"""
I split these into two functions so its easier, you know

"""


def integrate_ai(x, i, L):
    """
    This integrates the half of the function 
    """
    xs = np.linspace(0, L, 100)
    h = xs[1] - xs[0]
    first = ((step(xs[0])*math.cos(i*math.pi*xs[0]/float(L)))/2.0)*h
    last = ((step(xs[-1])*math.cos(i*math.pi*xs[-1]/float(L)))/2.0)*h
    int_sum = 0
    for j in xs[1:-1]:
        int_sum += (step(j)*math.cos(i*math.pi*j/float(L))) * h
    return (int_sum + first + last) / float(L)

def integrate_bi(x, i, L):
    """
    This integrates the other half of the function 

    Look at hwk4 for reference 
    """

    xs = np.linspace(0, L, 100)
    h = xs[1] - xs[0]
    first = ((step(xs[0])*math.sin(i*math.pi*xs[0]/float(L)))/2.0)*h
    last = ((step(xs[-1])*math.sin(i*math.pi*xs[-1]/float(L)))/2.0)*h
    int_sum = 0
    for j in xs[1:-1]:
        int_sum += (step(j)*math.sin(i*math.pi*j/float(L))) * h
    return (int_sum + first + last) / float(L)

def f(x, n, L=1.5):

    """
    This is just like main it calls the both functions and sums it up to integrate
    """
    s = 0
    for i in range(n+1):
        if i == 0:
            s += integrate_ai(x, i, L)/2.0
        else:
            s += (integrate_ai(x, i, L)*cos(i*math.pi*(x/float(L)))) + (integrate_bi(x, i, L)*sin(i*math.pi*(x/float(L))))
    return s

y = [step(xx) for xx in x]
fy = np.array([f(xx, 3) for xx in x])

plt.plot(x,y,label='step')
plt.plot(x,fy)
plt.grid()
plt.legend()

