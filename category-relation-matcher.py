import sys
from nltk.corpus import stopwords

last = 0
words = []

with open("reverb_wikipedia_tuples_short.txt", "r") as reverb:
    reverb_array = []
    for line in reverb:
        reverb_array.append(line)


def find_candidates(words):
    filtered_words = [w for w in words if not w in stopwords.words('english')]

#    print words


for line in sys.stdin:
    word = line.split(" ")[0]
    number = int(line.split(" ")[1].strip("\n"))
    if number > last:
        find_candidates(words)
        last = number
        words = []
        words.append(word)
    else:
        words.append(word)


print words
