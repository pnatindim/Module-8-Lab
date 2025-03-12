# Patric Natindim
# March 12 2025

# Checks whether the game character has picked up all the items needed to perform certain tasks and checks against any status debuffs
# Confirm checks with print statements

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses

player1 = character('', '', '')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']

for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)


def task_check(player):
    # Task 1
    task1_items = {'rope', 'coat', 'first aid kit'}
    task1_debuffs = {'slow'}

    # Task 2
    task2_items = {'pan', 'groceries'}
    task2_debuffs = {'small'}

    # Task 3
    task3_items = {'pen', 'paper', 'idea'}
    task3_debuffs_block = {'confusion'}

    inventory = set(player.weapons)
    debuffs = set(player.weaknesses)

    print("\nChecking Tasks:\n")

    # Check Task 1
    if task1_items.issubset(inventory):
        if not debuffs.intersection(task1_debuffs):
            print("Success")
        else:
            print("Failed, debuffs")
    else:
        print("Failed, missing items:")

    # Check Task 2
    if task2_items.issubset(inventory):
        if not debuffs.intersection(task2_debuffs):
            print("Success")
        else:
            print("Failed, debuffs")
    else:
        print("Failed, missing items:")

    # Check Task 3
    if task3_items.issubset(inventory):
        if not debuffs.intersection(task3_debuffs_block):
            print("Success")
        else:
            print("Failed, debuffs")
    else:
        print("Failed, missing items:")


task_check(player1)
