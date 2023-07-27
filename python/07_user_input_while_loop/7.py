unconfirmed_users=['alice','brain','candace']
confirmed_users=[]
#while循环的条件为unconfirmed_users列表不为空，为空时结束
while unconfirmed_users:
    current_user =unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print(f"\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())