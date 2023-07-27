# 可把列表放入字典中
pizza = {"crust": "thick", "toppings": ["mushrooms", "extra cheese"]}
print(f"You ordered a {pizza['crust']} - crust pizza" " with the following toppings:")
for topping in pizza["toppings"]:
    print(f"+{topping}")

favourite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
}
#此处for有2个变量
for name,languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")