# 切片输出
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
#可省略，默认最前或最后一个
print(players[:3])
print(players[0:])
#可输入负数，则输出倒数的几个
print(players[-3:])
#遍历切片
for player in players[0:3]:
    print(player.title())