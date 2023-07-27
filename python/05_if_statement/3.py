# 只要缩进相同，即视作同一代码块
age = 19
if age >= 18:
    print("You are allowed to vote!")
    print("Have you registered?\n")
age = 17
if age >= 18:
    print("You are allowed to vote!")
    print("Have you registered?\n")
else:
    print("You can't be here.")
    print("sorry.\n")
# 多重判断，其中使用elif
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
# elif可多次使用
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")
