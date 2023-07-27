# input()函数，参数为向用户输出的提示
message = input("Tell me something, and I will repeat\n")
print(message)
name = input("Please enter your name:\n")
print(f"Hello, {name.title()}!")
prompt = "If you tell me "
prompt += "something, and I will repeat\n"
name = input(prompt)
print(name)
