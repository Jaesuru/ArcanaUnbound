import random

from monsters import Monster


class Boss(Monster):
    def __init__(self, name, adjective, type_of_monster, hp, attack_damage):
        super().__init__(name, adjective, type_of_monster, hp, attack_damage)
        self.type_of_monster = "Overlord"

    def __str__(self):
        return f"{self.name} ({self.type_of_monster}) - HP: {self.hp}, Attack Damage: {self.attack_damage}"


def generate_boss():
    names = [
        "Chad", "Varyn", "Eldrin", "Malakar", "Zarvok", "Draven", "Rogar", "Krelthar",
        "Vorlak", "Thorne", "Aric", "Gorath", "Belgar", "Nerith", "Zephyros", "Eldor", "Drake"
    ]
    adjectives = [
        "Powerhouse", "Frail", "Depressed", "Prideful", "Glorious", "Mighty", "Bumbling",
        "Fearsome", "Grumpy", "Hilarious", "Ethereal", "Wrathful", "Luminous", "Cursed",
        "Majestic", "Wicked", "Freaky"
    ]
    titles = [
        "Overlord of Doom", "Overlord of Despair", "Overlord of the Nine Realms",
        "Overlord of the Universe", "Overlord of the Lost Souls",
        "Overlord of the Laughing Dead", "Overlord of the Abyss", "Overlord of Shadows",
        "Overlord of Eternal Night", "Overlord of the Forgotten", "Overlord of Chaos",
        "Overlord of Madness", "Overlord of the Infernals", "Overlord of the Celestials",
        "Overlord of the Deep", "Freaky Overlord"
    ]

    name = f"{random.choice(names)}"
    adjective = f"{random.choice(adjectives)}"
    title = f"{random.choice(titles)}"
    full_name = f"{name}, {adjective} {title}"

    # Adjust stats based on the adjective
    if adjective in ["Powerhouse", "Mighty", "Fearsome", "Wrathful"]:
        hp = random.randint(200, 300)
        attack_damage = random.randint(15, 30)
    elif adjective in ["Frail", "Depressed", "Bumbling", "Grumpy"]:
        hp = random.randint(100, 150)
        attack_damage = random.randint(5, 15)
    else:
        hp = random.randint(130, 200)
        attack_damage = random.randint(10, 25)

    return Boss(name=full_name, adjective=adjective, type_of_monster="Overlord", hp=hp, attack_damage=attack_damage)

# Example usage:
# boss = generate_boss()
# print(boss)
