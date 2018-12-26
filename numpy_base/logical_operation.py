import numpy as np

'''
	逻辑运算   demo
		与           同真为真
		或           同假为假
		非           真为假，假为真
		异或         相同为假，相异为真

'''
#测试数据
a = np.array([1,1,0,        0])
b = np.array([1,0,1,0])

# and 与
print(np.logical_and(a,b)) # [ True False False False]
# or 或
print(np.logical_or(a,b)) # [ True  True  True False]
#not 非
print(np.logical_not(a)) #[False False  True  True]
#xor 异或
print(np.logical_xor(a,b)) #[False  True  True False]