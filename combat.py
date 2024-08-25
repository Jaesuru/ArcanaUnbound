# combat.py
import os
import random
import sys
import time

from items import HealthPotion, create_weapon, ManaPotion, generate_graveyard_items, Item
from utilities import lines, type_text


class Combat:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def calculate_damage(self):
        if self.player.equipped_weapon:
            weapon = self.player.equipped_weapon
            return weapon.damage + random.randint(0, 5)
        else:
            return random.randint(1, 5)

    def player_turn(self):
        print()
        lines(34)
        type_text("Your turn! What do you want to do?")
        type_text("1. <A>ttack")
        type_text("2. <U>se an item")
        type_text("3. <F>lee\n")
        lines(34)

        type_text("Choose an action:")
        print("> ", end="")
        choice = input()

        if choice == '1' or choice == 'A' or choice == 'a':
            attack_damage = self.calculate_damage()
            type_text(f"\n* You attack the {self.monster.name} for {attack_damage} damage!")
            self.monster.update_health(-attack_damage)
            time.sleep(2)
        elif choice == '2' or choice == 'U' or choice == 'u':
            item_name = input("\nEnter the name of the item to use: ")
            self.player.use_item(item_name)
        elif choice == '3' or choice == 'F' or choice == 'f':
            type_text("\nYou attempt to flee!")
            if random.random() < 0.5:  # 50% chance to flee
                type_text("\nYou successfully flee from the battle.")
                return False
            else:
                type_text("\nYou fail to flee and must continue the fight.")
        return True

    def monster_turn(self):
        attack_damage = self.monster.attack_damage
        type_text(f"\n* The {self.monster.name} attacks you for {attack_damage} damage!\n")
        self.player.update_health(-attack_damage)
        time.sleep(2)

    def start_combat(self):
        type_text(f"\nThe {self.monster.name} appears! Commence battle!")
        while self.player.health > 0 and self.monster.hp > 0:
            if not self.player_turn():
                break
            if self.monster.hp <= 0:
                type_text(f"\nYou have defeated the {self.monster.name}!")
                loot = self.generate_loot()
                if loot:
                    type_text("\nYou found the following loot:")
                    for item in loot:
                        self.player.add_to_inventory(item)
                else:
                    type_text(f"\nThe {self.monster.name} didn't have any goods on it, unfortunately.")
                self.monster = None
                time.sleep(2)
                type_text("\nExiting battle...")
                time.sleep(1)
                break
            self.monster_turn()
            if self.player.health <= 0:
                type_text(f"\nYou have been defeated by the {self.monster.name}.\n")
                time.sleep(1)
                type_text(f"As you lie down in defeat, {self.monster.name} hits you with a quick emote before leaving.")
                time.sleep(2)
                type_text("\n...\n")
                time.sleep(2)
                type_text("You're blacking out. This is the end of this journey.")
                type_text("... but it won't be the last.")
                type_text("Goodbye for now.")
                time.sleep(3)
                sys.exit()

    def generate_loot(self):
        loot = []
        if random.random() < 0.5:
            potion_type = random.choice(["Health Potion", "Mana Potion"])
            loot.append(
                HealthPotion(name=potion_type) if potion_type == "Health Potion" else ManaPotion(name=potion_type))

        if random.random() < 0.5:
            if random.random() < 0.6:
                loot.append(generate_graveyard_items())
            else:
                loot.append(create_weapon(self.player))

        if random.random() < 0.5:
            gold_amount = random.randint(10, 100)
            loot.append(Item(name="Pouch o' Gold", item_type="Currency", value=gold_amount))

        return loot
