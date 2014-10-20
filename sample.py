import pylab as plb
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import scipy as sp
from scipy.optimize import curve_fit
from matplotlib import rc
import numpy as np
rc('font', **{'family':'sans-serif', 'sans-serif':['Helvetica']})
rc('text', usetex=True)

import sys

x_arr = []

for l in sys.stdin:
	x_arr.append(float(l.replace("\n", "")))

# Fake data
x = np.arange(0, 70, 1)
yl = 300 + 63*np.exp(-x/35.)

print type(yl)
yl = np.array(x_arr)

print x
print yl

def func(x, a, b, c):
    return a*np.exp(-b*x) + c

popt, pcov = curve_fit(func, x, yl, maxfev=20000)
a, b, c = popt
#print 'a=', a, 'b=', b, 'c=', c
#print 'func=', func(x, a, b, c)

xf = np.linspace(0, 70, 100)
yf = a*np.exp(-b*x) + c

plt.clf()

plt.plot(x, func(x, *popt))

plt.plot(x, yl, 'go', label='Lacquered')

plt.legend()
plt.ylabel("Temperature (K)")
plt.xlabel("Time (min)")
plt.show()