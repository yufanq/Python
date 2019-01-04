import matplotlib.pyplot as plt
import numpy as np
'''
水平直方图
barh
	
	
ax.invert_yaxis  水平图例显示方向


'''
#Fixing random state for reproducibility

np.random.seed(19680801)

plt.rcdefaults()
fig, ax = plt.subplots()

#Rxample data

people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr= error, align= 'center',
        color='green',ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)

ax.invert_yaxis() # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast to do you want to go today')

plt.show()