alien_0 = {}

alien_0["color"] = "green"
alien_0["points"] = 5


print(alien_0)
del alien_0["points"]
print(alien_0)

alien_0 = {"color": "green", "points": 5}

print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(alien_0)

alien_0 = {"color": "green"}
print(f"エイリアンは{alien_0['color']}です。")

alien_0["color"] = "yellow"
print(f"エイリアンは{alien_0['color']}になりました。")


alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"最初のX座標:{alien_0['x_position']}")

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment

print(f"新しいX座標:{alien_0['x_position']}")

alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "poinst": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []
for alien in range(30):
    new_alien = {"color":"green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15

for alien in aliens[:5]:
    print(alien)
print("...")

print(f"全エイリアンの数:{len(aliens)}")