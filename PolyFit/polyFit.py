import numpy as np
import matplotlib.pyplot as plt

x = np.array([1718,1767,1774,1775,1792,1816,1828,1834,1878,1906])
y = np.array([0.5,0.8,1.4,2.7,4.5,7.5,12.0,17.0,17.2,23.0])
z = np.polyfit(x, y, 3)
p30 = np.poly1d(np.polyfit(x, y, 9))
plt.plot(z)
#plt.plot(x,y)
plt.show()
