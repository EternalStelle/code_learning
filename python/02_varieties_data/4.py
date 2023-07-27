# Python单双引号均可用于字符串
favourite_language = 'python '
print(favourite_language.rstrip())
# .rstrip()暂时移除字符串右边的空白
# 永久移除应修改变量
favourite_language = favourite_language.rstrip()
print(favourite_language)
favourite_language = " Python "
# .lstrip()暂时移除字符串左边的空白
# .strip()暂时移除左右两边的空白，永久移除应修改变量
print(favourite_language.lstrip())
print(favourite_language.strip())
