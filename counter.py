import numpy as np
import sys
import re
import math
import os
import numpy as np

increments = np.linspace(0, 1, num=1000)

def isIt(s, p):
    if len(re.findall(p, s)) > 0:
        return True
    return False

def lessThanTheshold(l, bottom, top):
    try:
        valu = float(l.split(",")[4])
        top = np.asscalar(top)
        bottom = np.asscalar(bottom)
        if (valu < top and valu > bottom):
            return True
        return False
    except IndexError:
        return False
    except ValueError:
        return False

lines = []

with open("textfiles/results.txt") as results:
    for line in results.readlines():
        line = line.replace("\n", "")
        lines.append(line)

try:
    os.remove("textfiles/increments.txt")
except OSError:
    pass

for i in range(1, len(increments)):
    top = increments[i]
    bottom = increments[i-1]
    writeto = "textfiles/increments.txt"
    syn = 0
    mero = 0
    holo = 0
    hyper = 0
    hypo = 0
    stem = 0
    none = 0
    for line in lines:
        if lessThanTheshold(line, bottom, top):
            if isIt(line, "^syn"):
                syn += 1
            if isIt(line, "^mero"):
                mero += 1
            if isIt(line, "^holo"):
                holo += 1
            if isIt(line, "^hyper"):
                hyper += 1
            if isIt(line, "^hypo"):
                hypo += 1
            if isIt(line, "^same stem"):
                stem += 1
            if isIt(line, "^none"):
                none += 1
    out = ",".join([str(top), str(bottom), str(syn), str(mero), str(holo), str(hyper), str(hypo), str(stem), str(none)])
    with open(writeto, "a") as results:
        results.write('\n' + out)