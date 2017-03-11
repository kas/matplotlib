import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
colors = ['c', 'm', 'r', 'b']

plt.pie(slices, labels=activities, colors=colors, startangle=90, shadow=True, explode=(0, 0.1, 0, 0), autopct='%1.1f%%')

# plt.xlabel('x')
# plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
# plt.legend() # automatically creates legend using the labels passed to plt.plot calls (First Line and Second Line)
plt.show()
