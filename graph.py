import matplotlib.pyplot as plt
left = [1,2,3,4,5]
height = [11,29,60,56,22]
tick_label = ['one', 'two', 'three', 'four', 'five']
plt.bar(left, height, tick_label = tick_label,
		width = 0.8, color = ['blue', 'red'])
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title("my second graph")
plt.show()