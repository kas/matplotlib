import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates
from matplotlib.dates import bytespdate2num
# from pandas_datareader.data import DataReader

def graph_data(stock):
    fig = plt.figure() # in order to modify the figure we need to reference it first
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/{}/chartdata;type=quote;range=10y/csv'.format(stock)
    # df = DataReader('TSLA','yahoo')
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    split_source = source_code.split('\n')
    stock_data = []
    for line in split_source:
        if (len(line.split(',')) == 6) and ('labels:' not in line) and (line != 'values:Date,close,high,low,open,volume'):
            stock_data.append(line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data, delimiter=',', unpack=True, converters={0: bytespdate2num('%Y%m%d')})

    ax1.plot_date(date, closep, '-', label='Price')
    # for label in ax1.xaxis.get_ticklabels():
    #     label.set_rotation(45)
    ax1.grid(True)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend() # automatically creates legend using the labels passed to plt.plot calls (First Line and Second Line)
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.20)
    plt.show()

graph_data('TSLA')
