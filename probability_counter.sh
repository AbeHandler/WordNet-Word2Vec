
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