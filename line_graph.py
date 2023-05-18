import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Product Sans'
matplotlib.rcParams['font.size'] = 10

df = pd.read_csv('earthquakes/japan-20190101_20211203_query.csv')

x = df['time']
y = df['mag']
y2 = df['depth']

fig, ax1 = plt.subplots()

ax1.plot(x, y2, label='Depth', color='#264653', linewidth=.5)
ax1.set_ylabel('Depth', color='#264653')
ax1.tick_params(axis='y', labelcolor='#264653')

ax2 = ax1.twinx()

ax2.plot(x, y, label='Magnitude', color='#e76f51', linewidth=.5, alpha=0.8)
ax2.set_ylabel('Magnitude', color='#e76f51')
ax2.tick_params(axis='y', labelcolor='#e76f51')

ax1.set_xlabel('Time')

plt.title('Japan Earthquakes\nMagnitude and Depth')

plt.show()
