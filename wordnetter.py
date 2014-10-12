import sys
from nltk.corpus import wordnet as wn
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v', action='count')
parser.add_argument('--out', '-o')
args = vars(parser.parse_args())

print args
verbose = args['verbose'] > 0

if args['out']:
    with open(args['out'], "a") as results:
        results.write("appended text")

def same_stem(one, two):
	if stemmer.stem(one) == stemmer.stem(two):
		return True
	else:
		return False

#print same_stem("run", "running")


def getAntonyms(ss):
	for l in ss.lemmas:
		if len(l.antonyms()) > 0:
			return [stemmer.stem(l.name) for l in l.antonyms()]
		return []

def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))

def translatePOS(pos):
	if pos == "verb":
		return wn.VERB
	return None


def getSynsets(word, pos=None):
	if pos:
		return wn.synsets(word, pos=pos)
	else:
		return wn.synsets(word)


'''
includes antonyms
'''
def synononymish(a, b, pos=None):
	total_a_words = []
	total_b_words = []

	synsets_a = getSynsets(a,pos)
	for ss in synsets_a:
		antonyms_a = getAntonyms(ss)
		synonyms_a = ss.lemma_names()
		total_a_words.extend(antonyms_a)
		total_a_words.extend(synonyms_a)
	synsets_b = getSynsets(b, pos)
	for ss in synsets_b:
		antonyms_b = getAntonyms(ss)
		synonyms_b = ss.lemma_names()
		total_b_words.extend(antonyms_b)
		total_b_words.extend(synonyms_b)
	intersection = intersect(total_a_words, total_b_words)
	if len(intersection)>0:
		return True
	return False


def synononymous(a, b, pos=None, verbose=None):
	synsets_a = getSynsets(a,pos)
	synsets_b = getSynsets(b, pos)
	intersection = intersect(synsets_a, synsets_b)
	if verbose:
		for i in intersection:
			print i.definition()
			print i.examples()
	if len(intersection)>0:
		return True
	return False

def antonymous(a, b):
	synsets_a = getSynsets(a)
	total_antonyms_a = []

	for a in synsets_a:
		total_antonyms_a.extend(getAntonyms(a))
	if stemmer.stem(b) in total_antonyms_a:
		return True
	return False

print antonymous('open', 'closed')
'''
for ss in wn.synsets("bad"): # Each synset represents a diff concept.
	antonyms = getAntonyms(ss)
	synonyms = ss.lemma_names()
	#returns synets
	hypernyms = ss.hypernyms()
	hyponyms = ss.hyponyms()
	member_holonyms = ss.member_holonyms()
	substance_holonyms = ss.substance_holonyms()
	instance_hyponyms = ss.instance_hyponyms()
	part_holonyms = ss.part_holonyms()
	member_meronyms = ss.member_meronyms()
	substance_meronyms = ss.substance_meronyms()
	part_meronyms = ss.part_meronyms()

	total = antonyms + synonyms + hypernyms  + hyponyms  + member_holonyms + substance_holonyms + instance_hyponyms \
	+ part_holonyms + member_meronyms + substance_meronyms + part_meronyms
	total = [t for t in total if isinstance(t, unicode)]

	print set(total)
'''