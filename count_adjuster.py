lines = tuple(open("wordnetcheck.txt", 'r'))

for l in lines:
	filename, multiple = l.replace("\n", "").split(" ")
	file_to_fix = tuple(open("textfiles/" + filename, 'r'))
	print "adjusting " + "textfiles/" + filename
	lines_to_write = []
	for f in file_to_fix:
		k, count = f.replace("\n", "").split(",")
		count = int(round(float(count) * float(multiple)))
		lines_to_write.append(",".join([str(k), str(count)]))
	with open("textfiles/" + filename.replace("total_", "total_adjusted_"), "a") as outfile:
		for item in lines_to_write:
			if len(item)>0:
				outfile.write(item + "\n")