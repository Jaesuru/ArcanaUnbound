import random


class Monster:
    def __init__(self, name, adjective, type_of_monster, hp, attack_damage):
        self.name = name
        self.adjective = adjective
        self.type_of_monster = type_of_monster
        self.hp = hp
        self.attack_damage = attack_damage

    def __str__(self):
        return f"{self.adjective} {self.name} ({self.type_of_monster}) - HP: {self.hp}, Attack Damage: {self.attack_damage}"

    def update_health(self, amount):
        self.hp += amount
        if self.hp <= 0:
            self.hp = 0
            print(f"\nThe {self.name} has been defeated.")
        else:
            print(f"\nThe {self.name}'s health is now {self.hp}.")


def generate_monster():
    adjectives = [
        "Ancient", "Fierce", "Mighty", "Haunting", "Cursed",
        "Silent", "Shambling", "Dreadful", "Shadowy", "Skeletal",
        "Grim", "Gloomy", "Tattered", "Spectral", "Ethereal",
        "Wraith-like", "Decayed", "Ravenous", "Horrific", "Pale", "Depressed"
    ]

    types = ["Zombie", "Skeleton", "Ghost"]

    adjective = random.choice(adjectives)
    type_of_monster = random.choice(types)

    # Define stats based on type
    if type_of_monster == "Zombie":
        hp = random.randint(50, 80)
        attack_damage = random.randint(2, 7)
    elif type_of_monster == "Skeleton":
        hp = random.randint(30, 60)
        attack_damage = random.randint(5, 10)
    elif type_of_monster == "Ghost":
        hp = random.randint(20, 40)
        attack_damage = random.randint(6, 12)

    name = f"{adjective} {type_of_monster}"

    return Monster(name=name, adjective=adjective, type_of_monster=type_of_monster, hp=hp, attack_damage=attack_damage)
