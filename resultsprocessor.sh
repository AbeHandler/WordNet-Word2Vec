cat results.txt | grep 'syn,' | awk -F","  '{print $5}' | sort -n | python chartmaker.py Synonym_Distance
cat results.txt | grep 'ant,' | awk -F","  '{print $5}' | sort -n | uniq -c | tr -s ' ' | tr ' ' '&' | sed -e 's/^&//g' > ant.txt
cat results.txt | grep 'holo,' | awk -F","  '{print $5}' | sort -n | uniq -c | tr -s ' ' | tr ' ' '&' | sed -e 's/^&//g' > holo.txt
cat results.txt | grep 'mero,' | awk -F","  '{print $5}' | sort -n | uniq -c | tr -s ' ' | tr ' ' '&' | sed -e 's/^&//g' > mero.txt
cat results.txt | grep 'none,' | awk -F","  '{print $5}' | sort -n | uniq -c | tr -s ' ' | tr ' ' '&' | sed -e 's/^&//g' > none.txt
cat results.txt | grep 'hyper,' | awk -F","  '{print $5}' | sort -n | uniq -c | tr -s ' ' | tr ' ' '&' | sed -e 's/^&//g' > hyper.txt
cat results.txt | grep 'hypo,' | awk -F","  '{print $5}' | sort -n | uniq -c | tr -s ' ' | tr ' ' '&' | sed -e 's/^&//g' > hypo.txt
