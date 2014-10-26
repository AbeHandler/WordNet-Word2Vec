###An empirical study of semantic similarity in WordNet and Word2Vec
#####Abram Handler | Master's Thesis: University of New Orleans, Fall 2014

####Abstract
Google's unsupervised Word2Vec system attempts to determine the semantic distance between words at web scale. This paper performs an empirical analysis of Word2Vec's determinations by comparing them to WordNet, a well-known, human-curated lexical database. It finds that Word2Vec tends to uncover more of certain types of semantic relations than others, with Word2Vec returning more hypernyms than synonyms followed by meronyms, hyponyms and holonyms. Moreover, it shows the likelihood that neighbors separated by distance k in Word2Vec are semantically related in WordNet.

####Files

`main.sh` Primary driver for the application. Use ./main.sh to run the experiment and generate results

`experiment.py` Runs the experiment

`process_results.sh` Calculates totals used to show final results

`tester.py` Some unit tests

`wordnetchecker.py` Finds the average numbers of each relation in WordNet

####Dependencies

* **NLTK 3.0.0**
* **Gensim 0.10.2**
* **numpy 1.9.0**
* **Word vectors from Google news corpus** [downloadable here](https://code.google.com/p/word2vec/).


