cat reverb_wikipedia_tuples.txt | awk -F '\t' '{print $4, $5, $6}' | tr '[:upper:]' '[:lower:]' |  tr -d 0-9 > reverb_wikipedia_tuples_short.txt
