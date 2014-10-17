cat results.txt | grep 'syn,' | awk -F","  '{print $5}' | sort -n > syndist.txt
cat results.txt | grep 'holo,' | awk -F","  '{print $5}' | sort -n > holdist.txt
cat results.txt | grep 'mero,' | awk -F","  '{print $5}' | sort -n > merdist.txt
cat results.txt | grep 'none,' | awk -F","  '{print $5}' | sort -n > none.txt
cat results.txt | grep 'hyper,' | awk -F","  '{print $5}' | sort -n  > hyperdist.txt
cat results.txt | grep 'hypo,' | awk -F","  '{print $5}' | sort -n > hypodist.txt
cat results.txt | grep '^same' | awk -F","  '{print $5}' > samestem.txt


cat samestem.txt | python chartmaker.py Same_stem
cat none.txt | python chartmaker.py No_Relation
cat merdist.txt | python chartmaker.py Meronym_Distance
cat holdist.txt | python chartmaker.py Holonym_Distance
cat syndist.txt | python chartmaker.py Synonym_Distance
cat hyperdist.txt | python chartmaker.py Hypernym_Distance
cat hypodist.txt | python chartmaker.py Hyponym_Distance
cat results.txt | python barcharter.py Bar

cat results.txt | python averagejacard.py 
