"""
Simple demo of a scatter plot.
"""
import numpy as np
import matplotlib.pyplot as plt
import sys

x = []
y = []

for l in sys.stdin:
	parts = l.split(",")
	xf = float(parts[0].replace("\n", ""))
	yf = float(parts[1].replace("\n", ""))
	parts = l.split(",")
	x.append(xf)
	y.append(yf)


x = np.array(x)
y = np.array(y)

area = 5 # 0 to 15 point radiuses

plt.scatter(x, y, s=area, c='b', alpha=0.5)
plt.show()