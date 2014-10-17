from gensim.models import word2vec
from wordnetter import get_meronyms
from wordnetter import get_holonyms
from wordnetter import not_in_wordnet
from wordnetter import holonymous
from wordnetter import meronymous
from wordnetter import hyoponomous
from nltk.corpus import reuters
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import random
import argparse
import os

words = random.sample(set(reuters.words()), 1000)

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