#Python自带一系列的库
# randint随机数函数，返回随机整数
from random import randint
print(randint(1,6))
# choice返回随机列表或元组元素
from random import choice
players=['charles','martina','michael','florance','eli']
first_up=choice(players)
print(first_up)
