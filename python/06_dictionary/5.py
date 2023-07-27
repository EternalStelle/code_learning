favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")
#使用.values()返回值列表
print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())
#可使用集合set()来使返回的值独一无二，集合中每个元素独一无二
print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())