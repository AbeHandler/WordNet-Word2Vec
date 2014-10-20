cat results.txt | egrep '^syn,' | awk -F","  '{print $5}' | sort -n > syndist.txt
cat results.txt | egrep '^holo,' | awk -F","  '{print $5}' | sort -n > holdist.txt
cat results.txt | egrep '^mero,' | awk -F","  '{print $5}' | sort -n > merdist.txt
cat results.txt | egrep '^none,' | awk -F","  '{print $5}' | sort -n > none.txt
cat results.txt | egrep '^hyper,' | awk -F","  '{print $5}' | sort -n  > hyperdist.txt
cat results.txt | egrep '^hypo,' | awk -F","  '{print $5}' | sort -n > hypodist.txt
cat results.txt | egrep '^same' | awk -F","  '{print $5}' > samestem.txt


cat samestem.txt | python chartmaker.py Same_stem
cat none.txt | python chartmaker.py No_Relation
cat merdist.txt | python chartmaker.py Meronym_Distance
cat holdist.txt | python chartmaker.py Holonym_Distance
cat syndist.txt | python chartmaker.py Synonym_Distance
cat hyperdist.txt | python chartmaker.py Hypernym_Distance
cat hypodist.txt | python chartmaker.py Hyponym_Distance
cat results.txt | python barcharter.py Bar

cat results.txt | python averagejacard.py 
cat results.txt | python counter.py

cat results.txt | grep -v 'not_in_wordnet' | python likelyhood.py 
cat results.txt | grep -v 'not_in_wordnet' | grep -v 'KeyError' | python likelyhood.py 

