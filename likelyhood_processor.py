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


def isIt(p, s):
    if len(re.findall(p, s)) > 0:
        return True
    return False


for line in sys.stdin:
    lines.append(line.replace("\n", ""))


def is_k(l, k, typeParam=None):
    if len(l) == 0:
        return False
    try:
        if not typeParam:
            if (int(l.split(",")[4]) == k):
                return True
            else:
                return False
        else:
            if (int(l.split(",")[4]) == k) and isIt("^" + typeParam, l):
                return True
        return False
    except ValueError:
        return False


types = ['syn', 'hypo', 'hyper', 'holo', 'mero']

totals = {}

for k in ks:
    totals[k] = float(sum(1 for l in lines if is_k(l, k)))

for t in types:
    for k in ks:
        type_hits = float(sum(1 for l in lines if is_k(l, k, t)))
        total_hits = totals[k]
        with open(t + ".likelyhood", "a") as myfile:
            myfile.write(",".join([str(k), str(syn_hits/total_hits)])+"\n")
