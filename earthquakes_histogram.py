import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.family'] = 'Product Sans'
matplotlib.rcParams['font.size'] = 10

df = pd.read_csv('earthquakes/japan-20190101_20211203_query.csv')
mag = df['mag']

bins = [2, 3, 4, 5, 6, 7, 8]
counts, edges = np.histogram(mag, bins)

colors = ['#264653', '#264653', '#2a9d8f', '#e9c46a', '#f4a261', '#e76f51']

for i in range(len(bins) - 1):
    plt.bar(bins[i] + 0.5, counts[i], width=1, color=colors[i % len(colors)], edgecolor='white')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(bins)

for i, count in enumerate(counts):
    plt.text(bins[i] + 0.5, count + 1, str(int(count)), ha='center', va='bottom')

plt.xlabel('Magnitude')
plt.ylabel('Frequency')
plt.title('Japan Earthquakes 2019-2021\nMagnitude Frequency Distribution')
plt.show()
