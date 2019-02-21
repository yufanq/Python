di = {}
di['ssds'] = 1
print(di['ssds'])
import  numpy as np
q = (2,2,2,2,2,2,1)
for i in q:
	a = np.random.rand(q[i],q[i +1])
	print(a)

qq = (2,2,3,2)
for i in range(len(qq)):
	np.random.rand(qq[i],qq[i])

for i in reversed(range(4)):  # 倒序
	print(i)