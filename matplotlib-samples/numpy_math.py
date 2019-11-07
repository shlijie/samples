import numpy as np
import matplotlib.pyplot as plt

# print(x)
# 线性函数
# y = x
# y = 1/x

# 指数函数
# y = np.power(0.5, x)
# y = np.power(2, x)
# 有理函数
# y = (x*x-3*x+2)/(x-2)
# 指数函数
# y = np.exp(x)

# 三角函数 Trigonometric functions
# y = np.sin(x)
# y = np.cos(x)
# y = np.tan(x)
# y = np.arcsin(x)
# y = np.arccos(x)
# y = np.arctan(x)
# y = np.sin(x)/x
# y = x * np.sin(1/x)
# y = (1 - np.cos(x))/x
# 双曲函数
x = np.linspace(-5, 5, 1000)
y = np.sinh(x)
y2 = np.cosh(x)
# y = np.tanh(x)
# y = np.arcsinh(x)
# y = np.arccosh(x)
# y = np.arctanh(x)

#创建figure窗口
plt.figure(num=3, figsize=(8, 5))

# linestyle: '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
plt.plot(x,y,'r',linewidth=1,color='red',linestyle='solid')
plt.plot(x,y2,'r',linewidth=1,color='blue',linestyle='--')

#设置坐标轴范围
plt.xlim((-5, 5))
plt.ylim((-5, 5))

#设置坐标轴刻度
# my_x_ticks = np.arange(-5, 5, 0.5)
# my_y_ticks = np.arange(-5, 5, 0.5)
# plt.xticks(my_x_ticks)
# plt.yticks(my_y_ticks)

#显示
plt.show()
