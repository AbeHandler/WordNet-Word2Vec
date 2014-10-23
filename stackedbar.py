#!/usr/bin/env python
# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

syn_counts = []
holo_counts = []
mero_counts = []
hyper_counts = []
hypo_counts = []

with open("textfiles/total_syn_counts.txt", "r") as total:
	for l in total.readlines():
		syn_counts.append(int(l.strip("\n").split(",")[1]))

with open("textfiles/total_holo_counts.txt", "r") as total:
	for l in total.readlines():
		holo_counts.append(int(l.strip("\n").split(",")[1]))

with open("textfiles/total_mero_counts.txt", "r") as total:
	for l in total.readlines():
		mero_counts.append(int(l.strip("\n").split(",")[1]))

with open("textfiles/total_hyper_counts.txt", "r") as total:
	for l in total.readlines():
		hyper_counts.append(int(l.strip("\n").split(",")[1]))

with open("textfiles/total_hypo_counts.txt", "r") as total:
	for l in total.readlines():
		hypo_counts.append(int(l.strip("\n").split(",")[1]))

N = 100
syns   = tuple(syn_counts[:100])
holos = tuple(holo_counts[:100])
meros = tuple(mero_counts[:100])
hypers = tuple(hyper_counts[:100])
hypos = tuple(hyper_counts[:100])

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence


p1 = plt.bar(ind, holos,   width, color='r')
p2 = plt.bar(ind, syns, width, color='y', bottom=holos)
p3 = plt.bar(ind, meros, width, color='g', bottom=syns)
p4 = plt.bar(ind, hypers, width, color='orange', bottom=meros)
p5 = plt.bar(ind, hypos, width, color='pink', bottom=hypers)


plt.ylabel('Count')
plt.title('Wordnet relations uncovered by Word2Vec')
plt.legend( (p1[0], p2[0], p3[0], p4[0], p5[5]), ('Holonyms', 'Synonyms', 'Meronyms', 'Hyernyms','Hyernyms') )

plt.show()