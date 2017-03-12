import matplotlib.pyplot as plt
import numpy as np
import requests
import sys
import json
# from pandas_datareader.data import DataReader

def graph_data(stock):
    # df = DataReader('TSLA','yahoo')

    fig = plt.figure() # in order to modify the figure we need to reference it first
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/{}/chartdata;type=quote;range=10d/json'.format(stock)
    r = requests.get(stock_price_url)
    r_jsonp_text = r.text
    try:
        left_index = r_jsonp_text.index('(') + 1
        right_index = r_jsonp_text.rindex(')')
    except ValueError:
        print("Failed to convert JSONP to JSON.")
        sys.exit(1)
    r_json_text = r_jsonp_text[left_index:right_index]
    data = json.loads(r_json_text)

    timestamp = []
    closep = []
    for row in data['series']:
        timestamp.append(row['Timestamp'])
        closep.append(row['close'])

    timestamp = np.asarray(timestamp, dtype='datetime64[s]') # convert timestamp to dates
    timestamp = timestamp.tolist() # convert timestamp into list of datetime.datetimes

    ax1.plot_date(timestamp, closep, '-', label='Price')
    ax1.grid(True)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend() # automatically creates legend using the labels passed to plt.plot calls (First Line and Second Line)
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.20)
    plt.show()

graph_data('TSLA')
