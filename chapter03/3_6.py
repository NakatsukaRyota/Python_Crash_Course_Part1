lists = ["マルクス", "ウェーバー", "ディルケム"]

print(f"{lists[0].title()}さん、一緒に夕食はいかがですか。")
print(f"{lists[1].title()}さん、一緒に夕食はいかがですか。")
print(f"{lists[2].title()}さん、一緒に夕食はいかがですか。")

print(f"{lists[0].title()}さんが参加できなくなりました。")

lists[0] = "ジンメル"
print(f"{lists[0].title()}さん、一緒に夕食はいかがですか。")
print(f"{lists[1].title()}さん、一緒に夕食はいかがですか。")
print(f"{lists[2].title()}さん、一緒に夕食はいかがですか。")

print("大きなテーブルを見つけました")

lists.insert(0, "パーソンズ")
lists.insert(3, "マートン")
lists.insert(5, "アンデルセン")

print(f"{lists[0].title()}さん、一緒に夕食はいかがですか。")
print(f"{lists[1].title()}さん、一緒に夕食はいかがですか。")
print(f"{lists[2].title()}さん、一緒に夕食はいかがですか。")
print(f"{lists[3].title()}さん、一緒に夕食はいかがですか。")
print(f"{lists[4].title()}さん、一緒に夕食はいかがですか。")
print(f"{lists[5].title()}さん、一緒に夕食はいかがですか。")