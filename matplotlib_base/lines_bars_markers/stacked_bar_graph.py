import numpy as np
import matplotlib.pyplot as plt
'''
直方图
bar
	bottom  底层的y坐标
			默认为0
			设置成其他可追加在其他数据上
	
	yerr

plt.xticks
	对应刻度位置的X轴标签
	
'''
N = 5
menMeans = (20,35,50,35,27)
womenWeans = (25, 32, 34, 20, 25)

menStd = (2,5,4,1,2)
womenStd = (3, 5, 2 ,3, 3)

ind =np.arange(N) # the x locations for the groups
width =  0.35 # the width of the bars :can also be len(x)

p1 = plt.bar(ind, menMeans, width, yerr= menStd)
p2 = plt.bar(ind, menMeans, width, bottom=menMeans, yerr = womenStd)

plt.xlabel('G') # X轴标签
plt.ylabel('Scores') # Y轴标签
plt. title('Scores by group and gender') # 设置标题
plt.xticks(ind,('G1','G2','G3','G4','G5'))
plt.yticks(np.arange(0,81,10))
plt.legend((p1[0],p2[0]),('Men','Women'))
plt.show()