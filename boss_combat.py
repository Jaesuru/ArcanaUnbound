import random
import sys
import time

from items import HealthPotion, create_weapon, ManaPotion, generate_graveyard_items, Item, create_powerful_weapon
from utilities import lines, type_text


class BossCombat:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def calculate_damage(self):
        if self.player.equipped_weapon:
            weapon = self.player.equipped_weapon
            return weapon.damage + random.randint(0, 5)
        else:
            return random.randint(1, 5) + 1000

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
            type_text(f"\n* You attack {self.monster.name} for {attack_damage} damage!")
            self.monster.update_health(-attack_damage)
            time.sleep(2)
        elif choice == '2' or choice == 'U' or choice == 'u':
            item_name = input("\nEnter the name of the item to use: ")
            self.player.use_item(item_name)
        elif choice == '3' or choice == 'F' or choice == 'f':
            type_text("\nYou attempt to flee!")
            if random.random() < 0:
                type_text("\nYou successfully flee from the battle.")
                return False
            else:
                type_text("\nIt's too late to give up now!")
        return True

    def monster_turn(self):
        attack_damage = self.monster.attack_damage
        type_text(f"\n* {self.monster.name} attacks you for {attack_damage} damage!\n")
        responses = {
            "Powerhouse": [
                f"<{self.monster.name}>: \"That’s right, feel the power of my brute force!\"",
                f"<{self.monster.name}>: \"Did you think you could withstand my might?\"",
                f"<{self.monster.name}>: \"Your defenses are no match for my strength!\"",
                f"<{self.monster.name}>: \"You’re about to learn what real power feels like!\"",
                f"<{self.monster.name}>: \"Hope you’re ready for more, because I’m just getting started!\""
            ],
            "Frail": [
                f"<{self.monster.name}>: \"Oh no, I might need to sit down after that!\"",
                f"<{self.monster.name}>: \"Careful, I’m on the brink of falling apart!\"",
                f"<{self.monster.name}>: \"That hit nearly shattered me!\"",
                f"<{self.monster.name}>: \"I’m barely holding together, don’t push it!\"",
                f"<{self.monster.name}>: \"Ugh, I’m more fragile than I thought!\""
            ],
            "Depressed": [
                f"<{self.monster.name}>: \"Another hit... just add it to the pile of my misfortunes.\"",
                f"<{self.monster.name}>: \"Your attacks don’t really brighten my day.\"",
                f"<{self.monster.name}>: \"Great, just what I needed... more damage.\"",
                f"<{self.monster.name}>: \"I guess I’ll just add that to my list of woes.\"",
                f"<{self.monster.name}>: \"Even your hits can’t shake my gloomy outlook.\""
            ],
            "Prideful": [
                f"<{self.monster.name}>: \"Is that all you’ve got? My pride is unshaken!\"",
                f"<{self.monster.name}>: \"Your attacks are nothing but a minor inconvenience to my grandeur!\"",
                f"<{self.monster.name}>: \"My pride stands tall, even against your feeble strikes!\"",
                f"<{self.monster.name}>: \"You’ll need more than that to dent my dignity!\"",
                f"<{self.monster.name}>: \"Your blows are as insignificant as a gnat on a lion!\""
            ],
            "Glorious": [
                f"<{self.monster.name}>: \"Your hits are but a shadow compared to my glory!\"",
                f"<{self.monster.name}>: \"Even in pain, I radiate splendor!\"",
                f"<{self.monster.name}>: \"Your attacks are as fleeting as a star against my brilliance!\"",
                f"<{self.monster.name}>: \"You can’t diminish my grandeur with your blows!\"",
                f"<{self.monster.name}>: \"I stand majestic despite your petty attacks!\""
            ],
            "Mighty": [
                f"<{self.monster.name}>: \"You’ve only felt a fraction of my might!\"",
                f"<{self.monster.name}>: \"Your attacks are nothing compared to my true power!\"",
                f"<{self.monster.name}>: \"Prepare yourself, I’m just warming up!\"",
                f"<{self.monster.name}>: \"That was a mere gust compared to my mighty force!\"",
                f"<{self.monster.name}>: \"Feel the full impact of my strength!\""
            ],
            "Bumbling": [
                f"<{self.monster.name}>: \"Oops, did I mess that up?\"",
                f"<{self.monster.name}>: \"Sorry, I’m a bit off today. That hit was a fluke!\"",
                f"<{self.monster.name}>: \"Did I really just let that happen?\"",
                f"<{self.monster.name}>: \"Whoops, I didn’t mean to make that hit so noticeable.\"",
                f"<{self.monster.name}>: \"Well, wasn’t that a clumsy move?\""
            ],
            "Fearsome": [
                f"<{self.monster.name}>: \"Feel the full brunt of my terror!\"",
                f"<{self.monster.name}>: \"Your attacks only fuel my wrath and fear!\"",
                f"<{self.monster.name}>: \"You’re about to experience true fear!\"",
                f"<{self.monster.name}>: \"Your hits are nothing compared to the dread I bring!\"",
                f"<{self.monster.name}>: \"Prepare to be overwhelmed by terror!\""
            ],
            "Grumpy": [
                f"<{self.monster.name}>: \"Ugh, more trouble from you?\"",
                f"<{self.monster.name}>: \"Can’t a monster have a moment of peace?\"",
                f"<{self.monster.name}>: \"Great, just what I needed—more annoyance.\"",
                f"<{self.monster.name}>: \"Couldn’t you find a better way to spend your time?\"",
                f"<{self.monster.name}>: \"Just another thing to add to my list of annoyances.\""
            ],
            "Hilarious": [
                f"<{self.monster.name}>: \"Is that the best you can do? I’m laughing at your attempts!\"",
                f"<{self.monster.name}>: \"Your hits are as funny as your jokes!\"",
                f"<{self.monster.name}>: \"Oh, I’m having a good laugh with every hit!\"",
                f"<{self.monster.name}>: \"You’re more entertaining than you are dangerous!\"",
                f"<{self.monster.name}>: \"I haven’t had this much fun in ages!\""
            ],
            "Ethereal": [
                f"<{self.monster.name}>: \"Your attacks barely touch my otherworldly form.\"",
                f"<{self.monster.name}>: \"Even in pain, my ethereal presence remains undiminished.\"",
                f"<{self.monster.name}>: \"Your hits are like whispers to my intangible being.\"",
                f"<{self.monster.name}>: \"You’re just grazing the surface of my ethereal essence.\"",
                f"<{self.monster.name}>: \"Your blows are mere distractions to my ghostly form.\""
            ],
            "Wrathful": [
                f"<{self.monster.name}>: \"Your hits only add fuel to my burning wrath!\"",
                f"<{self.monster.name}>: \"Prepare to face the full fury of my anger!\"",
                f"<{self.monster.name}>: \"You’ve ignited a storm of rage within me!\"",
                f"<{self.monster.name}>: \"Your attacks only serve to stoke the flames of my wrath!\"",
                f"<{self.monster.name}>: \"You’ll pay dearly for provoking my anger!\""
            ],
            "Luminous": [
                f"<{self.monster.name}>: \"Your attacks can’t dim the radiance of my light!\"",
                f"<{self.monster.name}>: \"Even your blows are overshadowed by my brilliance!\"",
                f"<{self.monster.name}>: \"My light remains undiminished by your minor strikes!\"",
                f"<{self.monster.name}>: \"You can’t eclipse my radiance with your attacks!\"",
                f"<{self.monster.name}>: \"I shine too brightly to be affected by your hits!\""
            ],
            "Cursed": [
                f"<{self.monster.name}>: \"Your attacks are nothing compared to the curse I bear!\"",
                f"<{self.monster.name}>: \"You think you can add to my suffering with your blows?\"",
                f"<{self.monster.name}>: \"Your strikes are mere trifles compared to my eternal curse!\"",
                f"<{self.monster.name}>: \"Even with your hits, I remain burdened by a far worse fate!\"",
                f"<{self.monster.name}>: \"My curse is a greater torment than anything you could inflict!\""
            ],
            "Majestic": [
                f"<{self.monster.name}>: \"Your attacks are mere trifles to my majestic presence!\"",
                f"<{self.monster.name}>: \"Even your blows are beneath my royal dignity!\"",
                f"<{self.monster.name}>: \"My grandeur stands untouched by your minor strikes!\"",
                f"<{self.monster.name}>: \"Your hits are as insignificant as a jest in my court!\"",
                f"<{self.monster.name}>: \"I rise above your attacks with regal grace!\""
            ],
            "Wicked": [
                f"<{self.monster.name}>: \"Your attacks amuse me more than they harm!\"",
                f"<{self.monster.name}>: \"You think you can bother a heart as wicked as mine?\"",
                f"<{self.monster.name}>: \"Your hits are a mere distraction from my wicked plans!\"",
                f"<{self.monster.name}>: \"Even in pain, my wickedness endures!\"",
                f"<{self.monster.name}>: \"Your blows are nothing compared to the malice I harbor!\""
            ]
        }

        adjective = self.monster.adjective
        response = random.choice(responses.get(adjective, ["I have no words for this attack."]))

        type_text(f"{response}\n")

        self.player.update_health(-attack_damage)
        time.sleep(2)

    def start_combat(self):
        type_text(f"\n{self.monster.name} makes his appearance! Commence battle!")
        while self.player.health > 0 and self.monster.hp > 0:
            if not self.player_turn():
                break
            if self.monster.hp <= 0:
                monster_name = str(self.monster.name)
                type_text("\n<" + monster_name + ">: \"That's it? That's how it ends? Damn you...\"")
                time.sleep(2)
                type_text(f"\n* Congratulations! You defeated {self.monster.name}!")
                loot = self.generate_loot()
                if loot:
                    type_text("\nYou found the following loot:")
                    for item in loot:
                        self.player.add_to_inventory(item)
                else:
                    type_text(f"\n{self.monster.name} didn't have any goods on it somehow, unfortunately.")
                self.monster = None
                time.sleep(2)
                type_text("\nExiting battle...")
                time.sleep(1)
                break
            self.monster_turn()
            if self.player.health <= 0:
                type_text(f"\nYou have been defeated by {self.monster.name}.\n")
                time.sleep(1)
                type_text(f"{self.monster.name} taunts you while you slowly perish.")
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
        if random.random() < 1:
            potion_type = random.choice(["Health Potion", "Mana Potion"])
            loot.append(
                HealthPotion(name=potion_type) if potion_type == "Health Potion" else ManaPotion(name=potion_type))

        if random.random() < 1:
            if random.random() < 1:
                loot.append(create_powerful_weapon(player_class=any, generate_class_specific=True))
            else:
                loot.append(create_weapon(self.player))

        if random.random() < 1:
            gold_amount = random.randint(100, 1001)
            loot.append(Item(name="Bag o' Gold", item_type="Currency", value=gold_amount))

        return loot
