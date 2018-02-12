import requests
import datetime
import pandas as pd
import matplotlib.pyplot as plt

def hourly_price_historical(symbol, comparison_symbol, limit, aggregate, exchange=''):
    url = 'https://min-api.cryptocompare.com/data/histohour?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    return df

def plotchart(axis, df, symbol, comparison_symbol):
    axis.plot(df.timestamp, df.close)
    axis.set_title(symbol + ' vs ' + comparison_symbol)
    axis.set_ylabel('Price in '+comparison_symbol)
    axis.set_xlabel('Year')

df1 = hourly_price_historical('BTC','USD', 9999, 1)
df2 = hourly_price_historical('ETH','USD', 9999, 1)
f, axarr = plt.subplots(2)


plotchart(axarr[0],df1,'BTC','USD')
plotchart(axarr[0],df2,'ETH','USD')

plt.show()