name = "ada lovelace"
# .title()将name首字母大写
print(name.title())
# .upper()将name每个字母大写
print(name.upper())
# .lower()将name每个字母小写
print(name.lower())
# f字符串
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
full_name = f"Hello, {first_name.title()} {last_name.title()}"
print(full_name)