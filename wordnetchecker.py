from nltk.corpus import wordnet as wn
from nltk.corpus import reuters
from wordnetter import get_meronyms
from wordnetter import get_holonyms
import random

import numpy as np
import sys
import re
import math
words = random.sample(set(reuters.words()), 10000)

holototal = []
synstotal = []
hyperstotal = []
hypostotal = []
merostotal = []

np.array(holototal)

for w in words:
    syns = wn.synsets(w)
    hypos = []
    hypers = []
    for a in syns:
        hypos.extend(a.hyponyms())
    for a in syns:
        hypers.extend(a.hypernyms())
    mero = get_meronyms(w)
    holo = get_holonyms(w)
    if len(mero) > 0:
        merostotal.append(len(mero))
    if len(holo) > 0:
        holototal.append(len(holo))
    if len(syns) > 0:
        synstotal.append(len(syns))
    if len(hypers) > 0:
        hyperstotal.append(len(hypers))
    if len(hypos) > 0:
        hypostotal.append(len(hypos))

mean_holo = np.mean(np.array(holototal))
mean_syn = np.mean(np.array(synstotal))
mean_hypo = np.mean(np.array(hypostotal))
mean_hyper = np.mean(np.array(hyperstotal))
mean_mero = np.mean(np.array(merostotal))

'''
print "holo {}".format(mean_holo)
print "syn {}".format(mean_syn)
print "hypo {}".format(mean_hypo)
print "hyper {}".format(mean_hyper)
print "mero {}".format(mean_mero)
'''

mean_of_means = np.mean(np.array([mean_mero, mean_holo, mean_syn, mean_hyper, mean_hypo]))

#print "mean of means {}".format(mean_of_means)

holofrac = mean_holo/mean_of_means
merofrac = mean_mero/mean_of_means
hypofrac = mean_hypo/mean_of_means
hyperfac = mean_hyper/mean_of_means
synfrac = mean_syn/mean_of_means

'''
print "holofrac {}".format(holofrac)
print "synfrac {}".format(synfrac)
print "hypofrac {}".format(hypofrac)
print "hyperfrac {}".format(hyperfac)
print "merofrac {}".format(merofrac)
'''

print "total_syn_counts.txt {}".format(1/synfrac)
print "total_hypo_counts.txt {}".format(1/hypofrac)
print "total_hyper_counts.txt {}".format(1/hyperfac)
print "total_mero_counts.txt {}".format(1/merofrac)
print "total_holo_counts.txt {}".format(1/holofrac)
