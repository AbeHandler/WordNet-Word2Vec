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

x = np.arange(0, len(x_arr), 1)

#print type(yl)
y = np.array(x_arr)


logx = np.log(x)
logy = np.log(y)

print logx
print logy

coeffs = np.polyfit(logx,logy,deg=2)
poly = np.poly1d(coeffs)

yfit = lambda x: np.exp(poly(np.log(x)))

print x
print yfit(x)

plt.plot(logx, logy)
plt.show()