# 打开文件，输出信息
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())
#逐行输出
with open('pi_digits.txt') as file_object:
    for line in file_object:
        # 此处调用.rstrip()清除多出的一行空白行
        print(line.rstrip())
