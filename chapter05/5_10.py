current_users = ["Ryo", "reo", "coco", "yako", "admin"]
new_users = ["ryo", "reo", "aaa", "user", "cat"]
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"ユーザー名{user}は使用できません。")
    else:
        print(f"ユーザー名{user}は使用可能です。")

    