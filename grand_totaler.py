import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

bar_width = 0.35


opacity = 0.4
error_config = {'ecolor': '0.3'}
means_men = (1453, 2561, 25620, 37107, 42908)
index = np.arange(len(means_men))
rects1 = plt.bar(index, means_men, alpha=".5")

plt.xticks(index + bar_width, ('Holonym', 'Meronym', 'Hyponym', 'Synonym', 'Hypernym'))

plt.ylabel('Count')

plt.legend()

plt.tight_layout()
plt.savefig('grand_total.png', bbox_inches='tight', pad_inches=.4)