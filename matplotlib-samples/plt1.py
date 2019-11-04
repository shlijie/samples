import numpy as np
import matplotlib.pyplot as plt
 
#x轴，y轴
x=[0,1]
y=[0,1]
#创建绘图对象
plt.figure()
#在当前绘图对象进行绘图（两个参数是x,y轴的数据）
plt.plot(x,y)

plt.xlabel("time(s)") #X轴标签
plt.ylabel("value(m)") #Y轴标签
plt.title("A simple plot") #标题
#保存图象
# plt.savefig("D:/easyplot.png")
plt.show()
