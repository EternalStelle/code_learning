# for与if嵌套
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requseted_topping in requested_toppings:
    if requseted_topping == "green peppers":
        print("Sorry, we don't have green peppers.")
    else:
        print(f"Adding {requseted_topping}")
print("\nFinished making your pizza!")
# 可使用if判断列表是否为空，为空则返回False，至少有一个元素则返回True
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
# 可使用for-if嵌套完成遍历列表
available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "extra cheese",
]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, e don't have {requested_topping}.")
