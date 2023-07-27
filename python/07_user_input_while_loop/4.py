prompt = "Tell me something, and I'll repeat\n"
#active变量作为标志，以布尔量确认while循环的启动
active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)
