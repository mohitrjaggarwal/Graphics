import numpy as np
from mpl_toolkits.mplot3d import axes3d 
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
x = [1,2,3,4,5,6,7,8,9]

p = np.array(x)
q = np.array(p*p)
r = np.array(p*p+q*q)

plt.plot(p,q,r)
plt.show()








