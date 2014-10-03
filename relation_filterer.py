import os
import sys

threshold = .7

for line in sys.stdin:
	try:
		confidence = line.split("\t")[3]
		if float(confidence) > threshold:
			sentence =  line.split("\t")[4].split(" ")
			parts_of_speech =  line.split("\t")[5].split(" ")
			pos = {}
			for c in range(len(sentence)):
				pos[sentence[c]] = parts_of_speech[c]
			if len (line.split("\t")[1].split(" "))==1:
				for w in line.split("\t")[1].split(" "):
					if "V" in pos[w]: #if it's a verb
						print w
	except IndexError:
		pass