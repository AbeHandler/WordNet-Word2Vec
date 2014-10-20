"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import sys
import re
import math
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from scipy.optimize import curve_fit
import sympy as sym

def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] == True:
        return s + r'$\%$'
    else:
        return s + '%'

lines = []

ks = range(1, 201)

floor = {}

for i in range(1, len(ks)):
    floor[ks[i]] = ks[i-1]

floor[ks[0]] = 0

labels = []
labels.append("<" + str(ks[0]))

for i in range(1, len(ks)):
    labels.append(str(ks[i-1]) + '-' + str(ks[i]))


def isIt(s, p):
    if len(re.findall(p, s)) > 0:
        return True
    return False


for line in sys.stdin:
    lines.append(line.replace("\n", ""))


def is_k(l, k):
    if len(l) == 0:
        return False
    try:
        if (int(l.split(",")[4]) == k):
            return True
        return False
    except ValueError:
        return False

syn = [l for l in lines if isIt(l, "^syn")]
'''
hypo = [l for l in lines if isIt(l, "^hypo")]
hyper = [l for l in lines if isIt(l, "^hyper")]
holo = [l for l in lines if isIt(l, "^holo")]
mero = [l for l in lines if isIt(l, "^mero")]
stem = [l for l in lines if isIt(l, "^same stem")]
none = [l for l in lines if isIt(l, "^none")]
'''
total = float(len(lines))

n_groups = 5

count_syn = []
count_hyper = []
count_hypo = []
count_holo = []
count_stem = []
count_mero = []
count_none = []
base = 10


x = []
y = []


def func(x, base_n, times, plus):
    return math.log(x, base_n)*times + plus


for k in ks:
    syn_hits = float(sum(1 for l in syn if is_k(l, k)))
    total_hits = float(sum(1 for l in lines if is_k(l, k)))
    x.append(k)
    y.append(syn_hits/total_hits)
    print ",".join([str(k), str(syn_hits/total_hits)])


x = np.array(x)
y = np.array(y)

area = 5 # 0 to 15 point radiuses

popt, pcov = curve_fit(func, x, y)

xs = sym.Symbol('\lambda')    
tex = sym.latex(func(xs,*popt)).replace('$', '')
plt.title(r'$f(\lambda)= %s$' %(tex),fontsize=16)

plt.plot(x, func(x, *popt), label="Fitted Curve")
plt.legend(loc='upper left')
plt.show()

"""
Print the coefficients and plot the funcion.
"""





#for k in ks:
#    count_hyper.append(float(len([s for s in hyper if lessThanGreaterThanK(s, k)]))/ float(len([t for t in lines if lessThanGreaterThanK(t, k)])))

#for k in ks:
#    count_hypo.append(float(len([s for s in hypo if lessThanGreaterThanK(s, k)])) / float(len([t for t in lines if lessThanGreaterThanK(t, k)])))

#for k in ks:
#    count_holo.append(float(len([s for s in holo if lessThanGreaterThanK(s, k)]))/ float(len([t for t in lines if lessThanGreaterThanK(t, k)])))

#for k in ks:
#    count_mero.append(float(len([s for s in mero if lessThanGreaterThanK(s, k)]))/ float(len([t for t in lines if lessThanGreaterThanK(t, k)])))

#for k in ks:
#    count_stem.append(float(len([s for s in stem if lessThanGreaterThanK(s, k)]))/ float(len([t for t in lines if lessThanGreaterThanK(t, k)])))

#for k in ks:
#    count_none.append(float(len([s for s in none if lessThanGreaterThanK(s, k)]))/ float(len([t for t in lines if lessThanGreaterThanK(t, k)])))

'''
count_syn = tuple(count_syn)

count_hyper = tuple(count_hyper)
count_hypo = tuple(count_hypo)
count_holo = tuple(count_holo)
count_mero = tuple(count_mero)
count_stem = tuple(count_stem)


import matplotlib.pyplot as plt
fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.1

opacity = 0.4
error_config = {'ecolor': '0.3'}


rects1 = plt.bar(index + .1, count_syn, bar_width,
                 alpha=opacity,
                 color='blue',
                 label='synonyms')

rects2 = plt.bar(index + .2, count_hyper, bar_width,
                 alpha=opacity,
                 color='red',
                 label='hypernyms')


rects3 = plt.bar(index + .3, count_hypo, bar_width,
                 alpha=opacity,
                 color='purple',
                 label='hyponyms')


rects4 = plt.bar(index + .4, count_holo, bar_width,
                 alpha=opacity,
                 color='green',
                 label='holonyms')


rects5 = plt.bar(index + .5, count_mero, bar_width,
                 alpha=opacity,
                 color='orange',
                 label='meronyms')


rects6 = plt.bar(index + .6, count_stem, bar_width,
                 alpha=opacity,
                 color='yellow',
                 label='same stem')

plt.xlabel('K')
plt.ylabel('Percentage likelyhood of relation')
plt.title('Semantic Similarity in Word2Vec Compared To WordNet')

plt.xticks(index + bar_width * 4, labels)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
formatter = FuncFormatter(to_percent)
plt.gca().yaxis.set_major_formatter(formatter)
plt.savefig('Likelyhood.png', bbox_inches='tight', pad_inches=.4)
'''