lists = ["マルクス", "ウェーバー", "ディルケム"]

print(f"{lists[0].title()}さん、一緒に夕食はいかがですか。")
print(f"{lists[1].title()}さん、一緒に夕食はいかがですか。")
print(f"{lists[2].title()}さん、一緒に夕食はいかがですか。")

print(f"{lists[0].title()}さんが参加できなくなりました。")

lists[0] = "ジンメル"
print(f"{lists[0].title()}さん、一緒に夕食はいかがですか。")
print(f"{lists[1].title()}さん、一緒に夕食はいかがですか。")
print(f"{lists[2].title()}さん、一緒に夕食はいかがですか。")