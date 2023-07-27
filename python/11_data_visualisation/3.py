import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = "SimSun"
fig, ax = plt.subplots()
# 绘制散点图，(x,y, s)s即为散点图点的大小
# range(1,1001)绘制一千个x点
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
# c即为颜色，s即为点的大小
# c可用颜色名，例：'red'，或RGB数值，例：(0,0.8,0)
# 亦可使用颜色映射，形成缓变的颜色变化，即cmap=plt.cm.{color},c=y_values，颜色随y坐标而变
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=2)
plt.grid(True, linestyle="-")
# 设定图表的标题，fontsize设定字体大小
ax.set_title("平方数", fontsize=24)
# 设定x坐标和y坐标的标识
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
# 设定坐标轴限度
ax.axis([0, 1000, 0, 1100000])
ax.tick_params(which="major", labelsize=14)
plt.show()
#可自动保存图片
#plt.savefig('squares_plot.png', bbox_inches='tight)
#后一个实参用于去除图片中的空白部分