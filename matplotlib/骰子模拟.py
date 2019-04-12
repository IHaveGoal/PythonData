from random import randint
import pygal

#模拟1000次掷骰子的结果
results = []
side_num = 6
for num in range(1000):
    result = randint(1,side_num)
    results.append(result)
print(results)
#计算各个点数的次数
frequencies = []
for value in range(1,side_num+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

#绘制直方图
hist = pygal.Bar()
hist.title = ('1000次掷骰子')
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
#将标签以及列值添加到图表
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')
#图标太暗用浏览器打开