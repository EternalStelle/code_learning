import matplotlib.pyplot as plt
from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        # 存储随机漫步次数的变量
        self.num_points = num_points
        # 两个储存每个点的x与y坐标的列表
        # 初始值为(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            # x_direction前进方向
            # x_distance前进距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            # 不可原地踏步
            if x_step == 0 and y_step == 0:
                continue
            # 计算下个点
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            # 新点进入列表
            self.x_values.append(x)
            self.y_values.append(y)


rw = RandomWalk()
rw.fill_walk()
fig, ax = plt.subplots()
# c=x,cmap=plt.cm.color可渲染渐变色,并随x坐标变化而变化
ax.scatter(rw.x_values, rw.y_values, c=rw.x_values, cmap=plt.cm.Blues, s=15)
plt.show()
