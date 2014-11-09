"""
Makes the total count chart
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib
from matplotlib.ticker import FuncFormatter
import Image

holo = []
mero = []
hyper = []
syn = []
hypo = []

with open("textfiles/total_adjusted_holo_counts.txt") as results:
    for line in results.readlines():
        holo.append(int(line.replace("\n", "").split(",")[1]))

with open("textfiles/total_adjusted_mero_counts.txt") as results:
    for line in results.readlines():
        mero.append(int(line.replace("\n", "").split(",")[1]))

with open("textfiles/total_adjusted_hyper_counts.txt") as results:
    for line in results.readlines():
        hyper.append(int(line.replace("\n", "").split(",")[1]))

with open("textfiles/total_adjusted_hypo_counts.txt") as results:
    for line in results.readlines():
        hypo.append(int(line.replace("\n", "").split(",")[1]))

with open("textfiles/total_adjusted_syn_counts.txt") as results:
    for line in results.readlines():
        syn.append(int(line.replace("\n", "").split(",")[1]))

holo = np.array(holo[:50])
mero = np.array(mero[:50])
hyper = np.array(hyper[:50])
hypo = np.array(hypo[:50])
syn = np.array(syn[:50])

x = np.arange(1, len(syn) + 1, 1)

print x[0]

alpha = .4
plt.title("Count of relations by k (log-log)")

plt.scatter(x, syn, alpha=.4, label='Synonyms', marker="x", color="grey")
plt.scatter(x, hyper, alpha=.4, label='Hypernyms', marker="*")
plt.scatter(x, holo, alpha=.4, label='Holonyms', marker="+")
plt.scatter(x, hypo, alpha=.4, label='Hyponyms', marker=".")
plt.scatter(x, mero, alpha=.4, label='Meronyms', marker="d")

plt.xlabel("log k")
plt.ylabel("log Count")

plt.tight_layout()
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.loglog()
plt.minorticks_off()
plt.autoscale()
plt.ylim(0, 5000)
plt.xlim(0, 50)
plt.savefig('total_adjusted.png', bbox_inches='tight', pad_inches=.4)
Image.open('total_adjusted.png').convert('L').save('total_adjusted_bw.png')