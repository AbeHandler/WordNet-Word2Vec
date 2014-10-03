import gensim
import os
import hashlib
import sys
import numpy as np
from nltk.stem.lancaster import LancasterStemmer
st = LancasterStemmer()

class MySentences(object):
     def __init__(self, dirname):
         self.dirname = dirname

     def __iter__(self):
         for fname in os.listdir(self.dirname):
             for line in open(os.path.join(self.dirname, fname)):
                 yield ([st.stem(i) for i in line.decode('ascii', 'ignore').lower().split()])



location = sys.argv[1]

fn = location.replace("/", "") + "model"

if not os.path.isfile(fn):
    sentences = MySentences(location) # a memory-friendly iterator
    model = gensim.models.Word2Vec(sentences)
    model.save(fn)

model = gensim.models.Word2Vec.load(fn)

array = []
numbers={}
words={}
counter = 0

for w in model.vocab.keys():
	numbers[w] = counter
	words[counter] = w
	counter = counter + 1

distances = np.zeros((counter, counter))

for i in range(counter):
	for j in range(counter):
		distances[i,j] = model.similarity(words[i], words[j])

ret = [i[0] for i in np.where(distances == distances.max())]

print words[ret[0]]
print words[ret[1]]

#print distances

#print np.nanargmin(distances)
#print np.nanargmin(distances)

distances.dump(fn + ".dat")
distances = np.load(fn + ".dat")