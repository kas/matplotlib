import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates
# from pandas_datareader.data import DataReader

def graph_data(stock):
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/{}/chartdata;type=quote;range=10y/csv'.format(stock)
    # df = DataReader('TSLA','yahoo')

    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    split_source = source_code.split('\n')

    stock_data = []

    for line in split_source:
        if (len(line.split(',')) == 6) and (line != 'values:Date,close,high,low,open,volume'):
            stock_data.append(line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data, delimiter=',', unpack=True, converters={0: bytespdate2num('%Y%m%d')})

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend() # automatically creates legend using the labels passed to plt.plot calls (First Line and Second Line)
    plt.show()

graph_data('TSLA')
