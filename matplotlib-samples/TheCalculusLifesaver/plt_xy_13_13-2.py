import matplotlib.pyplot as plt  #导入matplotlib库
import numpy as np  #导入numpy库
import mpl_toolkits.axisartist as axisartist

#创建画布
fig = plt.figure(figsize=(8, 8))
#使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111)
#将绘图区对象添加到画布中
fig.add_axes(ax)

# 通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis[:].set_visible(False)
# ax.new_floating_axis代表添加新的坐标轴,new_floating_axis(0,0)第一个0代表平行直线，第二个0代表该直线经过0点
ax.axis["x"] = ax.new_floating_axis(0,0)
# 给x坐标轴加上箭头 空心箭头
ax.axis["x"].set_axisline_style("->", size = 1.0)
# 添加y坐标轴，且加上箭头 new_floating_axis(1,0)代表竖直曲线且经过0点
ax.axis["y"] = ax.new_floating_axis(1,0)
# 实心箭头
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
# 设置x、y轴上刻度显示方向
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right")

#生成x步长为0.1的列表数据
# x = np.arange(-15,15,0.1)
x = np.linspace(-10, 10, 1000)
#y数据
y=x-np.cos(x)

#设置x、y坐标轴的范围
plt.xlim(-10,10)
plt.ylim(-10,10)
#绘制图形
plt.plot(x,y, c='b')

plt.show()
