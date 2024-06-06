import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

x = ['8','16','32', '64', '128', '256', '512']
y1 = [1693.0, 837.2,393.7, 210.4, 112.3, 77.2, 57.3]

y2 = [1693.0, 837.2,393.7,207.9,123.3,107.9,119.1]

x3 = ['16','32', '64', '128', '256', '512']
y3 = [614.9,427,265.9,225.85,185.8,164.3]

ticks = [1024, 512, 256, 128, 64]
tickLabels = ['$2^{10}$', '$2^9$', '$2^8$', '$2^7$', '$2^6$']


plt.plot(x, y1, color='black', marker='o', linestyle='dotted', linewidth=2, markersize=4, label='GreediRIS-trunc')
plt.plot(x, y2, color='black', marker='o', linewidth=2, markersize=4, label='GreediRIS')
plt.plot(x3, y3, color='red', marker='o', linewidth=2, markersize=4, label='Ripples')
plt.yscale("log")
plt.legend()
plt.ylabel('Time (sec)')
plt.xlabel('m: Number of nodes')
plt.yticks(ticks=ticks, labels=tickLabels, minor=False)
plt.tight_layout()
plt.savefig('Figure3.PDF', dpi=500)
