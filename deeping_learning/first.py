import numpy as np
# import tensorflow as tf
#
# hello = tf.constant('Hello, TensorFlow!')
# sess = tf.Session()
# sess.run(hello)
# a = tf.constant(10)
# b= tf.constant(32)
# sess.run(a+b)
import matplotlib.pyplot as plt
a = np.arange(-2,2,0.01)
# plt.plot(a,a ** 2,'o-')
import pandas as pd
# print(pd.Series(a))
import sklearn.datasets as dt
# print(dt.lfw.Bunch.keys())
def sigmoid(x):
	return 1 / (1 + np.exp(-x))
plt.plot(a,sigmoid(a))
plt.show()
