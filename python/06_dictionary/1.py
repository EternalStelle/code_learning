# 创建alien_0字典，含有两个键，键分别赋值
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])
new_points = alien_0["points"]
print(f"You just earned {new_points} points!")
# 字典可动态添加
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
# 可创建空字典，再添加
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)
#可随时修改键值
alien_0['color']='yellow'
print(alien_0)
