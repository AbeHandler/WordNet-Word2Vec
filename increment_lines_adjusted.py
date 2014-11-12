import numpy as np
import sys
import re
import math
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

lowess = sm.nonparametric.lowess

increments = np.linspace(0, 1, num=1000)


#these ratios come from wordnetcheck
synratio = 1.38035667709
hyporatio = 0.358620245857
hyperratio = 1.44090670617
meroratio = 1.83191715951
holoratio = 4.04529267639

syns = []
meros = []
hypers = []
hypos = []
stems = []
holos = []
increments = []

with open("textfiles/increments.txt") as results:
    for line in results.readlines():
        try:
            line = line.replace("\n", "")
            top, bottom, syn, mero, holo, hyper, hypo, stem, none = line.split(",")
            increments.append((float(top) + float(bottom)) / 2)
            syns.append(int(syn))
            holos.append(int(holo))
            meros.append(int(mero))
            hypers.append(int(hyper))
            hypos.append(int(hypo))
            stems.append(int(stem))
        except ValueError:
            pass

syns = np.array(syns)

alpha = .4

hypers = [h * hyperratio for h in hypers]
syns = [h * synratio for h in syns]
meros = [h * meroratio for h in meros]
holos = [h * holoratio for h in holos]
hypos = [h * hyporatio for h in hypos]


plt.scatter(increments, hypers, color="purple", alpha=alpha, label="Hypernyms")
plt.scatter(increments, syns, color="green", alpha=alpha, label="Synonyms")
plt.scatter(increments, hypos, color="yellow", alpha=alpha, label="Hyponyms")
plt.scatter(increments, meros, color="orange", alpha=alpha, label="Meronyms")
plt.scatter(increments, holos, color="blue", alpha=alpha, label="Holonyms")

plt.xlabel('Cosine distance')
plt.ylabel('Count')
plt.legend(loc=2)
plt.xlim(0,1)
plt.ylim(0,400)

plt.savefig('increment_lines_adjusted.png', bbox_inches='tight', pad_inches=.4)