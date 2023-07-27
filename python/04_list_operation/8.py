# 不可变列表，即元组，使用()，而非[]，一定有逗号，即使只有一个元素
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)
# 元组不可变，但可重新定义整个元组
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)
