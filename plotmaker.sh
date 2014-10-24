cat textfiles/total_mero_counts.txt |  awk -F","  '{print $2}'  |  python chartmaker.py Meronym_Distance
cat textfiles/total_holo_counts.txt |  awk -F","  '{print $2}'  |  python chartmaker.py Holonym_Distance
cat textfiles/total_syn_counts.txt |  awk -F","  '{print $2}'  |  python chartmaker.py Synonym_Distance
cat textfiles/total_hyper_counts.txt |  awk -F","  '{print $2}'  | python chartmaker.py Hypernym_Distance
cat textfiles/total_hypo_counts.txt  |  awk -F","  '{print $2}'  | python chartmaker.py Hyponym_Distance



echo 'scatters'
#generate the plots
./scattermaker.sh syn
./scattermaker.sh hypo
./scattermaker.sh hyper
./scattermaker.sh holo
./scattermaker.sh mero
./scattermaker.sh adjusted_syn
./scattermaker.sh adjusted_hypo
./scattermaker.sh adjusted_hyper
./scattermaker.sh adjusted_holo
./scattermaker.sh adjusted_mero
python barcharter.py

