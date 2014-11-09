import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import stats
import statsmodels.api as sm
import random

lowess = sm.nonparametric.lowess

xx = []
yy = []



my_randoms=[]

with open("textfiles/dandd.txt") as results:
    for line in results.readlines():
        y, x = line.split(",")
        flot = True
        try:
            x = float(x.replace("\n", ""))
            y = float(y.replace("\n", ""))
        except:
            flot = False
            pass
        if flot:
            yy.append(y)
            xx.append(x)


for i in range (10000):
    my_randoms.append(random.randrange(1, len(yy), 1))


plot_x = []
plot_y = []


for r in my_randoms:
    plot_x.append(xx[r])
    #print yy[r]
    plot_y.append(yy[r])


xx = np.array(plot_x)
yy = np.array(plot_y)

alls = [a for a in lowess(xx, yy, frac=.7)]
xes = [x[1] for x in alls]
yes = [y[0] for y in alls]

line, = plt.plot(xes, yes)

#plt.loglog()
plt.show()
