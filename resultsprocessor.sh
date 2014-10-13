echo 'key error'
cat results.txt | egrep '^KeyError' | wc -l
echo 'syn'
cat results.txt | egrep '^syn' | wc -l 
echo 'ant'
cat results.txt | egrep '^ant' | wc -l
echo 'none'
cat results.txt | egrep '^none' | wc -l
echo 'total'
cat results.txt |  wc -l
