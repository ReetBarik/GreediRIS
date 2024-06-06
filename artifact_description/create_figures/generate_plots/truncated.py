import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

x = ['32', '64', '128', '256', '512']
y1 = [393.7, 210.4, 112.3, 77.2, 57.3]
y2 = [128.705, 60.145, 22.968, 13.104, 8.482]
y1 = [m-n for m, n in zip(y1, y2)]

y11 = [393.7,207.9,123.3,107.9,119.1]
y21 = [128.705,55.245,27.804,31.147,60.558]
y11 = [m-n for m, n in zip(y11, y21)]

alpha = [r'$\alpha=1$', r'$\alpha=0.5$', r'$\alpha=0.25$', r'$\alpha=0.125$', r'$\alpha=0.0625$']


fig, axes = plt.subplots(nrows=2, ncols=1)
# axs = fig.subplot_mosaic([['bar1'], ['bar2']])

axes[0].bar(x, y11, color = 'tomato', edgecolor='black', label='Total')
axes[0].bar(x, y21, color = 'tomato', bottom=y11, edgecolor='black', hatch='//', label='Seed Selection')
axes[0].set_ylabel('Time (sec)')
# axes[0].set_xlabel('m: Number of machines')
axes[0].set_title('(a) GreediRIS', fontsize=10)
axes[0].legend()


axes[1].bar(x, y1, color = 'palevioletred', edgecolor='black', label='Total')
rects = axes[1].bar(x, y2, color = 'palevioletred', bottom=y1, edgecolor='black', hatch='//', label='Seed Selection')
axes[1].bar_label(rects,labels = alpha, padding=3, label_type = 'edge')
axes[1].set_ylabel('Time (sec)')
axes[1].set_xlabel('m: Number of nodes')
axes[1].set_title('(b) GreediRIS-trunc', fontsize=10)
axes[1].legend()

plt.tight_layout()
plt.savefig('Figure5.PDF', dpi=500)
