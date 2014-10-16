cat results.txt | grep 'syn,' | awk -F","  '{print $5}' | sort -n | python chartmaker.py Synonym_Distance
cat results.txt | grep 'holo,' | awk -F","  '{print $5}' | sort -n | python chartmaker.py Holonym_Distance
cat results.txt | grep 'mero,' | awk -F","  '{print $5}' | sort -n | python chartmaker.py Meronym_Distance
cat results.txt | grep 'none,' | awk -F","  '{print $5}' | sort -n | python chartmaker.py No_Relation
cat results.txt | grep 'hyper,' | awk -F","  '{print $5}' | sort -n | python chartmaker.py Hypernym_Distance
cat results.txt | grep 'hypo,' | awk -F","  '{print $5}' | sort -n | python chartmaker.py Hyponym_Distance
cat results.txt | python barcharter.py Bar
cat results.txt | egrep '^syn' | awk  -F"," 'BEGIN {OFS = ","} {print $4,$6}' | python scatterploy.py 



cat results.txt | egrep '^holo' | awk  -F"," 'BEGIN {OFS = ","} {print $6}' | python meaner.py 
cat results.txt | egrep '^mer' | awk  -F"," 'BEGIN {OFS = ","} {print $6}' | python meaner.py 
cat results.txt | egrep '^hyp' | awk  -F"," 'BEGIN {OFS = ","} {print $6}' | python meaner.py 
cat results.txt | egrep '^hypo' | awk  -F"," 'BEGIN {OFS = ","} {print $6}' | python meaner.py 
cat results.txt | egrep '^syn' | awk  -F"," 'BEGIN {OFS = ","} {print $6}' | python meaner.py    #check at different Ks
