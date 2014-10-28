# This is the code used for the second mandatory assignment in
# MAT1120 - Linear Algebra
# at the University of Oslo.

import numpy as np
import matplotlib.pylab as plt
from assignment import *

plt.xkcd()
# Initializing and calculating matrices C and S
n = 8
C = np.zeros((n, n))
S = np.zeros((n, n))
t = np.pi/16 + (np.linspace(1, 8, 8)-1)*np.pi/8

for i in range(n):
    for j in range(n):
        C[i][j] = np.cos((j)*t[i])
        S[i][j] = np.sin((j+1)*t[i])

def f(t):
    return (np.pi**2 - t**2)*np.exp(t/(2*np.pi))

def f_l(t):
    return 0.5*(f(t) + f(-t)) 

def f_o(t):
    return 0.5*(f(t) - f(-t))

def f_midpoint(t, yc, ys):
    c = np.cos
    s = np.sin
    return    yc[0] + yc[1]*c(t) + yc[2]*c(2*t) + yc[3]*c(3*t) + yc[4]*c(4*t)\
            + yc[5]*c(5*t) + yc[6]*c(6*t) + yc[7]*c(7*t)\
            + ys[0]*s(t) + ys[1]*s(2*t) + ys[2]*s(3*t) + ys[3]*s(4*t) + ys[4]*s(5*t)\
            + ys[5]*s(6*t) + ys[6]*s(7*t) + ys[7]*s(8*t)






time_values = np.linspace(-np.pi, np.pi, 1000)
yl = calc_vector_y(f_l, n)
yo = calc_vector_y(f_o, n)
yc = find_inverse(C).dot(yl)
ys = find_inverse(S).dot(yo)

plt.plot(time_values, f(time_values), time_values, f_midpoint(time_values, yc, ys))

plt.show()

