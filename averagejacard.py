import re
import numpy as np

syns = []
meros = []
hypers = []
hypos = []
stems = []
holos = []
increments = []

lines = []

def isIt(s, p):
    if len(re.findall(p, s)) > 0:
        return True
    return False

with open("textfiles/results.txt") as results:
    for line in results.readlines():
        line = line.replace("\n", "")
        if isIt(line, "^syn"):
            relation, cos, word1, word2, cos2, k, jacard = line.split(",")
            syns.append(float(jacard))
        if isIt(line, "^mero"):
            relation, cos, word1, word2, cos2, k, jacard = line.split(",")
            meros.append(float(jacard))
        if isIt(line, "^holo"):
            relation, cos, word1, word2, cos2, k, jacard = line.split(",")
            holos.append(float(jacard))
        if isIt(line, "^hyper"):
            relation, cos, word1, word2, cos2, k, jacard = line.split(",")
            hypers.append(float(jacard))
        if isIt(line, "^hypo"):
            relation, cos, word1, word2, cos2, k, jacard = line.split(",")
            hypos.append(float(jacard))

print "syns {}".format(np.average(syns))
print "holos {}".format(np.average(holos))
print "hypers {}".format(np.average(hypers))
print "hypos {}".format(np.average(hypos))
print "meros {}".format(np.average(meros))
