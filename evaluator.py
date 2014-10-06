import wordnetter
import sys
from wordnetter import synononymous
from wordnetter import antonymous
from nltk.corpus import wordnet as wn

yes = 0
no = 0
lines = []
for line in sys.stdin:
	lines.append(line)

print "Checking for synononymous"

for line in lines:
	try:
		parts = line.replace("\n","").split("\t")
		pos = wn.VERB
		if synononymous(parts[1],parts[2],wn.VERB):
			yes = yes + 1
			#print "{}, {}".format(parts[1],parts[2], "v")
		else:
			no = no + 1
	except IndexError:
		pass

print "yes {}".format(str(yes))
print "no {}".format(str(no))


print "Checking for antonyms"
yes = 0 
no = 0
for line in lines:
	try:
		parts = line.replace("\n","").split("\t")
		pos = wn.VERB
		if antonymous(parts[1],parts[2],wn.VERB):
			yes = yes + 1
			#print "{}, {}".format(parts[1],parts[2], "v")
		else:
			no = no + 1
	except IndexError:
		pass

print "yes {}".format(str(yes))
print "no {}".format(str(no))