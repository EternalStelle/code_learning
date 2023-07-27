# 导入pizza.py文件，获得其中的make_pizza函数
# 使用方法为mudule_name.function_name()
import pizza

pizza.make_pizza(16, "pepperoni", "green peppers")
# 可使用from ... import...从指定文件中获得指定函数
# 调用时无需句点，直接使用
from pizza import make_pizza

make_pizza(16, "pepperoni", "green peppers")
# 获得函数后可as指定别名
from pizza import make_pizza as mp

mp(16, "pepperoni", "green peppers")

# 也可为模块(引用的文件)指定别名
import pizza as p

p.make_pizza(16, "pepperoni", "green peppers")

# 也可使用*导入所有函数，即可无需句点直接使用
# 但不建议使用，因其可能与已有的函数名重复
from pizza import *

make_pizza(16, "pepperoni", "green peppers")
