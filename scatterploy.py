"""
Simple demo of a scatter plot.
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib
from matplotlib.ticker import FuncFormatter


def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] == True:
        return s + r'$\%$'
    else:
        return s + '%'

formatter = FuncFormatter(to_percent)

# Set the formatter
plt.gca().yaxis.set_major_formatter(formatter)

x_arr = []

for l in sys.stdin:
	x_arr.append(float(l.replace("\n", "")))

# Fake data
x = np.arange(0, len(x_arr), 1)

y = np.array(x_arr)


area = 5 # 0 to 15 point radiuses

plt.scatter(x, y, s=area, c='b', alpha=1, label='Synonym')
plt.legend()
plt.xlabel("K")
plt.ylabel("Pct likelyhood")
plt.tight_layout()
plt.savefig(sys.argv[1] + '.png', bbox_inches='tight', pad_inches=.4)