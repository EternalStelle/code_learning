# 利用while循环删除列表中的所有某个内容
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)
while "cat" in pets:
    pets.remove("cat")
print(pets)
# 建立responses空字典
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("Would you like to let another person to respond?")
    if repeat == "no":
        polling_active = False
print("\n---poll Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")
