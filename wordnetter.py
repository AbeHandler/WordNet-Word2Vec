import sys
from nltk.corpus import wordnet as wn
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")


def get_synsets(word, pos):
    syns = wn.synsets(word, pos)
    return syns


def same_stem(one, two):
    if stemmer.stem(one) == stemmer.stem(two):
        return True
    else:
        return False


""" return the intersection of two lists """


def intersect(a, b):
    return set(a) & set(b)


""" return the union of two lists """


def union(a, b):
    return set(a).union(set(b))


def get_meronyms(syns):
    out = []
    for s in syns:
        out.extend([s for s in s.member_meronyms()])
        out.extend([s for s in s.substance_meronyms()])
        out.extend([s for s in s.part_meronyms()])
    return set(out)


def get_holonyms(syns):
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


def not_in_wordnet(w, pos):
    syns = wn.synsets(w, pos)
    if len(syns) == 0:
        return True
    return False


def synononymous(worda, wordb, pos):
    syns_a = get_synsets(worda, pos)
    syns_b = get_synsets(wordb, pos)
    return jaccard(syns_a, syns_b)


def hyoponomous(a, b, pos):
    synsets_a = wn.synsets(a, pos)

    hyponyms = []
    for a in synsets_a:
        hyponyms.extend(a.hyponyms())

    synsets_b = wn.synsets(b, pos)
    return jaccard(hyponyms, synsets_b)


def hypernomous(a, b, pos):
    synsets_a = get_synsets(a, pos)

    hypernyms = []
    for a in synsets_a:
        hypernyms.extend(a.hypernyms())

    synsets_b = wn.synsets(b, pos)
    return jaccard(hypernyms, synsets_b)


def meronymous(a, b, pos):
    syn_a = wn.synsets(a, pos)
    syn_b = get_meronyms(wn.synsets(b, pos))
    return jaccard(syn_a, syn_b)


def holonymous(a, b, pos):
    syn_a = wn.synsets(a, pos)
    syn_b = get_holonyms(wn.synsets(b, pos))
    return jaccard(syn_a, syn_b)
