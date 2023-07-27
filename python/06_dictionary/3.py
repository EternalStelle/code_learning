favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
language = favourite_languages["sarah"].title()
print(f"Sarah likes {language}")

alien_0 = {"color": "green", "speend": "medium"}
# 在不确定字典内容时，可使用get()而非方括号
point_value = alien_0.get("points", "There's no such value")
print(point_value)
#若get()无第二个值，且第一个值不存在，则返回None