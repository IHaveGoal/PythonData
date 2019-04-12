import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    #创建与文件相关联的阅读器reader
    reader = csv.reader(f)
    #读出文件的下一行，只调用一次，所以得到第一行
    header_row = next(reader)
    #每个元素的索引和值
    for index, colum_header in enumerate(header_row):
        print(index, colum_header)
    #从第二行开始获取日期和最高气温
    dates,highs,lows = [],[],[]
    for row in reader:
        try:

            current_date = datetime.strptime(row[0],'%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
    #else放置try成功执行后运行的代码
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    print(highs)
    #自定义画布大小
    fig = plt.figure(dpi=128,figsize=(10,6))
    #dates横坐标，highs纵坐标，c颜色，alpha透明度（0是全透明，1不透明）
    plt.plot(dates,highs,c='red',alpha=0.5)
    plt.plot(dates,lows,c='blue',alpha=0.5)
    #facecolor填充颜色
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

    #设置图标表参数
    plt.title('Daily high and low temperatures of dath_valley-2014',fontsize=24)
    plt.xlabel('',fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature(F)',fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)
    plt.show()