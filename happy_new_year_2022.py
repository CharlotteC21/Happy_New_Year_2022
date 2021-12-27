# import libraries
from pandas import DataFrame
from scipy.stats import uniform
from scipy.stats import randint
import numpy as np
import matplotlib.pyplot as plt

# sample data
df = DataFrame({'ny' : ['ny-%i' % i for i in np.arange(10000)],
'pvalue' : uniform.rvs(size=10000),
'color_dots' : ['c-%i' % i for i in randint.rvs(0,12,size=10000)]})

# -log_10(pvalue)
df['confetti'] = -np.log10(df.pvalue)
df.color_dots = df.color_dots.astype('category')
df.color_dots = df.color_dots.cat.set_categories(['c-%i' % i for i in range(12)], ordered=True)
df = df.sort_values('color_dots')

df['ind'] = range(len(df))
df_grouped = df.groupby(('color_dots'))

# manhattan plot
fig = plt.figure(figsize=(14, 8)) # Set the figure size
ax = fig.add_subplot(111)
colors = ['darkred','darkgreen','darkblue', 'gold']
x_labels = []
x_labels_pos = []
for num, (name, group) in enumerate(df_grouped):
    group.plot(kind='scatter', x='ind', y='confetti',color=colors[num % len(colors)], ax=ax)
    x_labels.append(name)
    x_labels_pos.append((group['ind'].iloc[-1] - (group['ind'].iloc[-1] - group['ind'].iloc[0])/2))
ax.set_xticks(x_labels_pos)
ax.set_xticklabels(x_labels)

# set axis limits
ax.set_xlim([0, len(df)])
ax.set_ylim([0, 3.5])

# x axis label
ax.set_xlabel('Happy New Year 2022!', fontsize=55)

# show the graph
plt.show()