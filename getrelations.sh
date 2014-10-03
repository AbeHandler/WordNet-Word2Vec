cat reutersrelations.txt | \
python relation_filterer.py | \
python gensimmodel.py test | \
python relation_semanticprocessor.py | \
uniq > relations_sorted.txt