import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = "SimSun"
fig, ax=plt.subplots()
#绘制散点图，(x,y, s)s即为散点图点的大小
x_values=[1,2,3,4,5]
y_values=[1,4,9,16,25]
ax.scatter(x_values,y_values,s=20)
plt.grid(True, linestyle="-")
# 设定图表的标题，fontsize设定字体大小
ax.set_title("平方数", fontsize=24)
# 设定x坐标和y坐标的标识
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
# 设定刻度的样式，axis即为坐标轴
ax.tick_params(axis="both",which='major' ,labelsize=14)
plt.show()