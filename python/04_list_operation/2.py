# 利用range(a, b)生成由a到(b-1)的数，也可range(b)，将由0开始
for value in range(1, 5):
    print(value)
for value in range(5):
    print(value)
# 利用list创建列表
numbers = list(range(1, 6))
print(numbers)
# 利用range可指定步长range(a, b, step)
for value in range(1, 10, 2):
    print(value)
