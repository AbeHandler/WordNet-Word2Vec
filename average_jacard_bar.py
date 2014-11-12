import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

bar_width = 0.35


opacity = 0.4
error_config = {'ecolor': '0.3'}
means_men = (0.0673, 0.1608, 0.1887, 0.2059, 0.2985)
index = np.arange(len(means_men))
rects1 = plt.bar(index, means_men, alpha=".5")

plt.xticks(index + bar_width, ('Hyponym', 'Hypernym', 'Meronym', 'Synonym', 'Holonym'))

plt.ylabel('Count')

plt.legend()

plt.tight_layout()
plt.savefig('jacard.png', bbox_inches='tight', pad_inches=.4)