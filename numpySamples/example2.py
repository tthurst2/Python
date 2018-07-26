import matplotlib.pyplot as plt
import numpy as np
import math as mth





x = np.array([1718,1767,1774,1775,1792,1816,1828,1834,1878,1906])
xNew = np.array([1718,1767,1774,1775,1792,1816,1828,1834,1878,1906, 2000])
y = np.array([0.5,0.8,1.4,2.7,4.5,7.5,12.0,17.0,17.2,23.0])
z = np.polyfit(x, y, 2)




xp = np.linspace(-2, 6, 100)
#plt.plot(x, y, '.',  xp, p(xp), '-', xp, p30(xp), '--')
# [<matplotlib.lines.Line2D object at 0x...>, <matplotlib.lines.Line2D object at 0x...>, <matplotlib.lines.Line2D object at 0x...>]
plt.ylim(-2,30)
plt.xlim(0,10)
yCalc = np.polyval(z, x)
print yCalc
print np.polyval(z,xNew)
def leastSquares(y, yCalc):

    sums = 0
    count = 0
    for i in np.nditer(y):
        j = yCalc[count] - y[count]
        count = count + 1
        sums = sums + j**2
        print "val ", np.ndindex(count + 1).ndincr(), "val 2 ", np.nditer(yCalc).value
        print j, j**2
    return sums
        
print  leastSquares(y,yCalc), " - Sum"
plt.plot(np.poly1d(np.polyval(z,x)),'.')
# (-2, 2)

plt.show()



