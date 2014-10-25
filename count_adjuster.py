import os
lines = tuple(open("wordnetcheck.txt", 'r'))

for l in lines:
	filename, multiple = l.replace("\n", "").split(" ")
	file_to_fix = tuple(open("textfiles/" + filename, 'r'))
	print "adjusting " + "textfiles/" + filename
	lines_to_write = []
	for f in file_to_fix:
		k, count = f.replace("\n", "").split(",")
		print "k {}".format(k)
		print "count {}".format(count)
		print "multiple {}".format(multiple)
		adjusted_count = int(float(count) * float(multiple))
		print "adjusted_count {}".format(adjusted_count)
		lines_to_write.append(",".join([str(k), str(adjusted_count)]))

	try:
		os.remove("textfiles/" + filename.replace("total_", "total_adjusted_"))
	except OSError:
		pass

	with open("textfiles/" + filename.replace("total_", "total_adjusted_"), "a") as outfile:
		for item in lines_to_write:
			if len(item) > 0:
				outfile.write(item + "\n")
