import json
import pandas as pd
import matplotlib.pyplot as plt
import requests
from config import alpha_vantage_api_api_key as key

plt.rcParams['font.family'] = 'Product Sans'
plt.rcParams['font.size'] = 10


def graph_data(stock):
    stock_price_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock}&apikey={key}'
    
    response = requests.get(stock_price_url)
    data = json.loads(response.text)
    
    time_series_data = data['Time Series (Daily)']
    
    df = pd.DataFrame.from_dict(time_series_data, orient='index')
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    
    plt.plot(df.index, df['4. close'])
    
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title('Daily Adjusted Close Prices')
    plt.show()


graph_data('TSLA')
