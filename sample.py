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
x1_arr = []
x2_arr = []

with open("textfiles/syn_probabilities.txt") as results:
    for line in results.readlines():
        x_arr.append(float(line.replace("\n", "")))

with open("textfiles/hyper_probabilities.txt") as results:
    for line in results.readlines():
        x1_arr.append(float(line.replace("\n", "")))

with open("textfiles/hypo_probabilities.txt") as results:
    for line in results.readlines():
        x2_arr.append(float(line.replace("\n", "")))

# Fake data
x = np.arange(0, len(x_arr), 1)

#print type(yl)
yl = np.array(x_arr)
yl1 = np.array(x1_arr)
yl2 = np.array(x2_arr)

#print x
#print yl

def func(x, a, b, c):
    return a*np.exp(-b*x) + c

popt, pcov = curve_fit(func, x, yl, maxfev=20000)
a, b, c = popt
print 'a=', a, 'b=', b, 'c=', c
print 'func=', func(x, a, b, c)

xf = np.linspace(0, 70, 100)
yf = a*np.exp(-b*x) + c

plt.title(r'$\alpha > \beta$')

title = str(round(a, 4)) + "\\" + "times" + "\\" + "ln{(x)} + " + str(round(c, 4))

plt.title(r'$' + title + '$')

print a 
print b
print c

plt.clf()
opacity = 0.4
#plt.plot(x, func(x, *popt))

plt.plot(x, yl, 'go', label='Synonyms', color="blue", alpha=opacity)
plt.plot(x, yl1, 'go', label='Hypernyms', color="red", alpha=opacity)
plt.plot(x, yl2, 'go', label='Hypornyms', color="yellow", alpha=opacity)

plt.legend()
plt.xlabel("ln(k)")
plt.ylabel("ln(probability)")
plt.xlim([0,700])
plt.ylim(.003162277, .1)
plt.loglog()
plt.minorticks_off()
plt.title("Relations: ln probability by ln k")
plt.savefig('loglog_prob.png', bbox_inches='tight', pad_inches=.4)