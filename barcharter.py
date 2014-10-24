"""
Bar chart to show different relations at different k
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


with open("textfiles/results.txt") as results:
    for line in results.readlines():
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
stem = [l for l in lines if isIt(l, "^same stem")]

n_groups = 5

ks = [40, 80, 120, 160, 200]
floor = {}
floor[40] = 0
floor[80] = 40
floor[120] = 80
floor[160] = 120
floor[200] = 160

count_syn = []
count_hyper = []
count_hypo = []
count_holo = []
count_stem = []
count_mero = []
base = 10

for k in ks:
    count_syn.append(math.log(len([s for s in syn if lessThanGreaterThanK(s, k)]), base))

for k in ks:
    count_hyper.append(math.log(len([s for s in hyper if lessThanGreaterThanK(s, k)]), base))

for k in ks:
    count_hypo.append(math.log(len([s for s in hypo if lessThanGreaterThanK(s, k)]), base))

for k in ks:
    count_holo.append(math.log(len([s for s in holo if lessThanGreaterThanK(s, k)]), base))

for k in ks:
    count_mero.append(math.log(len([s for s in mero if lessThanGreaterThanK(s, k)]), base))

for k in ks:
    count_stem.append(math.log(len([s for s in stem if lessThanGreaterThanK(s, k)]), base))


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
plt.ylabel('log 10 of count')
plt.title('Semantic Similarity in Word2Vec Compared To WordNet')
plt.xticks(index + bar_width * 4, ('<40', '40-80', '80-120', '120-160', '160-200'))
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.savefig('All.png', bbox_inches='tight', pad_inches=.4)