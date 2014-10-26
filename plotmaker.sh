cat textfiles/total_mero_counts.txt |  awk -F","  '{print $2}'  |  python chartmaker.py Meronym_Distance
cat textfiles/total_holo_counts.txt |  awk -F","  '{print $2}'  |  python chartmaker.py Holonym_Distance
cat textfiles/total_syn_counts.txt |  awk -F","  '{print $2}'  |  python chartmaker.py Synonym_Distance
cat textfiles/total_hyper_counts.txt |  awk -F","  '{print $2}'  | python chartmaker.py Hypernym_Distance
cat textfiles/total_hypo_counts.txt  |  awk -F","  '{print $2}'  | python chartmaker.py Hyponym_Distance



echo 'scatters'
python total_count_chart_maker_adjusted.py
python total_count_chart_maker.py

python barcharter.py

