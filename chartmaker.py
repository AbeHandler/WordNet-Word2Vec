#!/usr/bin/env python
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import sys

arr = []

kind = sys.argv[1]


for line in sys.stdin:
    try:
        arr.append(int(line))
    except ValueError:
        pass

x = np.array(arr)

#print x.shape

# the histogram of the data
n, bins, patches = plt.hist(x, color='#BD7CE8', alpha=0.4)

plt.xlabel('k')
plt.ylabel('Count')
#plt.title(kind.replace("_", " "))
plt.grid(True)

plt.savefig(kind+'.png', bbox_inches='tight', pad_inches=.4)