import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# Set the font family and size
matplotlib.rcParams['font.family'] = 'Product Sans'
matplotlib.rcParams['font.size'] = 10

# Read the data
df = pd.read_csv('earthquakes/japan-20190101_20211203_query.csv')

# Extract the magnitude column from the DataFrame
mag = df['mag']

# Define the bins for the histogram
bins = [2, 3, 4, 5, 6, 7, 8]

# Compute the histogram values
counts, edges = np.histogram(mag, bins)

# Define colors for each bin
colors = ['#264653', '#264653', '#2a9d8f', '#e9c46a', '#f4a261', '#e76f51']

# Plot each bar individually with a specified color
for i in range(len(bins) - 1):
    plt.bar(bins[i] + 0.5, counts[i], width=1, color=colors[i % len(colors)], edgecolor='white')

# Add gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Customize ticks and labels
plt.xticks(bins)

# Add data labels
for i, count in enumerate(counts):
    plt.text(bins[i] + 0.5, count + 1, str(int(count)), ha='center', va='bottom')

# Set the x-axis label
plt.xlabel('Magnitude')

# Set the y-axis label
plt.ylabel('Frequency')

# Set the title of the plot
plt.title('Japan Earthquakes 2019-2021\nMagnitude Frequency Distribution')

# Display the plot
plt.show()
