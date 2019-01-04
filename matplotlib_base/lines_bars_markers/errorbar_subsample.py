import numpy as np
import  matplotlib.pyplot as plt
'''
	errorbar
		yerr  错误标记的大小
		errorevery  每隔几个点显示一次错误标记

'''
# example data
x = np.arange(0.1, 4, 0.1)
y = np.exp( -x)

# example variable error bar values
yerr = 0.1 + 0.1 * np.sqrt(x)

#Now switch to a more 00 interface to exercise moere features
fig,axs = plt.subplots(nrows= 1,ncols= 2, sharex= True,)
ax = axs[0]
ax.errorbar(x, y, yerr= yerr)
ax.set_title('all errprbars')

ax = axs[1]
ax.errorbar(x= x,y= y,yerr= yerr, errorevery= 2)
ax.set_title('only every 5th errorbar')

fig.suptitle('only every 5th errorbar')

fig.suptitle('Errorbar subsampling for better appearance')
plt.show()
