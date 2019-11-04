import numpy as np
import matplotlib.pyplot as plt
 
x = np.linspace(0, 2 * np.pi, 20)
plt.figure(figsize=(6, 4))# 新建一个图像，设置图像大小
plt.plot(x, np.sin(x), 'ro-', label='sinx')# 设置颜色、标记符号、线型、图例标签
plt.plot(x, np.cos(x), 'b*--', label='cosx')
plt.title('plot curve', fontsize=25)# 标题
plt.xlim(-1, 7)# x轴范围
plt.ylim(-1.5, 1.5)# y轴范围
plt.xlabel('x', fontsize=20)# x轴标签
plt.ylabel('y', fontsize=20)# y轴标签
plt.legend(loc='best')# 图例
plt.show()
