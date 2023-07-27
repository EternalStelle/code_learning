current_number = 0
# continue跳出循环，并重新进入循环
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
