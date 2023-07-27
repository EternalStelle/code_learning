import matplotlib.pyplot as plt

# 导入宋体，支持中文显示
plt.rcParams["font.sans-serif"] = "SimSun"
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# 变量fig表示整张图片，变量ax表示图片中的各个图表
# 函数subplots()在一张图片中绘制一个或多个图表
fig, ax = plt.subplots()
# 使用内置样式(可选)
# plt.style.use('bmh')
# 渲染背景格线
plt.grid(True, linestyle="-")
# plot(输入,输出,其他参数)
ax.plot(input_values, squares, linewidth=3)
# 设定图表的标题，fontsize设定字体大小
ax.set_title("平方数", fontsize=24)
# 设定x坐标和y坐标的标识
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
# 设定刻度的样式，axis即为坐标轴
ax.tick_params(axis="both", labelsize=14)
plt.show()
