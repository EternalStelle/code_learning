cars = ["bmw", "audi", "toyota", "subaru"]
# 按字母顺序排序
cars.sort()
print(cars)
# 按字母顺序反向排序
cars.sort(reverse=True)
print(cars)
# 临时修改顺序显示
print(sorted(cars))
print(cars)
# 反向排序(与字母顺序无关)
cars.reverse()
print(cars)
#测量列表长度
print(len(cars))