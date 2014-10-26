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

lines = []

ks = range(1, 200)

ks = []

totals = tuple(open("total_k_counts.txt", "r"))

k_dict = {}

for t in totals:
    t = t.strip("\n").split(",")
    k_dict[int(t[0])] = int(t[1])

for line in sys.stdin:
    spl = [l.strip() for l in line.split("-")]
    k = float(k_dict[int(spl[0])])
    count = float(spl[1])
    if count == 0:
        print count
    else:
        print count / k




#print totals
'''
for t in types:
    for k in ks:
        print t
        print k
        type_hits = float(sum(1 for l in lines if is_k(l, k, t)))
        print type_hits
        total_hits = totals[k]
        with open(t + ".likelyhood", "a") as myfile:
            myfile.write(",".join([str(k), str(syn_hits/total_hits)])+"\n")
'''
