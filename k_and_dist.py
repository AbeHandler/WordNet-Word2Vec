import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import stats

xx = []
holo = []
syn = []
hyper = []
hypo = []
mero = []
none = []

with open("textfiles/none.txt") as results:
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
            none.append(y)

with open("textfiles/holo.txt") as results:
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
            holo.append(y)


with open("textfiles/syn.txt") as results:
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
            syn.append(y)


with open("textfiles/hyper.txt") as results:
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
            hyper.append(y)


with open("textfiles/hypo.txt") as results:
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
            hypo.append(y)

with open("textfiles/mero.txt") as results:
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
            mero.append(y)

holo = np.array(holo)
syn = np.array(syn)
hyper = np.array(hyper)
hypo = np.array(hypo)
mero = np.array(mero)

alpha = .3
plt.hist(holo, color="red", alpha=alpha)
plt.hist(syn, color="blue", alpha=alpha)
plt.hist(hyper, color="yellow", alpha=alpha)
plt.hist(hypo, color="green", alpha=alpha)
plt.hist(mero, color="purple", alpha=alpha)
plt.hist(none, color="orange", alpha=alpha)
'''
density_mero = stats.kde.gaussian_kde(mero)
x = np.arange(0., 1, .01)
plt.plot(x, density_mero(x))

density_holo = stats.kde.gaussian_kde(holo)
x = np.arange(0., 1, .01)
plt.plot(x, density_holo(x))

density_syn = stats.kde.gaussian_kde(syn)
x = np.arange(0., 1, .01)
plt.plot(x, density_syn(x))

density_hyper = stats.kde.gaussian_kde(hyper)
x = np.arange(0., 1, .01)
plt.plot(x, density_hyper(x))

density_hypo = stats.kde.gaussian_kde(hypo)
x = np.arange(0., 1, .01)
plt.plot(x, density_hypo(x), label="hypo")

density_none = stats.kde.gaussian_kde(none)
x = np.arange(0., 1, .01)
plt.plot(x, density_none(x), label="none")
'''
plt.legend()
#plt.loglog()
plt.show()
