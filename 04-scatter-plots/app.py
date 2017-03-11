import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 4, 2, 1, 4, 5, 2, 3]

plt.scatter(x, y, label='skitscat', color='k', marker='x', s=15)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend() # automatically creates legend using the labels passed to plt.plot calls (First Line and Second Line)
plt.show()
