import numpy as np
import sys
import re
import math
import numpy as np
import matplotlib.pyplot as plt

increments = np.linspace(0, 1, num=1000)

syns = []
meros = []
hypers = []
hypos = []
stems = []
holos = []
increments = []

with open("textfiles/counter_cumulative.txt") as results:
    for line in results.readlines():
        line = line.replace("\n", "")
        try:
            i, syn, mero, holo, hyper, hypo, stem = line.split(",")
            increments.append(i)
            syns.append(syn)
            holos.append(holo)
            meros.append(mero)
            hypers.append(hyper)
            hypos.append(hypo)
            stems.append(stem)
        except:
            print line



plt.plot(increments, stems, label="Same stems")
plt.plot(increments, hypers, label="Hypernyms")
plt.plot(increments, syns, label="Synonyms")
plt.plot(increments, hypos, label="Hyponyms")
plt.plot(increments, meros, label="Meronyms")
plt.plot(increments, holos, label="Holonyms")

plt.xlabel('Cosine distance')
plt.ylabel('Frequency')
plt.legend(loc="2")

plt.savefig('total_by_semantic_cumultiave.png', bbox_inches='tight', pad_inches=.4)