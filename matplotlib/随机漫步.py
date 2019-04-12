from random import choice

class RandomWork():

    def __init__(self,num=50000):
        self.num = num
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        while len(self.x_values) < self.num:
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)


import matplotlib.pyplot as plt

# 模拟多次速随机漫步
while True:

    rw = RandomWork()
    rw.fill_walk()
    point_num = list(range(rw.num))
    plt.scatter(rw.x_values,rw.y_values,c=point_num,cmap=plt.cm.Blues,
                edgecolor='none',s=1)

    #突出起点、终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=10)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                s=10)

    plt.show()
    keep = input('Make another walk ?')
    if keep == 'n':
        break