import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import json
import requests
import sys
# from pandas_datareader.data import DataReader

def graph_data(stock):
    # df = DataReader('TSLA','yahoo')

    fig = plt.figure() # in order to modify the figure we need to reference it first
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/{}/chartdata;type=quote;range=10y/json'.format(stock)
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

    date = []
    closep = []
    for row in data['series']:
        date.append(row['Date'])
        closep.append(row['close'])

    for index, current_date in enumerate(date):
        date[index] = dt.datetime.strptime(str(current_date), '%Y%m%d').date()

    date = np.asarray(date)
    closep = np.asarray(closep)

    ax1.plot_date(date, closep, '-', label='Price')
    ax1.axhline(closep[0], color='k', linewidth=5)
    ax1.fill_between(date, closep, closep[0], label='Gain', where=(closep > closep[0]), facecolor='g', alpha=0.5)
    ax1.fill_between(date, closep, closep[0], label='Loss', where=(closep < closep[0]), facecolor='r', alpha=0.5)    

    ax1.grid(True)
    # ax1.xaxis.label.set_color('c')
    # ax1.yaxis.label.set_color('r')
    ax1.set_yticks([0.0, 25.0, 50.0, 75.0])

    ax1.spines['left'].set_color('c')
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['left'].set_linewidth(5)

    ax1.tick_params(axis='x', colors='#f06215')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    plt.legend() # automatically creates legend using the labels passed to plt.plot calls (First Line and Second Line)
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.20)
    plt.show()

graph_data('EBAY')
