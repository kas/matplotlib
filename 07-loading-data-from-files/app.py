import matplotlib.pyplot as plt

# method 1
'''
import csv

x = []
y = []

with open('example.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label='Loaded from file!')
'''

# method 2
'''
import numpy as np

x, y = np.loadtxt('example.txt', delimiter=',', unpack=True) # unpack into x and y
plt.plot(x, y, label='Loaded from file!')
'''

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend() # automatically creates legend using the labels passed to plt.plot calls (First Line and Second Line)
plt.show()
