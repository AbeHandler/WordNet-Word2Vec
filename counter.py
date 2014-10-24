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
not_in_wordnet = [l for l in lines if isIt(l, "^not_in_wordnet")]
key_error = [l for l in lines if isIt(l, "^KeyError")]

ks = [40, 80, 120, 160, 200]

floor = {}
floor[40] = 0
floor[80] = 40
floor[120] = 80
floor[160] = 120
floor[200] = 160

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

print "Key Error &" + str(len(key_error))
