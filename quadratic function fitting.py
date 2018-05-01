# 1519100058 黄杰 第六次作业
# 二次函数拟合

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

plt.figure(figsize=(9,9))

x = np.linspace(-10,10,1000)
X = np.array([0,1,2,3,-1,-2,-3])
Y = np.array([-1.22,1.85,3.22,10.29,2.21,3.72,8.7])

def f(p):
    a,b,c=p
    return(Y-(a*X*X+b*X+c))

r=leastsq(f,[1,0,0])
a,b,c=r[0]
print("a=",a,"b=",b,"c=",c)

plt.scatter(X,Y, s=100, alpha=1.0, marker='o',label=u'数据点')

y=a*x*x+b*x+c

plt.plot(x, y, color='r',linewidth=5, linestyle=":",markersize=20, label=u'拟合曲线')

plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')

plt.xlabel(u'安培/A', fontsize=20)
plt.ylabel(u'伏特/V', fontsize=20)

plt.xlim(x.min() * 1.1, x.max() * 1.1)
plt.ylim(-10, y.max() * 1.1)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#刻度字体大小
plt.legend(loc='upper left')
plt.savefig('二次函数拟合.jpeg')

plt.show()
