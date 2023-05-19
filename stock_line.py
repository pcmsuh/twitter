import json
import pandas as pd
import matplotlib.pyplot as plt
import requests
from config import alpha_vantage_api_api_key as key

plt.rcParams['font.family'] = 'Product Sans'
plt.rcParams['font.size'] = 10
theme_colors = ['#212529', '#343a40']


def graph_data(stock, start_date):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    stock_price_url = (
        f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={stock}&apikey={key}'
    )

    response = requests.get(stock_price_url)
    data = json.loads(response.text)

    time_series_data = data['Monthly Adjusted Time Series']
    df = pd.DataFrame.from_dict(time_series_data, orient='index')
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)

    ax1.plot(df.index, df['4. close'], label='Price')

    ax1.plot([], [], linewidth=5, label='Loss', color='red', alpha=0.5)
    ax1.plot([], [], linewidth=5, label='Gain', color='green', alpha=0.5)

    mask = (df.index > start_date)
    start_price = df.asof(start_date)['4. close']
    ax1.axhline(start_price, color=theme_colors[0], linestyle='-', linewidth=0.25)

    ax1.fill_between(df.index[mask], df['4. close'][mask], start_price,
                     alpha=0.5, where=(df['4. close'][mask] > start_price),
                     color='green', interpolate=True)
    ax1.fill_between(df.index[mask], df['4. close'][mask], start_price,
                     alpha=0.5, where=(df['4. close'][mask] <= start_price),
                     color='red', interpolate=True)

    for label in ax1.get_xticklabels():
        label.set_rotation(45)
    ax1.grid(True, color='grey', linestyle='-', linewidth=0.25)
    ax1.xaxis.label.set_color(theme_colors[0])
    ax1.yaxis.label.set_color(theme_colors[0])

    ax1.set_yticks(range(0, int(df['4. close'].max()) + 100, 100))

    ax1.spines['left'].set_color('grey')
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)

    ax1.tick_params(axis='x', colors=theme_colors[0], labelsize=10)
    ax1.tick_params(axis='y', colors=theme_colors[0], labelsize=10)

    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title(f'{stock}\n(Louis Vuitton, Moët & Chandon, Hennessy, Dior, and Sephora)')
    plt.legend()

    plt.subplots_adjust(left=0.15, bottom=0.25, right=0.9, top=0.85, wspace=0.2, hspace=0)
    plt.show()


graph_data('LVMHF', '2019-12-01')
