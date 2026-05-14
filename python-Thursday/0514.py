import numpy as np 

sample=([1.2,1.44,2.56],[5.2,6.44,7.56])
np.savetxt('data.csv',sample,delimiter=',',fmt='%1.4f')
a=np.loadtxt('data.csv',delimiter=',')
print(a)