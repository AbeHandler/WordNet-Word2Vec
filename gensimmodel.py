import gensim
import os


class MySentences(object):
     def __init__(self, dirname):
         self.dirname = dirname

     def __iter__(self):
         for fname in os.listdir(self.dirname):
             for line in open(os.path.join(self.dirname, fname)):
                 line = line.lower()
                 yield line.split()


sentences = MySentences('/home/abe-lens-laptop/thesis/Corpus/Contracts') # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences)
model.save("mymodel")