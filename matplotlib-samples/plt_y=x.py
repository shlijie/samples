import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-100, 100, 10000)
# print(x)
# 线性函数
# y = x
# y = 1/x
# 三角函数
# y = np.sin(x)
# y = np.sin(x)/x
# y = x * np.sin(1/x)
y = (1 - np.cos(x))/x
# 指数函数
# y = np.power(0.5, x)
# y = np.power(2, x)
# 有理函数
# y = (x*x-3*x+2)/(x-2)

plt.plot(x,y,'r',linewidth=1)
plt.show()
