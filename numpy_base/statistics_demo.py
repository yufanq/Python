import numpy as np
'''
随机抽样
https://docs.scipy.org/doc/numpy/reference/routines.random.html
	随机数的生成  样例
	
	函数名     
	rand            [0,1) 
	randn           标准正态分布
	randint         离散均匀分布
	random_sample   连续均匀分布
'''

#rand
print(np.random.rand(2,2,2).shape)

#randn
'''
	对于随机样本N（\ mu，\ sigma ^ 2），请使用：

			sigma * np.random.randn(...) + mu
'''
print(np.random.randn(2,2))

#randint
print(np.random.randint(low=1,high=10,size=(10),dtype=np.int))

#random_sample
np.random.seed(3)
print(np.random.random_sample((2,3)))
print(np.random.random((2,5)))
np.random.seed(3)
print(np.random.ranf((2,3)))


print(np.random.beta(2,3,(3,2)))