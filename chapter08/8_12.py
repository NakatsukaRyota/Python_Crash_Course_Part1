def make_sandwitch(*sandwitches):
    print("\n以下のサンドウィッチを作成します。")
    for sandwatch in sandwitches:
        print(f"-{sandwatch}")

make_sandwitch("たまご")
make_sandwitch("たまご", "チーズ")
make_sandwitch("たまご", "チーズ", "レタス")