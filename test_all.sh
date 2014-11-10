./test_k.sh syn > textfiles/syn.txt
./test_k.sh mero > textfiles/mero.txt
./test_k.sh holo > textfiles/holo.txt
./test_k.sh hypo > textfiles/hypo.txt
./test_k.sh hyper > textfiles/hyper.txt
./test_k.sh none > textfiles/none.txt
cat textfiles/results.txt | grep -v 'not_in_wordnet' | grep -v 'KeyError' | grep -v 'same' | awk -F',' 'BEGIN { OFS=","} { print $5,$6 }' > textfiles/dandd.txt
