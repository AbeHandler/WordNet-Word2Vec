import sys
import numpy as np

total = []

for l in sys.stdin:
	try:
		if float(l.replace("\n", "")) < 1:
			total.append(float(l.replace("\n", "")))
	except ValueError:
		pass

x = np.array(total)

print np.mean(x)