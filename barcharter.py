"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import re


lines = []


def isNone(s):
    if len(re.findall("^none", s)) > 0:
        return True
    return False


def isSyn(s):
    if len(re.findall("^syn", s)) > 0:
        return True
    return False


def isHypo(s):
    if len(re.findall("^hypo", s)) > 0:
        return True
    return False


def isHyper(s):
    if len(re.findall("^hyper", s)) > 0:
        return True
    return False


def isHolo(s):
    if len(re.findall("^holo", s)) > 0:
        return True
    return False


def isMero(s):
    if len(re.findall("^mero", s)) > 0:
        return True
    return False


def isAnt(s):
    if len(re.findall("^ant", s)) > 0:
        return True
    return False


for line in sys.stdin:
    lines.append(line.replace("\n", ""))

syn = [l for l in lines if isSyn(l)]

print syn

n_groups = 5

count_syn = (20, 35, 30, 35, 27)

count_ant = (25, 32, 34, 20, 25)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, count_syn, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Synonyms')

rects2 = plt.bar(index + bar_width, count_ant, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Antonyms')

plt.xlabel('K')
plt.ylabel('Count')
plt.title('Semantic relations in WordNet')
plt.xticks(index + bar_width, ('1', '<10', '<20', '<50', '<100'))
plt.legend()

plt.tight_layout()
plt.show()