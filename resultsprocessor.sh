cat results.txt | grep 'syn,' | awk -F","  '{print $5}' | sort -n | python chartmaker.py Synonym_Distance
cat results.txt | grep 'ant,' | awk -F","  '{print $5}' | sort -n | python chartmaker.py Antonym_Distance
cat results.txt | grep 'holo,' | awk -F","  '{print $5}' | sort -n | python chartmaker.py Holonym_Distance
cat results.txt | grep 'mero,' | awk -F","  '{print $5}' | sort -n | python chartmaker.py Meronym_Distance
cat results.txt | grep 'none,' | awk -F","  '{print $5}' | sort -n | python chartmaker.py No_Relation
cat results.txt | grep 'hyper,' | awk -F","  '{print $5}' | sort -n | python chartmaker.py Hypernym_Distance
cat results.txt | grep 'hypo,' | awk -F","  '{print $5}' | sort -n | python chartmaker.py Hyponym_Distance
cat results.txt | python barcharter.py Bar