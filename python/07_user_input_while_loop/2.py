# 使用int()获取数值输入，只有数值才可做比较
age = input("How old are you?\n")
age = int(age)
print(age)
# %求模运算
number=input("Enter a number, I'll tell it if it's odd or even\n")
number=int(number)
if number%2==0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")