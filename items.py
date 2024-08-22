import random

from utilities import type_text


class Item:
    def __init__(self, name, item_type, damage=0, critical_chance=0):
        self.name = name
        self.item_type = item_type
        self.damage = damage
        self.critical_chance = critical_chance

    def __str__(self):
        return self.name

    def describe(self):
        description = f"{self.name}: Type: {self.item_type}"
        if self.damage > 0:
            description += f", Damage: {self.damage}"
        if self.critical_chance > 0:
            description += f", Critical Chance: {self.critical_chance}%"
        return description

    def calculate_damage(self):
        if random.random() < self.critical_chance / 100:
            return self.damage * 2  # Critical hit does 2x damage
        return self.damage


class HealthPotion(Item):
    def __init__(self, name="Health Potion"):
        super().__init__(name, item_type="Potion")

    def use(self, player):
        player.update_health(player.max_health - player.health)
        type_text(f"{player.name} used a {self.name} and restored health to full!")


class ManaPotion(Item):
    def __init__(self, name="Mana Potion"):
        super().__init__(name, item_type="Potion")

    def use(self, player):
        player.update_mana(player.max_mana - player.mana)
        type_text(f"{player.name} used a {self.name} and restored mana to full!")


def consume_potion(self, potion):
    if potion.item_type == "Health Potion":
        self.health = 100
        type_text(f"\n* {self.name} consumed a Health Potion and fully restored health.")
    elif potion.item_type == "Mana Potion":
        self.mana = 100
        type_text(f"\n* {self.name} consumed a Mana Potion and fully restored mana.")
    self.inventory.remove(potion)


def generate_random_weapon_name():
    adjectives = ["Ancient", "Mystic", "Cursed", "Enchanted", "Rusty", "Shiny", "Ordinary"]
    materials = ["Wooden", "Iron", "Golden", "Steel", "Bronze", "Bone"]
    nouns = ["Sword", "Staff", "Dagger"]

    adjective = random.choice(adjectives)
    material = random.choice(materials)
    noun = random.choice(nouns)
    return f"{adjective} {material} {noun}"


def create_weapon(player_class, generate_class_specific=True):
    item_type = "Weapon"

    # 5% chance to get a "Wooden Plank"
    if random.random() < 0.05:
        return Item(name="Wooden Plank", item_type=item_type, damage=20, critical_chance=85)

    # Generate a class-specific weapon if requested
    if generate_class_specific:
        specific_weapon = None
        if player_class == "Warrior":
            specific_weapon = "Sword"
        elif player_class == "Mage":
            specific_weapon = "Staff"
        elif player_class == "Rogue":
            specific_weapon = "Dagger"

        if specific_weapon:
            name = f"Class-Specific {specific_weapon}"
            # Define material damage additiveness
            material_damage_additives = {
                "Wooden": 0,  # No extra damage
                "Iron": 2,  # Adds 2 damage
                "Golden": 4,  # Adds 4 damage
                "Steel": 3,  # Adds 3 damage
                "Bronze": 1,  # Adds 1 damage
                "Bone": 0  # No extra damage
            }

            # Define adjective damage modifiers
            adjective_damage_modifiers = {
                "Ancient": 5,  # Adds 5 damage
                "Mystic": 3,  # Adds 3 damage
                "Cursed": -5,  # Subtracts 5 damage
                "Enchanted": 4,  # Adds 4 damage
                "Rusty": -2,  # Subtracts 2 damage
                "Shiny": 2,  # Adds 2 damage
                "Ordinary": 0  # No extra damage
            }

            # Generate the weapon name and extract properties
            weapon_name = generate_random_weapon_name()
            parts = weapon_name.split()
            adjective = parts[0]
            material = parts[1]
            noun = parts[-1]

            # Calculate damage with additive effects from material and adjective
            damage = random.randint(5, 15) + material_damage_additives.get(material, 0)
            damage += adjective_damage_modifiers.get(adjective, 0)

            # Set weapon-specific properties based on the noun
            if noun == "Sword":
                critical_chance = 35
            elif noun == "Staff":
                critical_chance = 25
            elif noun == "Dagger":
                critical_chance = 50

            return Item(name=name, item_type=item_type, damage=damage, critical_chance=critical_chance)

    # If no class-specific weapon was generated, return a random weapon
    name = generate_random_weapon_name()
    # Extract the adjective, material, and noun from the weapon name
    parts = name.split()
    adjective = parts[0]
    material = parts[1]
    noun = parts[-1]

    # Define default critical chance
    critical_chance = 0

    # Define material damage additiveness and adjective damage modifiers
    material_damage_additives = {
        "Wooden": 0,
        "Iron": 2,
        "Golden": 4,
        "Steel": 3,
        "Bronze": 1,
        "Bone": 0
    }
    adjective_damage_modifiers = {
        "Ancient": 5,
        "Mystic": 3,
        "Cursed": -5,
        "Enchanted": 4,
        "Rusty": -2,
        "Shiny": 2,
        "Ordinary": 0
    }

    # Calculate damage with additive effects
    damage = random.randint(5, 15) + material_damage_additives.get(material, 0)
    damage += adjective_damage_modifiers.get(adjective, 0)

    # Set weapon-specific properties based on the noun
    if noun == "Sword":
        critical_chance = 35
    elif noun == "Staff":
        critical_chance = 25
    elif noun == "Dagger":
        critical_chance = 50

    return Item(name=name, item_type=item_type, damage=damage, critical_chance=critical_chance)
