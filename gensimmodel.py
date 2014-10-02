import gensim
import os
import hashlib
import numpy as np

class MySentences(object):
     def __init__(self, dirname):
         self.dirname = dirname

     def __iter__(self):
         for fname in os.listdir(self.dirname):
             for line in open(os.path.join(self.dirname, fname)):
                 line = line.lower()
                 yield line.split()


if not os.path.isfile("mymodel"):
    sentences = MySentences('/home/abe-lens-laptop/thesis/Corpus/Contracts') # a memory-friendly iterator
    model = gensim.models.Word2Vec(sentences)
    model.save("mymodel")

model = gensim.models.Word2Vec.load("mymodel")

array = []
keys={}


def processWord(word):
	array.append(model[word])
	b = model[word].view(np.uint8)
	b = hashlib.sha1(b).hexdigest()
	keys[b] = word


for w in model.vocab.keys():
	processWord(w)


myarray = np.asarray(array)


import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from pylab import *

# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4, random_state=0)
X = StandardScaler().fit_transform(X) 

xx, yy = zip(*X)
scatter(xx,yy)

db = DBSCAN(eps=3, min_samples=3).fit(myarray)
core_samples = db.core_sample_indices_
labels = db.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

clusters = [myarray[labels == i] for i in xrange(n_clusters_)]

for c in clusters:
	for e in c:
		b = e.view(np.uint8)
		b = hashlib.sha1(b).hexdigest()
		print keys[b]