import gensim
import os
import hashlib
import sys
import pickle
import numpy as np
from nltk.stem.lancaster import LancasterStemmer
st = LancasterStemmer()


def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'r') as f:
        return pickle.load(f)


class MySentences(object):
     def __init__(self, dirname):
         self.dirname = dirname

     def __iter__(self):
         for fname in os.listdir(self.dirname):
             for line in open(os.path.join(self.dirname, fname)):
                 yield ([i for i in line.decode('ascii', 'ignore').lower().split()])

relations = []

for line in sys.stdin:
	relations.append(line.replace("\n", ""))

location = sys.argv[1]

fn = location.replace("/", "") + "model"

if not os.path.isfile(fn):
    sentences = MySentences(location) # a memory-friendly iterator
    model = gensim.models.Word2Vec(sentences, min_count=10)
    model.save(fn)

model = gensim.models.Word2Vec.load(fn)

for r1 in relations:
	for r2 in relations:
		try:
			print str(model.n_similarity(r1.split(" "),r2.split(" "))) + "\t" + " ".join(r1.split(" ")) + "\t" + " ".join(r2.split(" "))
		except:
			pass

'''
array = []
numbers={}
words={}
counter = 0

for w in model.vocab.keys():
	numbers[w] = counter
	words[counter] = w
	counter = counter + 1

save_obj(words, "words")
distances = np.zeros((counter, counter))

for i in range(counter):
	for j in range(counter):
		if model.similarity(words[i], words[j]) > 0:
			distances[i,j] = model.similarity(words[i], words[j])
		else:
			distances[i,j] = 100000

words = load_obj("words")

for i in range(100):
	ret = [i[0] for i in np.where(distances == distances.min())]
	print distances[ret[0]][ret[1]]
	print words[ret[0]] + "," + words[ret[1]]
	distances[ret[0]][ret[1]] = 100000

print model.n_similarity(['man', 'woman'], ['green', 'cow'])

#print distances

#print np.nanargmin(distances)
#print np.nanargmin(distances)

#distances.dump(fn + ".dat")
#distances = np.load(fn + ".dat")
'''