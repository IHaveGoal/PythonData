import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    #创建与文件相关联的阅读器reader
    reader = csv.reader(f)
    #读出文件的下一行，只调用一次，所以得到第一行
    header_row = next(reader)
    #每个元素的索引和值
    for index, colum_header in enumerate(header_row):
        print(index, colum_header)
    #从第二行开始获取日期和最高气温
    dates,highs = [],[]
    for row in reader:

        current_date = datetime.strptime(row[0],'%Y-%m-%d')
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)
    print(highs)
    #根据数据绘制图表
    fig = plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,highs,c='red')
    #设置图标表参数
    plt.title('Daily high temperatures,July 2014',fontsize=24)
    plt.xlabel('',fontsize=16)
    #x轴倾斜显示
    fig.autofmt_xdate()
    plt.ylabel('Temperature(F)',fontsize=16)
    #设置刻度标记的的大小
    plt.tick_params(axis='both',which='major',labelsize=16)
    plt.show()