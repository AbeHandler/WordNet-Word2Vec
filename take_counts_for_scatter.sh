cat textfiles/total_syn_counts.txt | awk -F"," '{print $2}' > textfiles/total_count_scatter_syn.txt
cat textfiles/total_mero_counts.txt | awk -F"," '{print $2}' > textfiles/total_count_scatter_mero.txt
cat textfiles/total_hyper_counts.txt | awk -F"," '{print $2}' > textfiles/total_count_scatter_hyper.txt
cat textfiles/total_hypo_counts.txt | awk -F"," '{print $2}' > textfiles/total_count_scatter_hypo.txt
cat textfiles/total_holo_counts.txt | awk -F"," '{print $2}' > textfiles/total_count_scatter_holo.txt
cat textfiles/total_holo_counts.txt | awk -F"," '{print $2}' > textfiles/total_count_scatter_stem.txt