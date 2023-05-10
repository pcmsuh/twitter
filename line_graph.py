import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Set the font family and size
matplotlib.rcParams['font.family'] = 'Product Sans'
matplotlib.rcParams['font.size'] = 10

# Read the data
df = pd.read_csv('earthquakes/japan-20190101_20211203_query.csv')

# Extract the x, y, and y2 values
x = df['time']
y = df['mag']
y2 = df['depth']

# Create a figure and a set of subplots (axes)
fig, ax1 = plt.subplots()

# Plot the depth data (y2) on ax1 first
ax1.plot(x, y2, label='Depth', color='#264653', linewidth=.5)
ax1.set_ylabel('Depth', color='#264653')
ax1.tick_params(axis='y', labelcolor='#264653')

# Create ax2 with a shared x-axis and separate y-axis
ax2 = ax1.twinx()

# Plot the magnitude data (y) on ax2
ax2.plot(x, y, label='Magnitude', color='#e76f51', linewidth=.5, alpha=0.8)
ax2.set_ylabel('Magnitude', color='#e76f51')
ax2.tick_params(axis='y', labelcolor='#e76f51')

# Set the x-axis label
ax1.set_xlabel('Time')

# Set the title
plt.title('Japan Earthquakes\nMagnitude and Depth')

# Show the plot
plt.show()
