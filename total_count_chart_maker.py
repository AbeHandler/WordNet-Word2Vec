"""
Makes the total count chart
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib
from matplotlib.ticker import FuncFormatter


holo = []
mero = []
hyper = []
syn = []
hypo = []

with open("textfiles/total_count_scatter_holo.txt") as results:
    for line in results.readlines():
        holo.append(int(line.replace("\n", "")))

with open("textfiles/total_count_scatter_mero.txt") as results:
    for line in results.readlines():
        mero.append(int(line.replace("\n", "")))

with open("textfiles/total_count_scatter_hyper.txt") as results:
    for line in results.readlines():
        hyper.append(int(line.replace("\n", "")))

with open("textfiles/total_count_scatter_hypo.txt") as results:
    for line in results.readlines():
        hypo.append(int(line.replace("\n", "")))

with open("textfiles/total_count_scatter_syn.txt") as results:
    for line in results.readlines():
        syn.append(int(line.replace("\n", "")))

holo = np.array(holo)
mero = np.array(mero)
hyper = np.array(hyper)
hypo = np.array(hypo)
syn = np.array(syn)

def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(int(round(100 * y)))
    print s

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] == True:
        return s + r'$\%$'
    else:
        return s + '%'

#formatter = FuncFormatter(to_percent)

# Set the formatter
#plt.gca().yaxis.set_major_formatter(formatter)


# Fake data
x = np.arange(0, len(syn), 1)

area = 15 # 0 to 15 point radiuses

alpha = .4
plt.title("Count of relations by k")
plt.ylim(0, 350)
plt.xlim(0,200)
plt.scatter(x, syn, alpha=.4, label='Synonyms', color="blue")
plt.scatter(x, hyper, alpha=.4, label='Hypernyms', color="red")
plt.scatter(x, holo, alpha=.4, label='Holonyms', color="green")
plt.scatter(x, hypo, alpha=.4, label='Hyponyms', color="purple")
plt.scatter(x, mero, alpha=.4, label='Meronyms', color="orange")


plt.legend()
plt.xlabel("k")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig('total.png', bbox_inches='tight', pad_inches=.4)