#get the counts for each of the different relations at different values of k
./type_counter.sh 200 syn | tr -d " \t\ \r" | tr '-' ',' > textfiles/total_syn_counts.txt 

./type_counter.sh 200 hypo | tr -d " \t\ \r" | tr '-' ',' > textfiles/total_hypo_counts.txt 

./type_counter.sh 200 hyper | tr -d " \t\ \r" | tr '-' ',' > textfiles/total_hyper_counts.txt 

./type_counter.sh 200 holo | tr -d " \t\ \r" | tr '-' ',' > textfiles/total_holo_counts.txt 

./type_counter.sh 200 mero  | tr -d " \t\ \r" | tr '-' ',' > textfiles/total_mero_counts.txt 

./type_counter.sh 200 stem  | tr -d " \t\ \r" | tr '-' ',' > textfiles/total_stem_counts.txt 


./total_counter.sh 200  | tr -d " \t\ \r" | tr '-' ',' > textfiles/total_counts.txt


./scattermaker.sh syn
./scattermaker.sh hypo
./scattermaker.sh hyper
./scattermaker.sh holo
./scattermaker.sh mero
./scattermaker.sh stem

#cat results.txt | egrep '^syn,' | awk -F","  '{print $5}' | sort -n > syndist.txt
#cat results.txt | egrep '^holo,' | awk -F","  '{print $5}' | sort -n > holdist.txt
#cat results.txt | egrep '^mero,' | awk -F","  '{print $5}' | sort -n > merdist.txt
#cat results.txt | egrep '^none,' | awk -F","  '{print $5}' | sort -n > none.txt
#cat results.txt | egrep '^hyper,' | awk -F","  '{print $5}' | sort -n  > hyperdist.txt
#cat results.txt | egrep '^hypo,' | awk -F","  '{print $5}' | sort -n > hypodist.txt
#cat results.txt | egrep '^same' | awk -F","  '{print $5}' > samestem.txt


#cat samestem.txt | python chartmaker.py Same_stem
#cat none.txt | python chartmaker.py No_Relation
#cat merdist.txt | python chartmaker.py Meronym_Distance
#cat holdist.txt | python chartmaker.py Holonym_Distance
#cat syndist.txt | python chartmaker.py Synonym_Distance
#cat hyperdist.txt | python chartmaker.py Hypernym_Distance
#cat hypodist.txt | python chartmaker.py Hyponym_Distance
#cat results.txt | python barcharter.py Bar

#cat results.txt | python averagejacard.py 
#cat results.txt | python counter.py

#cat results.txt | python barcharter_adjusted.py 

#cat results.txt | grep -v 'not_in_wordnet' | grep -v 'KeyError' | python likelyhood.py 
#cat synread.txt | python sample.py 


#cat results.txt | grep -v 'not_in_wordnet' | grep -v 'KeyError' | python likelyhood_processor.py 