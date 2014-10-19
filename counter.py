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
stem = [l for l in lines if isIt(l, "^same stem")]
not_in_wordnet = [l for l in lines if isIt(l, "^not_in_wordnet")]

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
count_stem = []
count_mero = []
count_not_in_wordnet = []
base = 10


def print_line(start, array):
    for k in ks:
        start = start + str(len([s for s in array if lessThanGreaterThanK(s, k)])) + " & "
    print start.strip(" & ") + "\\" + "\\" + "  \hline"

print_line("Synonomy &", syn)

print_line("Hyponomy &", hypo)

print_line("Hypernomy &", hyper)

print_line("Holonomy &", holo)

print_line("Meronomy &", mero)

print_line("Same stem &", stem)

print_line("Not in wordnet &", not_in_wordnet)
