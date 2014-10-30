#cleanup from any prior runs
rm textfiles/total* > /dev/null 2>&1
rm images/* > /dev/null 2>&1
rm *png > /dev/null 2>&1

#generate the counts

 ./type_counter.sh 200 same | tr -d " \t\ \r" | tr '-' ',' > textfiles/total_stem_counts.txt 

./type_counter.sh 200 syn | tr -d " \t\ \r" | tr '-' ',' > textfiles/total_syn_counts.txt

./type_counter.sh 200 hypo | tr -d " \t\ \r" | tr '-' ',' > textfiles/total_hypo_counts.txt

./type_counter.sh 200 hyper | tr -d " \t\ \r" | tr '-' ',' > textfiles/total_hyper_counts.txt 

./type_counter.sh 200 holo | tr -d " \t\ \r" | tr '-' ',' > textfiles/total_holo_counts.txt 

./type_counter.sh 200 mero | tr -d " \t\ \r" | tr '-' ',' > textfiles/total_mero_counts.txt 

./total_counter.sh 200 | tr -d " \t\ \r" | tr '-' ',' > textfiles/total_counts.txt

python counter.py > latexchart.txt  #a make the chart for the latex document

#make adjusted counts
python wordnetchecker.py > wordnetcheck.txt  #shows the output of the checker for inclusion in latex doc
rm textfiles/total_adjusted*
python count_adjuster.py


#calculate the probabilities 
python probability_calculator.py --relation_file textfiles/total_syn_counts.txt --k_file textfiles/total_counts.txt > textfiles/syn_probabilities.txt
python probability_calculator.py --relation_file textfiles/total_mero_counts.txt --k_file textfiles/total_counts.txt > textfiles/mero_probabilities.txt
python probability_calculator.py --relation_file textfiles/total_holo_counts.txt --k_file textfiles/total_counts.txt > textfiles/holo_probabilities.txt
python probability_calculator.py --relation_file textfiles/total_hyper_counts.txt --k_file textfiles/total_counts.txt > textfiles/hyper_probabilities.txt
python probability_calculator.py --relation_file textfiles/total_hypo_counts.txt --k_file textfiles/total_counts.txt > textfiles/hypo_probabilities.txt

python probability_calculator.py --relation_file textfiles/total_adjusted_syn_counts.txt --k_file textfiles/total_counts.txt > textfiles/adjusted_syn_probabilities.txt
python probability_calculator.py --relation_file textfiles/total_adjusted_mero_counts.txt --k_file textfiles/total_counts.txt > textfiles/adjusted_mero_probabilities.txt
python probability_calculator.py --relation_file textfiles/total_adjusted_holo_counts.txt --k_file textfiles/total_counts.txt > textfiles/adjusted_holo_probabilities.txt
python probability_calculator.py --relation_file textfiles/total_adjusted_hyper_counts.txt --k_file textfiles/total_counts.txt > textfiles/adjusted_hyper_probabilities.txt
python probability_calculator.py --relation_file textfiles/total_adjusted_hypo_counts.txt --k_file textfiles/total_counts.txt > textfiles/adjusted_hypo_probabilities.txt


cat textfiles/total_syn_counts.txt | awk -F"," '{print $2}' > textfiles/total_count_scatter_syn.txt
cat textfiles/total_mero_counts.txt | awk -F"," '{print $2}' > textfiles/total_count_scatter_mero.txt
cat textfiles/total_hyper_counts.txt | awk -F"," '{print $2}' > textfiles/total_count_scatter_hyper.txt
cat textfiles/total_hypo_counts.txt | awk -F"," '{print $2}' > textfiles/total_count_scatter_hypo.txt
cat textfiles/total_holo_counts.txt | awk -F"," '{print $2}' > textfiles/total_count_scatter_holo.txt
cat textfiles/total_holo_counts.txt | awk -F"," '{print $2}' > textfiles/total_count_scatter_stem.txt