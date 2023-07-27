motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
# 更改元素
motorcycles[0] = "ducati"
print(motorcycles)
# 附加元素
motorcycles.append("honda")
print(motorcycles)
# 插入元素.insert(位置，元素)
motorcycles.insert(1, "yayer")
print(motorcycles)
# 删除元素
del motorcycles[0]
print(motorcycles)
# 移除元素，默认最后一个
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)
# 根据值删除元素
# 也可令一变量为'yayer'，再用.remove(变量)
motorcycles.remove("yayer")
print(motorcycles)
