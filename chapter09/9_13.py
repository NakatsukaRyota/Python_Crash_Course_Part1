from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

die_6 = Die()
for i in range(1, 11):
    die_6.roll_die()

print("-----")

die_10 = Die(10)
for i in range(1, 11):
    die_10.roll_die()

print("-----")
die_20 = Die(20)
for i in range(1, 11):
    die_20.roll_die()


