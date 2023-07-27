# 导入csv模块
import csv
# 导入matplotlib
import matplotlib.pyplot as plt
#导入中文字体
plt.rcParams["font.sans-serif"] = "SimSun"

filename = "D:\Download\sample4.csv"
with open(filename) as f:
    # 调用csv.reader()把文件读取
    reader = csv.reader(f)
    # next()返回文件中的下一行，调用一次即为第一行
    header_row = next(reader)
    print(header_row)

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # 对列表使用enumerate()获得每个元素的索引及其值
    for index, column_header in enumerate(header_row):
        print(index, column_header)

#获取数据
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #注意缩进
    nums=[]
    for row in reader:
        #由于前面已读取第一行，此处即从第二行开始读取
        #row[1]即为前面获得的元素索引
        num=int(row[1])
        nums.append(num)
fig,ax=plt.subplots()
ax.plot(nums,c='red')
ax.set_title("数据变化情况")
ax.set_xlabel('x',fontsize=16)
ax.set_ylabel('y',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)
plt.show()