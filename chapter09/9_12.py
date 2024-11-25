from admin import Admin

admin = Admin("ryota", "nakatsuka", 24, "Osaka")

admin.privileges.privileges = ["投稿を追加する",
                            "投稿を削除する",
                            "ユーザーを利用禁止にする"]
admin.privileges.show_privileges()