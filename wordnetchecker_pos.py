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
    parts_of_speech = [wn.VERB, wn.ADJ, wn.NOUN, wn.ADV, wn.ADJ_SAT]
    for pos in parts_of_speech:
        syns = wn.synsets(w, pos)
        hypos = []
        hypers = []
        for a in syns:
            hypos.extend(a.hyponyms())
        for a in syns:
            hypers.extend(a.hypernyms())
        mero = get_meronyms(wn.synsets(w, pos))
        holo = get_holonyms(wn.synsets(w, pos))

        if len(mero) > 0:
            merostotal.append((len(mero), pos))
        else:
            merostotal.append((0, pos))

        if len(holo) > 0:
            holototal.append((len(holo), pos))
        else:
            holototal.append((0, pos))

        if len(syns) > 0:
            synstotal.append((len(syns), pos))
        else:
            synstotal.append((0, pos))

        if len(hypers) > 0:
            hyperstotal.append((len(hypers), pos))
        else:
            hyperstotal.append((0, pos))

        if len(hypos) > 0:
            hypostotal.append((len(hypos), pos))
        else:
            hypostotal.append((0, pos))


for pos in parts_of_speech:
    mean_holo = np.mean(np.array([p[0] for p in holototal if p[1] == pos]))
    mean_syn = np.mean(np.array([p[0] for p in synstotal if p[1] == pos]))
    mean_hypo = np.mean(np.array([p[0] for p in hypostotal if p[1] == pos]))
    mean_hyper = np.mean(np.array([p[0] for p in hyperstotal if p[1] == pos]))
    mean_mero = np.mean(np.array([p[0] for p in merostotal if p[1] == pos]))
    mean_of_means = np.mean(np.array([mean_mero, mean_holo, mean_syn, mean_hyper, mean_hypo]))
    holofrac = mean_holo/mean_of_means
    merofrac = mean_mero/mean_of_means
    hypofrac = mean_hypo/mean_of_means
    hyperfac = mean_hyper/mean_of_means
    synfrac = mean_syn/mean_of_means

    print "holofrac {} {}".format(holofrac, pos)
    print "synfrac {} {}".format(synfrac, pos)
    print "hypofrac {} {}".format(hypofrac, pos)
    print "hyperfrac {} {}".format(hyperfac, pos)
    print "merofrac {} {}".format(merofrac, pos)

    if synfrac != 0:
        print "total_syn_counts.txt {} {}".format(1/synfrac, pos)
    else:
        print "total_syn_counts.txt {} {}".format(0, pos)

    if hypofrac != 0:
        print "total_hypo_counts.txt {} {}".format(1/hypofrac, pos)
    else:
        print "total_hypo_counts.txt {} {}".format(0, pos)

    if hyperfac != 0:
        print "total_hyper_counts.txt {} {}".format(1/hyperfac, pos)
    else:
        print "total_hyper_counts.txt {} {}".format(0, pos)

    if merofrac != 0:
        print "total_mero_counts.txt {} {}".format(1/merofrac, pos)
    else:
        print "total_mero_counts.txt {} {}".format(0, pos)

    if holofrac != 0:
        print "total_holo_counts.txt {} {}".format(1/holofrac, pos)
    else:
        print "total_holo_counts.txt {} {}".format(0, pos)
