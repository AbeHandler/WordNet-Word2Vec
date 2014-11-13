echo 'syn-a|' $(cat textfiles/results.txt | egrep '^syn,a' | wc -l)
echo 'syn-n|' $(cat textfiles/results.txt | egrep '^syn,n' | wc -l)
echo 'syn-r|' $(cat textfiles/results.txt | egrep '^syn,r' | wc -l)
echo 'syn-v|' $(cat textfiles/results.txt | egrep '^syn,v' | wc -l)


echo 'mero-a|' $(cat textfiles/results.txt | egrep '^mero,a' | wc -l)
echo 'mero-n|' $(cat textfiles/results.txt | egrep '^mero,n' | wc -l)
echo 'mero-r|' $(cat textfiles/results.txt | egrep '^mero,r' | wc -l)
echo 'mero-v|' $(cat textfiles/results.txt | egrep '^mero,v' | wc -l)


echo 'holo-a|' $(cat textfiles/results.txt | egrep '^holo,a' | wc -l)
echo 'holo-n|' $(cat textfiles/results.txt | egrep '^holo,n' | wc -l)
echo 'holo-r|' $(cat textfiles/results.txt | egrep '^holo,r' | wc -l)
echo 'holo-v|' $(cat textfiles/results.txt | egrep '^holo,v' | wc -l)


echo 'hyper-a|' $(cat textfiles/results.txt | egrep '^hyper,a' | wc -l)
echo 'hyper-n|' $(cat textfiles/results.txt | egrep '^hyper,n' | wc -l)
echo 'hyper-r|' $(cat textfiles/results.txt | egrep '^hyper,r' | wc -l)
echo 'hyper-v|' $(cat textfiles/results.txt | egrep '^hyper,v' | wc -l)


echo 'hypo-a|' $(cat textfiles/results.txt | egrep '^hypo,a' | wc -l)
echo 'hypo-n|' $(cat textfiles/results.txt | egrep '^hypo,n' | wc -l)
echo 'hypo-r|' $(cat textfiles/results.txt | egrep '^hypo,r' | wc -l)
echo 'hypo-v|' $(cat textfiles/results.txt | egrep '^hypo,v' | wc -l)