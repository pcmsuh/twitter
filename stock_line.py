import json
import pandas as pd
import matplotlib.pyplot as plt
import requests
from config import alpha_vantage_api_api_key as key

plt.rcParams['font.family'] = 'Product Sans'
plt.rcParams['font.size'] = 10


def graph_data(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    stock_price_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock}&apikey={key}'
    
    response = requests.get(stock_price_url)
    data = json.loads(response.text)
    
    time_series_data = data['Time Series (Daily)']
    
    df = pd.DataFrame.from_dict(time_series_data, orient='index')
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    
    ax1.plot(df.index, df['4. close'], label='Price')
    for label in ax1.get_xticklabels():
        label.set_rotation(45)
    ax1.grid(True, color = 'grey', linestyle='-', linewidth=0.25)

    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title('Daily Adjusted Close Prices')
    plt.legend()
    plt.subplots_adjust(left=0.15, bottom=0.25, right=0.9, top=0.85, wspace=0.2, hspace=0)
    plt.show()


graph_data('TSLA')
