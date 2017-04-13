from matplotlib import style
from matplotlib.finance import candlestick2_ohlc
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

import datetime as dt
import json
import numpy as np
import requests

style.use('fivethirtyeight')
print(plt.style.available)

print(plt.__file__)

def graph_data(stock):
    fig = plt.figure() # in order to modify the figure we need to reference it first
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/{}/chartdata;type=quote;range=1m/json'.format(stock)
    r = requests.get(stock_price_url)
    r_jsonp_text = r.text
    try:
        left_index = r_jsonp_text.index('(') + 1
        right_index = r_jsonp_text.rindex(')')
    except ValueError:
        print('Failed to convert JSONP to JSON!')
        sys.exit(1)
    r_json_text = r_jsonp_text[left_index:right_index]
    data = json.loads(r_json_text)

    date = []
    closep = []
    openp = []
    highp = []
    lowp = []
    volume = []
    for row in data['series']:
        date.append(row['Date'])
        closep.append(row['close'])
        openp.append(row['open'])
        highp.append(row['high'])
        lowp.append(row['low'])
        volume.append(row['volume'])

    for index, current_date in enumerate(date):
        date[index] = dt.datetime.strptime(str(current_date), '%Y%m%d').date()

    date = np.asarray(date)
    closep = np.asarray(closep)
    openp = np.asarray(openp)
    highp = np.asarray(highp)
    lowp = np.asarray(lowp)
    volume = np.asarray(volume)

    candlestick2_ohlc(ax1, openp, highp, lowp, closep, width=0.4)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.grid(True)

    bbox_props = dict(boxstyle='round', fc='w', ec='k')
    ax1.annotate(str(closep[-1]), (date[-1], closep[-1]), xytext=(date[-1], closep[-1]), bbox=bbox_props)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.20)
    plt.show()

graph_data('EBAY')

