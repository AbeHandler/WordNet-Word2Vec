"""
Makes the total count chart
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib
from matplotlib.ticker import FuncFormatter
import Image
from pylab import setp

import statsmodels.api as sm

lowess = sm.nonparametric.lowess

holo = []
mero = []
hyper = []
syn = []
hypo = []
same_stem = []

with open("textfiles/total_count_scatter_stem.txt") as results:
    for line in results.readlines():
        same_stem.append(int(line.replace("\n", "")))

with open("textfiles/holo.txt") as results:
    for line in results.readlines():
        holo.append(int(line.replace("\n", "")))

with open("textfiles/mero.txt") as results:
    for line in results.readlines():
        mero.append(int(line.replace("\n", "")))

with open("textfiles/hyper.txt") as results:
    for line in results.readlines():
        hyper.append(int(line.replace("\n", "")))

with open("textfiles/hypo.txt") as results:
    for line in results.readlines():
        hypo.append(int(line.replace("\n", "")))

with open("textfiles/syn.txt") as results:
    for line in results.readlines():
        syn.append(int(line.replace("\n", "")))

holo = np.array(holo[:50])
mero = np.array(mero[:50])
hyper = np.array(hyper[:50])
hypo = np.array(hypo[:50])
syn = np.array(syn[:50])
same_stem = np.array(same_stem[:50])

x = np.arange(1, len(syn) + 1, 1)

print x[0]

alpha = .4
plt.title("Count of holo relations by k")

#styles = ['', ' ', 'None', '--', '-.', '-', ':']

frac_val = .4


#plt.scatter(x, same_stem, alpha=.4, label='Same stem', marker="h")
z = [a[1] for a in lowess(same_stem, x, frac=frac_val)]
line, = plt.plot(z, label='Same stem', linestyle='-')

#plt.scatter(x, syn, alpha=.4, label='Synonyms', marker="x", color="grey")
z = [a[1] for a in lowess(syn, x, frac=frac_val)]
line = plt.plot(z, label='Synonyms', linestyle='-.')

#plt.scatter(x, hyper, alpha=.4, label='Hypernyms', marker="*")
z = [a[1] for a in lowess(hyper, x, frac=frac_val)]
line, = plt.plot(z, label='Hypernyms', linestyle="--")

#lt.scatter(x, hypo, alpha=.4, label='Hyponyms', marker=".")
z = [a[1] for a in lowess(hypo, x, frac=frac_val)]
line = plt.plot(z, label='Hyponyms', linestyle='-')

#plt.scatter(x, mero, alpha=.4, label='Meronyms', marker="d")
z = [a[1] for a in lowess(mero, x, frac=frac_val)]
line = plt.plot(z, label='Meronyms', linestyle=':')

#plt.scatter(x, holo, alpha=.4, label='Holonyms', marker="o")
z = [a[1] for a in lowess(holo, x, frac=frac_val)]
line, = plt.plot(z, label='Holonyms')
line.set_dashes([1, 3, 1, 3, 1, 3])


plt.xlabel("log k")
plt.ylabel("log count")
plt.title("Log-log count of relations with lowess best fit")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlim(.9,60)
plt.loglog()

plt.savefig('lowess.png', bbox_inches='tight', pad_inches=.4)
Image.open('lowess.png').convert('L').save('lowess2.png')