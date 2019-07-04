from classes.game import Person,bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 70}]

arr = {"name": "kartik", "age": 21}

Player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True

print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attacks!" + bcolors.ENDC)

while running:
    print("===========================================")

    Player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = Player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "Points of damage. Enemy HP:", enemy.get_hp())

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    Player.take_damage(enemy_dmg)
    print("Enemy attacked for", enemy_dmg, "Player HP:", Player.get_hp())