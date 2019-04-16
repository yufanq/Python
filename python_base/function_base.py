# page = download_page()
# freqs = compute_frequencies(page)
# for word, fred in freqs:
# 	print(word,freq)
#

# 自定义函数

import math
x = 1
y = math.sqrt
# 判断一个对象是否可调用
callable(x)
callable(y)

def hello(name):
	return "Hello," + name + "!"

def fibs(num):
	result = [0,1]
	for i in range(num - 2):
		result.append(result[ -2] + result--1)
	return result

def square(x):
	'Calculates the square of the number x'
	return x * x

square.__doc__ #访问文档字符串
# 函数的属性

def test():
	print('This is printed')
	return
	print('This is not')

def change(n):
	n[0] = 'M'

names = ['MT','T']
change(names)

names = ['M','T']
n = names[:]
n is names
n == names
# 创建副本
change(names[:])
