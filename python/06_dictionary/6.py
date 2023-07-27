# 可把字典放入列表中
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 20}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# 利用代码生成alien
aliens = []
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)
# 显示前5个
for alien in aliens[:5]:
    print(alien)
print(f"Total number of aliens: {len(aliens)}")
