my_foods = ["pizza", "falafel", "carrot cake"]
# 可通过=复制列表，不可写friend_foods=myfoods，这样只是两个变量设为同一个列表
# 省略前后两个数即为整个列表
friend_foods = my_foods[:]
print("My favourite foods are:")
print(my_foods)
print("\nMy friend favourite foods are:")
print(friend_foods)
my_foods.append("cannoli")
friend_foods.append("ice cream")
print("My favourite foods are:")
print(my_foods)
print("\nMy friend favourite foods are:")
print(friend_foods)
