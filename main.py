from classes.game import Person,bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 70}]

arr = {"name": "kartik", "age": 21}

Player = Person(460, 65, 60, 34, magic)

print(magic[0]["name"], ":", Player.generate_spell_damage(0))
print(magic[1]["name"], ":", Player.generate_spell_damage(1))
print(magic[1]["name"], ":", Player.generate_spell_damage(2))

