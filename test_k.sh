cat textfiles/results.txt | grep -v 'not_in_wordnet' | grep -v 'KeyError' | grep -v 'same' | grep "$1"  | awk -F',' 'BEGIN { OFS=","} { print $2,$6 }' 

