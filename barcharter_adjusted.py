"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import sys
import re
import math


lines = []


def isIt(s, p):
    if len(re.findall(p, s)) > 0:
        return True
    return False


for line in sys.stdin:
    lines.append(line.replace("\n", ""))


def lessThanGreaterThanK(l, k):
    try:
        if (int(l.split(",")[4]) <= k and int(l.split(",")[4]) > floor[k]):
            return True
        return False
    except ValueError:
        pass

syn = [l for l in lines if isIt(l, "^syn")]
hypo = [l for l in lines if isIt(l, "^hypo")]
hyper = [l for l in lines if isIt(l, "^hyper")]
holo = [l for l in lines if isIt(l, "^holo")]
mero = [l for l in lines if isIt(l, "^mero")]


n_groups = 5

ks = [200, 400, 600, 800, 1000]
floor = {}
floor[200] = 0
floor[400] = 200
floor[600] = 400
floor[800] = 600
floor[1000] = 800

count_syn = []
count_hyper = []
count_hypo = []
count_holo = []
count_mero = []
base = 10

for k in ks:
    count_syn.append(len([s for s in syn if lessThanGreaterThanK(s, k)]))

for k in ks:
    count_hyper.append(len([s for s in hyper if lessThanGreaterThanK(s, k)]))

for k in ks:
    count_hypo.append(len([s for s in hypo if lessThanGreaterThanK(s, k)]))

for k in ks:
    count_holo.append(len([s for s in holo if lessThanGreaterThanK(s, k)]))

for k in ks:
    count_mero.append(len([s for s in mero if lessThanGreaterThanK(s, k)]))


syn = 0.128765837896
hypo = 0.599908659263
hyper = 0.125228424687
mero = 0.100856732318
holo = 0.0452403458359

max_val = max([syn, hypo, hyper, mero, holo])

print max_val

count_syn = tuple([math.log((1/(syn / max_val)) * s, 10) for s in count_syn])
count_hyper = tuple([math.log((1/(hyper / max_val)) * s, 10) for s in count_hyper])
count_hypo = tuple([math.log((1/(hypo / max_val)) * s, 10) for s in count_hypo])
count_holo = tuple([math.log((1/(holo / max_val)) * s, 10) for s in count_holo])
count_mero = tuple([math.log((1/(mero / max_val)) * s, 10) for s in count_mero])


import matplotlib.pyplot as plt
fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.1

opacity = 0.4
error_config = {'ecolor': '0.3'}


rects1 = plt.bar(index + .15, count_syn, bar_width,
                 alpha=opacity,
                 color='blue',
                 label='synonyms')

rects2 = plt.bar(index + .3, count_hyper, bar_width,
                 alpha=opacity,
                 color='red',
                 label='hypernyms')


rects3 = plt.bar(index + .45, count_hypo, bar_width,
                 alpha=opacity,
                 color='purple',
                 label='hyponyms')


rects4 = plt.bar(index + .6, count_holo, bar_width,
                 alpha=opacity,
                 color='green',
                 label='holonyms')


rects5 = plt.bar(index + .75, count_mero, bar_width,
                 alpha=opacity,
                 color='orange',
                 label='meronyms')


plt.xlabel('K')
plt.ylabel('Log 10 of adjusted count')
plt.title('Semantic Similarity in Word2Vec Compared To WordNet -- Adjusted')
plt.xticks(index + bar_width * 5, ('<200', '200-400', '400-600', '600-800', '>800'))
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='on')

plt.tight_layout()

plt.savefig('Adjusted.png', bbox_inches='tight', pad_inches=.4)