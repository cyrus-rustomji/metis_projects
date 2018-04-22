# subtract the candidates (2,7,1,5,10) by the 0 - 10 by tenths
# find the smallest result

import numpy as np
from matplotlib import pyplot as plt
data = [1,2,5,7,10]

lst = []

for i in np.arange(0,10.1,0.1):
	num = (data-i)
	sum_num = sum(num**2)
	lst.append(round(sum_num,2))
	i += 1
print(lst)
x = min(j for j in lst)
print(x)
x = np.arange(0,10.1,0.1)
y = lst
plt.scatter(x,y)
plt.show()