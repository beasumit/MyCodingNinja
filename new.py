import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,40,2)
y = x

x1 = [0,1,2,3,4,5,6,7,9,10]
y1 = [1,2,5,10,17,26,37,50,82,101]

plt.plot(x1, y1, label='x[i]=x[i]^2 +1')
plt.plot(x, y, label='x[i]=y[i]')
plt.ylabel('Y')
plt.xlabel('X')
plt.legend()
plt.show()
print("0 to 10")
print("25 to 35")