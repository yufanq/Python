import matplotlib.pyplot as plt
import numpy as np

'''
	设置点的样子
	def setp(obj, *args, **kwargs):
        return _setp(obj, *args, **kwargs)

'''
def f(t):
	"A damped exponential"

	s1 = np.cos(2 * np.pi * t)
	e1 = np.exp(-t)

	return s1 * e1
t1 = np.arange(0.0,5.0, .2)

line = plt.plot(t1,f(t1),'ro')

plt.setp(line,markersize=30)
plt.setp(line,markerfacecolor='C0')

plt.show()