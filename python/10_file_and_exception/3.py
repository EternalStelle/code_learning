#使用try:...except:...代码块，尝试执行try的内容，否则出现某个错误后执行except的内容
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
#简单的除法计算器
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")
while True:
    first_number=input("\nFirst number: ")
    if first_number=='q':
        break
    second_number=input("\nSecond number: ")
    if second_number=='q':
        break
    #使用try:...except:...else:...代码块
    try:
        #应使用int()，把输入的字符串转为数字
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't devide by zero!")
    else:
        print(f"Answer is {answer}")
