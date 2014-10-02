import gensim
import os
import hashlib
import sys
import numpy as np

class MySentences(object):
     def __init__(self, dirname):
         self.dirname = dirname

     def __iter__(self):
         for fname in os.listdir(self.dirname):
             for line in open(os.path.join(self.dirname, fname)):
                 line = line.lower()
                 yield line.split()


location = "/home/abe-lens-laptop/nltk_data/corpora/gutenberg"

fn = location.replace("/", "")

if not os.path.isfile(fn):
    sentences = MySentences(location) # a memory-friendly iterator
    model = gensim.models.Word2Vec(sentences)
    model.save(fn)

model = gensim.models.Word2Vec.load(fn)

print len(model.vocab)
array = []
numbers={}
words={}
counter = 0

for w in model.vocab.keys():
	numbers[w] = counter
	words[counter] = w
	counter = counter + 1

distances = np.zeros((counter, counter))

print model.similarity("man", "woman")
print model.similarity("man", "horse")

for i in range(counter):
	print counter
	for j in range(counter):
		distances[i,j] = model.similarity(words[i], words[i])

print distances[numbers["man"], numbers["woman"]]

mat.dump("my_matrix.dat")
mat2 = numpy.load("my_matrix.dat")

'''
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from pylab import *

Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4, random_state=0)
X = StandardScaler().fit_transform(X) 

xx, yy = zip(*X)
scatter(xx,yy)

print 'running scan'
db = DBSCAN(eps=.05, min_samples=5).fit(myarray)


core_samples = db.core_sample_indices_
labels = db.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

clusters = [myarray[labels == i] for i in xrange(n_clusters_)]

for c in clusters:
	print "###"
	for e in c:
		b = e.view(np.uint8)
		b = hashlib.sha1(b).hexdigest()
		sys.stdout.write(numbers[b] + " ")
'''