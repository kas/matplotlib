import matplotlib.pyplot as plt
import numpy as np
import urllib
# from pandas_datareader.data import DataReader

def graph_data(stock):
    fig = plt.figure() # in order to modify the figure we need to reference it first
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    # stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/{}/chartdata;type=quote;range=10d/csv'.format(stock)
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/{}/chartdata;type=quote;range=10d/csv'.format(stock)
    # df = DataReader('TSLA','yahoo')
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    split_source = source_code.split('\n')
    stock_data = []
    for line in split_source:
        if (len(line.split(',')) == 6) and ('labels:' not in line) and (line != 'values:Timestamp,close,high,low,open,volume'):
            stock_data.append(line)

    timestamp, closep, highp, lowp, openp, volume = np.loadtxt(stock_data, delimiter=',', unpack=True)
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
