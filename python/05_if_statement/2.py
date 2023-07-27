age_0 = 22
age_1 = 18
# 判断多个条件同时满足使用and连接
if age_0 >= 21 and age_1 >= 21:
    print("yes!")
else:
    print("No!")
# 判断多个条件至少一个满足使用or连接
if age_0 >= 21 or age_1 >= 21:
    print("yes!")
else:
    print("No!")
# 判断某元素是否存在于列表中使用in
requested_toppings = ["mushrooms", "onions", "pineapple"]
if "mushrooms" in requested_toppings:
    print("Yes!")
else:
    print("No!")
# 判断某元素是否不存在于列表中使用not in
banned_users = ["anderw", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, you are allowed to post.")
# 布尔表达式
game_active = True
can_edit = False
