java -Xmx512m -jar reverb-latest.jar test/austen-emma.txt | awk -F "\t" 'BEGIN{OFS="\t";}{print $3,$4,$5,$12,$13,$14}' > austenrelations.txt
cat austenrelations.txt | python gensimmodel.py test > similarityofrelations.txt
cat similarityofrelations.txt | python relation_semanticprocessor.py > relations_sorted.txt