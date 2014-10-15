from gensim.models import word2vec
from wordnetter import synononymous
from wordnetter import antonymous
from wordnetter import hypernomous
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

try:
    os.remove("results.txt")
except OSError:
    pass

model = word2vec.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
stemmer = SnowballStemmer("english")
parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v', action='count')
parser.add_argument('--out', '-o')
args = vars(parser.parse_args())

verbose = args['verbose'] > 0

def same_stem(one, two):
	if stemmer.stem(one) == stemmer.stem(two):
		return True
	else:
		return False

def printout(line):
    if args['out']:
        with open(args['out'], "a") as results:
            results.write('\n' + line)

def inStopWords(w):
    if s in stopwords.words('english'):
        return True
    return False

words = set(reuters.words())
print len(words)

words = [s for s in words if not inStopWords(s)]
print len(words)

counter = 0
for r in words:
    r = r.encode('ascii', 'ignore')
    try:
        if verbose:
            print "word from vocab {}".format(r)
        n = 0
        sims = model.most_similar(positive=[r], topn=1000)
        for s in sims:
            n = n + 1
            s = (s[0].encode("ascii", 'ignore'), s[1])
            hit = False
            search = True
            if same_stem(s[0], r):
                search = False
                printout(",".join(['same stem', s[0], r, str(s[1]), str(n)]))
            if not_in_wordnet(r):
                search = False
                printout(",".join(['not_in_wordnet', s[0], r, str(s[1]), str(n)]))
            if search:
                if hypernomous(s[0], r) > 0:
                    hit = True
                    printout(",".join(['hyper', s[0], r, str(s[1]), str(n)]))
                if hyoponomous(s[0], r) > 0:
                    hit = True
                    printout(",".join(['hypo', s[0], r, str(s[1]), str(n)]))
                if synononymous(s[0], r):
                    hit = True
                    printout(",".join(['syn', s[0], r, str(s[1]), str(n)]))
                if antonymous(s[0], r):
                    hit = True
                    printout(",".join(['ant', s[0], r, str(s[1]), str(n)]))
                if holonymous(s[0], r):
                    hit = True
                    printout(",".join(['holo', s[0], r, str(s[1]), str(n)]))
                if meronymous(s[0], r):
                    hit = True
                    printout(",".join(['mero', s[0], r, str(s[1]), str(n)]))
                if not hit:
                    printout(",".join(['none', s[0], r, str(s[1]), str(n)]))
    except KeyError:
        print printout(",".join(['KeyError', r]))
        pass