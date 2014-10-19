from nltk.corpus import wordnet as wn
from nltk.corpus import reuters
from wordnetter import get_meronyms
from wordnetter import get_holonyms
import random

import numpy as np
import sys
import re
import math
words = random.sample(set(reuters.words()), 1000)

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

#print "holo {}".format(mean_holo)
#print "syn {}".format(mean_syn)
#print "hypo {}".format(mean_hypo)
#print "hyper {}".format(mean_hyper)
#print "mero {}".format(mean_mero)

sum_of_means = np.sum([mean_holo, mean_syn, mean_hypo, mean_hyper, mean_mero])

print "sum {}".format(str(sum_of_means))
print "syn {}".format(str(mean_syn/sum_of_means))
print "hypo {}".format(str(mean_hypo/sum_of_means))
print "hyper {}".format(str(mean_hyper/sum_of_means))
print "mero {}".format(str(mean_mero/sum_of_means))
print "holo {}".format(str(mean_holo/sum_of_means))

print mean_holo/sum_of_means + mean_mero/sum_of_means+ \
    mean_hypo/sum_of_means+ mean_hyper/sum_of_means + mean_syn/sum_of_means
