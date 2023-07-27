# 位置形参可与任意形参合用，任意形参位于最后
def make_pizza(size, *toppings):
    print(f"Making a size of {size} -inch, with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, "pepperoni", "green peppers")


# 任意数量的关键字形参
# func(**x)表示任意的关键字形参，创建了名为x的字典
def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics"
)
print(user_profile)