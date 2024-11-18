favorite_language = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

language = favorite_language["sarah"].title()
print(f"Sarahの好きなプログラミング言語は{language}です。")

for name, language in favorite_language.items():
    print(f"{name.title()}の好きなプログラミング言語は{language.title()}です。")

for name in favorite_language.keys():
    print(name.title())

friends = ["phil", "sarah"]
for name in favorite_language.keys():
    print(f"こんにちは{name.title()}。")

    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}、あなたの好きなプログラミング言語は`{language}ですね！")

if "erin" not in favorite_language.keys():
    print("Erin、投票してください")


for name in sorted(favorite_language.keys()):
    print(f"{name.title()}、投票ありがとう。")

print("以下の言語が投票されました。")
for language in favorite_language.values():
    print(language.title())

print("以下の言語が投票されました。")
for language in set(favorite_language.values()):
    print(language.title())


favorite_language = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskel"],
}

for name, languages in favorite_language.items():
    print(f"\n{name.title()}の好きな言語")
    for language in languages:
        print(f"\t{language.title()}")
        