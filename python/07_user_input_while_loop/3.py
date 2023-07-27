current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
prompt = "\nTell me something, and I will repeat\n"
# 先创建message字符串，以供比较才可进入while循环
message = ""
while message != "quit":
    message = input(prompt)
#使用if判断，防止quit也被输出
    if message != "quit":
        print(message)
