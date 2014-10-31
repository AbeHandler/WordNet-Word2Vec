import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib
from matplotlib.ticker import FuncFormatter


def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(int(round(100 * y)))
    print s

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] == True:
        return s + r'$\%$'
    else:
        return s + '%'

#formatter = FuncFormatter(to_percent)

# Set the formatter
#plt.gca().yaxis.set_major_formatter(formatter)

x_arr = []

for l in sys.stdin:
	x_arr.append(float(l.replace("\n", "")))

# Fake data
x = np.arange(0, len(x_arr), 1)

y = np.array(x_arr)

area = 15 # 0 to 15 point radiuses

plt.scatter(x, y, s=area, c='b', alpha=1, label=sys.argv[1])
plt.legend()
plt.xlabel("k")
plt.ylabel("Probability")
#plt.axis([0, 200, 0, .1])
plt.tight_layout()

plt.savefig(sys.argv[1] + '.png', bbox_inches='tight', pad_inches=.4)

plt.loglog(x, y, basex=2, basey=2)
plt.savefig(sys.argv[1] + "_log" + '.png', bbox_inches='tight', pad_inches=.4)