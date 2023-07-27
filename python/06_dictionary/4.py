user_0 = {"username": "efermi", "first": "enrico", "last": "fermi"}
# .items()返回键值对表，for循环将其分别赋予两个变量
for key, value in user_0.items():
    print(f"key:{key}")
    print(f"Value:{value}\n")

favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
# 仅需键名则可用.keys()，也可什么都不用for name in favourite_languages:
for name in favourite_languages.keys():
    print(name.title())

firends = ["phil", "sarah"]
for name in favourite_languages.keys():
    print(f"Hi, {name.title()}")
    if name in firends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you like {language}!")
