import sys
from nltk.corpus import wordnet as wn
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--out', '-o')
args = vars(parser.parse_args())


def same_stem(one, two):
    if stemmer.stem(one) == stemmer.stem(two):
        return True
    else:
        return False


""" return the intersection of two lists """


def intersect(a, b):
    return set(a) & set(b)


""" return the intersection of two lists """


def union(a, b):
    return set(a).union(set(b))


def get_meronyms(w):
    syns = wn.synsets(w)
    out = []
    for s in syns:
        out.extend([s for s in s.member_meronyms()])
        out.extend([s for s in s.substance_meronyms()])
        out.extend([s for s in s.part_meronyms()])
    return set(out)


def get_holonyms(w):
    syns = wn.synsets(w)
    out = []
    for s in syns:
        out.extend([s for s in s.member_holonyms()])
        out.extend([s for s in s.substance_holonyms()])
        out.extend([s for s in s.part_holonyms()])
    return set(out)


def jaccard(a, b):
    intrsc = len(set(a).intersection(set(b)))
    un = len(set(a).union(set(b)))
    if len(a) == 0 and len(b) == 0:
        return 1
    return float(intrsc)/float(un)


def not_in_wordnet(w):
    syns = wn.synsets(w)
    if len(syns) == 0:
        return True
    return False


def synononymous(worda, wordb):
    return jaccard(wn.synsets(worda), wn.synsets(wordb))


def hyoponomous(a, b):
    synsets_a = wn.synsets(a)

    hyponyms = []
    for a in synsets_a:
        hyponyms.extend(a.hyponyms())

    synsets_b = wn.synsets(b)
    return jaccard(hyponyms, synsets_b)


def hypernomous(a, b):
    synsets_a = wn.synsets(a)

    hypernyms = []
    for a in synsets_a:
        hypernyms.extend(a.hypernyms())

    synsets_b = wn.synsets(b)
    return jaccard(hypernyms, synsets_b)


def meronymous(a, b):
    syn_a = wn.synsets(a)
    syn_b = get_meronyms(b)
    return jaccard(syn_a, syn_b)


def holonymous(a, b):
    syn_a = wn.synsets(a)
    syn_b = get_holonyms(b)
    return jaccard(syn_a, syn_b)
