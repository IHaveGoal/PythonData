import matplotlib.pyplot as plt

x_value = list(range(1,1001))
y = [x**2 for x in x_value]
#scatter绘制点
plt.scatter(x_value,y,c=(0,0,0.8),edgecolor='none',s=5)
#设置x,y坐标范围
plt.axis([0,1100,0,1100000])
plt.show()