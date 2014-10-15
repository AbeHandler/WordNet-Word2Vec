"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt


n_groups = 5

count_syn = (20, 35, 30, 35, 27)

count_ant = (25, 32, 34, 20, 25)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, count_syn, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Synonyms')

rects2 = plt.bar(index + bar_width, count_ant, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Antonyms')

plt.xlabel('K')
plt.ylabel('Count')
plt.title('Semantic relations in WordNet')
plt.xticks(index + bar_width, ('1', '<10', '<20', '<50', '<100'))
plt.legend()

plt.tight_layout()
plt.show()