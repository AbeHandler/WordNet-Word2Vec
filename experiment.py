from gensim.models import word2vec
from wordnetter import synononymous
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
    os.remove("textfiles/results.txt")
except OSError:
    pass

model = word2vec.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
stemmer = SnowballStemmer("english")
parser = argparse.ArgumentParser()
parser.add_argument('--out', '-o')
args = vars(parser.parse_args())

def same_stem(one, two):
	if stemmer.stem(one) == stemmer.stem(two):
		return True
	else:
		return False

def printout(line):
    if args['out']:
        writeto = "textfiles/" + args['out']
        with open(writeto, "a") as results:
            results.write('\n' + line)

def inStopWords(w):
    if s in stopwords.words('english'):
        return True
    return False

words = random.sample(set(reuters.words()), 10000)

words = [s for s in words if not inStopWords(s)]

counter = 0
for r in words:
    counter = counter + 1
    r = r.encode('ascii', 'ignore')
    try:
        n = 0
        sims = model.most_similar(positive=[r], topn=200)
        for s in sims:
            n = n + 1
            print "counter: " + str(counter) + "-" + str(n)
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
                hyper = hypernomous(s[0], r)
                hypo = hyoponomous(s[0], r)
                syno = synononymous(s[0], r)
                holo = holonymous(s[0], r)
                mero = meronymous(s[0], r)
                if hyper > 0 and hyper < 1:
                    printout(",".join(['hyper', s[0], r, str(s[1]), str(n), str(hyper)]))
                if hypo > 0 and hypo < 1:
                    printout(",".join(['hypo', s[0], r, str(s[1]), str(n), str(hypo)]))
                if syno > 0 and syno < 1:
                    printout(",".join(['syn', s[0], r, str(s[1]), str(n), str(syno)]))
                if holo > 0 and holo < 1:
                    printout(",".join(['holo', s[0], r, str(s[1]), str(n), str(holo)]))
                if mero > 0 and mero < 1:
                    printout(",".join(['mero', s[0], r, str(s[1]), str(n), str(mero)]))
                if (((hyper + hypo + syno + holo + mero) == 0) or ((hyper + hypo + syno + holo + mero) == 5)):
                    printout(",".join(['none', s[0], r, str(s[1]), str(n)]))
    except KeyError:
        print printout(",".join(['KeyError', r]))
        pass