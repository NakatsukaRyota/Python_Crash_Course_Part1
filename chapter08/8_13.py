def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("良太", 
                            "中塚",
                            location="大阪",
                            field="社会学",
                            age=24)

print(user_profile)