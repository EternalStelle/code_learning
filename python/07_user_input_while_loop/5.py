prompt = "Tell me something, and I'll repeat\n"
# 利用break跳出循环
while True:
    city = input(prompt)
    if city == "quit":
        break
    else:
        print(f"I'd love to go to city {city}")
