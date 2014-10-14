from gensim.models import word2vec
from wordnetter import synononymous
from wordnetter import antonymous
from wordnetter import hypernomous
from wordnetter import not_in_wordnet
from wordnetter import holonymous
from wordnetter import meronymous
from nltk.corpus import reuters
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import random
import argparse

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

randoms = random.sample(reuters.words(), 100000)
counter = 0
for r in randoms:
    r = r.encode('ascii', 'ignore')
    try:
        if verbose:
            print "word from vocab {}".format(r)
        n = 1
        while same_stem(model.most_similar(positive=[r], topn=n).pop()[0], r):
            if verbose:
                print "same stem {}".format(model.most_similar(positive=[r],
                                            topn=n).pop()[0])
                print 'incrementing n'
            n = n + 1
        sims = [model.most_similar(positive=[r], topn=n).pop()]
        for s in sims:
            s = (s[0].encode("ascii", 'ignore'), s[1])
            if s in stopwords.words('english'):
                printout(",".join(['stop', s[0], r]))
            elif not_in_wordnet(r):
                printout(",".join(['not_in_wordnet', s[0], r]))
            # elif hypernomous(s[0],r):
            #    print 'hyp'
            #    printout(",".join(['hyp',s[0],r]))
            elif synononymous(s[0], r):
                printout(",".join(['syn', s[0], r]))
            elif antonymous(s[0], r):
                printout(",".join(['ant', s[0], r]))
            elif holonymous(s[0], r):
                printout(",".join(['holo', s[0], r]))
            elif meronymous(s[0], r):
                printout(",".join(['mero', s[0], r]))
            else:
                printout(",".join(['none', s[0], r]))
    except KeyError:
        print printout(",".join(['KeyError', r]))
        pass