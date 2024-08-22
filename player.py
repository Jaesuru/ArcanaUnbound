from utilities import type_text
from collections import Counter
from items import Item, HealthPotion, ManaPotion


class Player:
    def __init__(self, name, race, player_class, health=100, mana=50, inventory=None):
        self.name = name
        self.race = race
        self.player_class = player_class
        self.health = health
        self.mana = mana
        self.max_health = health  # Added max_health for potion usage
        self.max_mana = mana  # Added max_mana for potion usage
        self.inventory = inventory if inventory else []
        self.equipped_weapon = None

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                if isinstance(item, Item) and item.item_type == "Weapon":
                    self.equip_weapon(item_name)
                elif isinstance(item, HealthPotion) or isinstance(item, ManaPotion):
                    item.use(self)
                else:
                    type_text(f"\n* {item_name} cannot be used directly.")
                return
        type_text(f"\n* {item_name} is not in your inventory.")

    def display_info(self):
        return f"{self.name}, the {self.race} {self.player_class}"

    def update_health(self, amount):
        self.health += amount
        if self.health <= 0:
            self.health = 0
            type_text(f"{self.name} has been defeated.")
        else:
            type_text(f"{self.name}'s health is now {self.health}.")

    def update_mana(self, amount):
        self.mana += amount
        if self.mana < 0:
            self.mana = 0
            type_text(f"{self.name} has exhausted their mana.")
        else:
            type_text(f"{self.name}'s mana is now {self.mana}.")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        type_text(f"\n* {item} obtained.")

    def display_inventory(self):
        if self.inventory:
            # Count the occurrences of each item in the inventory by name
            inventory_counter = Counter(str(item) for item in self.inventory)
            inventory_list = ', '.join(f"[{item}] x{count}" if count > 1 else f"[{item}]"
                                       for item, count in inventory_counter.items())
            type_text(f"Your inventory: {inventory_list}")
        else:
            type_text("Your inventory is empty.")

    def equip_weapon(self, weapon_name):
        for item in self.inventory:
            if isinstance(item, Item) and item.name == weapon_name:
                self.equipped_weapon = item
                type_text(f"\n* {self.name} has equipped {item.name}.")
                return
        type_text(f"\n* {weapon_name} is not in your inventory.")