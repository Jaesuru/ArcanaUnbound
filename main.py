import sys
import time
import random

from boss import generate_boss
from boss_combat import BossCombat
from combat import Combat
from items import create_weapon, HealthPotion, ManaPotion, generate_graveyard_items, Item
from monsters import generate_monster
from player import Player
from utilities import type_text, type_text_fast, lines
from rooms import generate_forest_name, Room, generate_description_forest, \
    generate_graveyard_name, generate_description_graveyard, generate_description_boss_castle, generate_boss_castle_name

player = None
introduction_done = None


def get_name_length(name):
    return len(name) + 1


def name_line_maker(name):
    length = get_name_length(name)
    print("+" + '=' * length + "+")


def print_ascii_art():
    ascii_art = """
   _____                                      ____ ___     ___.                            .___
  /  _  \\_______   ____ _____    ____ _____  |    |   \\____\\_ |__   ____  __ __  ____    __| _/
 /  /_\\  \\_  __ \\_/ ___\\\\__  \\  /    \\\\__  \\ |    |   /    \\| __ \\ /  _ \\|  |  \\/    \\  / __ | 
/    |    \\  | \\/\\  \\___ / __ \\|   |  \\/ __ \\|    |  /   |  \\ \\_\\ (  <_> )  |  /   |  \\/ /_/ | 
\\____|__  /__|    \\___  >____  /___|  (____  /______/|___|  /___  /\\____/|____/|___|  /\\____ | 
        \\/            \\/     \\/     \\/     \\/             \\/    \\/                  \\/      \\/
    """
    lines(95)
    print(ascii_art)
    lines(95)


def wait_for_enter():
    type_text("\nPress Enter to Play...")
    input()


def get_input(prompt, options=None):
    invalid_responses = [
        "That's not a valid input. Please try again.",
        "Hmm, that doesn't seem right. Try again.",
        "A voice from afar beckons out to you, \"Try again...\"",
        "Unrecognized input. Please try again.",
        "Invalid input, try reading the prompt again."
    ]

    while True:
        type_text(prompt)
        print("> ", end="")
        choice = input().capitalize()
        if options is None or choice in options:
            return choice
        type_text(random.choice(invalid_responses))


def introduction():
    global player, introduction_done
    lines(38)
    type_text("Welcome to the world of ArcanaUnbound.")
    lines(38)
    time.sleep(.5)
    type_text("\n* Starting game...")
    time.sleep(2)

    if introduction_done:
        type_text("\n<???>: \"Ah, it’s you again. It seems you’re familiar with this place.\"")
        time.sleep(1)
        type_text("<???>: \"Since you already know who you are, we'll skip the formalities.\"")
        time.sleep(1)
        type_text("\n<???>: \"Let's get straight to the action.\"")
        time.sleep(2)
        type_text("\n* Loading game...\n")
        time.sleep(2)
        return player

    else:
        dialogues = [
            [
                "\nYou slowly regain consciousness in a dimly lit room, a place that feels strangely familiar.",
                "The air is thick with an eerie silence, with a slight cold breeze.",
                "You can't shake the feeling that you’ve been here before.",
                "A figure emerges from the darkness, their features obscured by a shroud of mystery.",
                "\n<???>: \"Ah, another soul. It seems you’ve found your way here, again or not.\"",
                "<???>: \"Do you remember why you're here?\"",
                "...",
                "<???>: \"Probably not.\"",
                "<???>: \"You see, this realm is ruled by an overlord whose power keeps us all bound here.\"",
                "<???>: \"Your task, should you choose to accept it, is to confront and defeat this overlord.\"",
                "<???>: \"Only then will you be able to break free from this purgatory.\""
            ],
            [
                "\nYour eyes slowly open, revealing a darkened space filled with faint memories.",
                "The air carries a chill, and the silence is almost deafening.",
                "A strange sense of déjà vu washes over you.",
                "From the shadows, a figure steps forward.",
                "\n<???>: \"Ah, another traveler has arrived. Have you been here before?\"",
                "<???>: \"Do you recall why you have come?\"",
                "...",
                "<???>: \"No? I thought not.\"",
                "<???>: \"This place is ruled by a powerful overlord, keeping all souls bound.\"",
                "<???>: \"Your mission, if you dare to undertake it, is to defeat the overlord.\"",
                "<???>: \"Only then can you hope to escape this cursed place.\""
            ],
            [
                "\nYou awaken in a shadowy room, the atmosphere heavy with an eerie stillness.",
                "A faint breeze brushes against your skin, carrying a coldness that seeps into your bones.",
                "The surroundings feel oddly familiar, yet distant.",
                "A mysterious figure materializes from the darkness, their presence both unsettling and intriguing.",
                "\n<???>: \"Another soul finds its way here. Do you remember this place?\"",
                "<???>: \"Do you know why you’ve come?\"",
                "...",
                "<???>: \"As I suspected, you don’t.\"",
                "<???>: \"This realm is under the control of an overlord whose power binds us all.\"",
                "<???>: \"You must face and defeat this overlord if you wish to be free.\"",
                "<???>: \"Your only hope lies in breaking the chains that hold us all.\""
            ]
        ]

        selected_dialogue = random.choice(dialogues)

        for line in selected_dialogue:
            type_text(line)
            time.sleep(1)

        while True:
            print()
            lines(60)
            print()
            player_name = get_input("\"Now then, what is your name?\"")
            type_text(f"\nYou have chosen the name: {player_name}")
            confirmation = get_input("Is this correct? (Y/N)", options=['Y', 'N'])
            if confirmation == 'Y':
                break

        races = {
            'H': 'Human',
            'E': 'Elf',
            'D': 'Dwarf',
            'Human': 'Human',
            'Elf': 'Elf',
            'Dwarf': 'Dwarf',
        }

        while True:
            type_text("\n")
            lines(60)
            type_text("Choose your race:")
            type_text("1. <H>uman")
            type_text("2. <E>lf")
            type_text("3. <D>warf")
            race_choice = get_input("\n\"What is your race?\"", options=races.keys())
            player_race = races[race_choice]
            type_text(f"\nYou have chosen the race: {player_race}")
            confirmation = get_input("Is this correct? (Y/N)", options=['Y', 'N'])
            if confirmation == 'Y':
                break

        classes = {
            'W': 'Warrior',
            'M': 'Mage',
            'R': 'Rogue',
            'Warrior': 'Warrior',
            'Mage': 'Mage',
            'Rogue': 'Rogue'
        }

        while True:
            type_text("\n")
            lines(60)
            type_text("Choose your class:")
            type_text("1. <W>arrior")
            type_text("2. <M>age")
            type_text("3. <R>ogue")
            class_choice = get_input("\n\"Finally, what is your class?\"", options=classes.keys())
            player_class = classes[class_choice]
            type_text(f"\nYou have chosen the class: {player_class}")
            confirmation = get_input("Is this correct? (Y/N)", options=['Y', 'N'])
            if confirmation == 'Y':
                break

        player = Player(player_name, player_race, player_class)

        type_text(f"\n* Hero {player.display_info()} was created.")
        time.sleep(2)
        type_text("\n\"Well alright, it's about time for you to wake up now for real this time.\"")
        time.sleep(3)
        type_text("\nYou feel your consciousness fade away...")
        time.sleep(2)
        type_text("\n* Loading game...\n")
        time.sleep(2)

        introduction_done = False

    return player


def starting_room_intro():
    global player
    forest_name, adjective = generate_forest_name()
    forest_description = generate_description_forest(adjective)
    random_forest_room = Room(name=forest_name, description=forest_description)
    name_line_maker(random_forest_room.description)
    random_forest_room.describe()
    name_line_maker(random_forest_room.description)

    def get_introduction_text():
        intros = [
            [
                "\nYou slowly regain consciousness.",
                "The first thing you notice is the rustling of nearby leaves, carried by a gentle breeze.",
                "As you open your eyes, you see the canopy of a dense forest, with the moonlight shining through.",
                "You're lying on a bed of soft, verdant grass that feels cool against your skin.",
                "In the distance, you can hear the soothing sound of a gentle water stream flowing.",
                "The air is fresh and crisp, carrying the subtle scent of pine and earth."
            ],
            [
                "\nYou awaken with a start, your senses gradually returning.",
                "The sound of rustling leaves greets your ears as a soft breeze caresses your face.",
                "Above, the canopy of a dense forest filters the moonlight, casting dappled shadows on the ground.",
                "You find yourself on a bed of cool, soft grass, the earth beneath you solid and reassuring.",
                "Nearby, the gentle murmur of a stream adds to the tranquility of the scene.",
                "The air is crisp and carries the faint, refreshing scent of pine and damp earth."
            ],
            [
                "\nConsciousness slowly returns to you, like a distant memory.",
                "You hear the rustle of leaves as a gentle breeze flows through the trees, touching your skin.",
                "Your eyes flutter open to see the towering trees of a dense forest, bathed in soft moonlight.",
                "You're lying on a bed of lush grass, its coolness a welcome sensation against your body.",
                "The peaceful sound of a nearby stream trickles through the air, adding to the serenity.",
                "The fresh, pine-scented air fills your lungs, grounding you in this tranquil moment."
            ]
        ]

        return random.choice(intros)

    def play_introduction():
        introduction_text = get_introduction_text()
        for line in introduction_text:
            type_text(line)

    play_introduction()

    while True:
        choice = get_input("\nGet Up? (y/n)", options=['Y', 'N'])
        if choice == 'Y':
            type_text("\nYou push yourself up from the grass and stand up, ready to explore the environment.")
            type_text("\nYou are now ready to start your adventure.")
            break
        elif choice == 'N':
            type_text("\nYou decide to stay on the grass a bit longer, admiring the serenity of the environment")
            type_text("After some time, you feel more refreshed and decided whether to get up.")

            while True:
                choice = get_input("\nWill you get up now? (y/n)", options=['Y', 'N'])
                if choice == 'Y':
                    type_text("\nYou push yourself up from the grass and stand up, ready to explore the environment.")
                    type_text("\nYou are now ready to start your adventure.")
                    break
                elif choice == 'N':
                    type_text("\nYou continue to lie on the grass, enjoying the peaceful surroundings.")
                    time.sleep(1)
                    type_text("...")
                    time.sleep(3)
                    type_text("After a while, a voice from afar beckons you to arise.")
                    time.sleep(.5)
                    type_text("\n<???>: \"This is no time for a leisure nap!\"")
                    time.sleep(2)

                    while True:
                        choice = get_input("\nDo you give up your free will? (y/n)", options=['Y', 'N'])
                        if choice == 'Y':
                            type_text(
                                "\nYou exert yourself, and finally push yourself up from the grass to stand up.")
                            type_text("\nYou feel powerful.")
                            break
                        elif choice == 'N':
                            type_text("\nYou decided that there were better things to do and kept still.")
                            time.sleep(1)
                            type_text("...")
                            time.sleep(1)
                            type_text("However, a sudden powerful gust of wind blew you to your feet.")
                            time.sleep(2)

                            type_text(f"\n* {player.display_info()} is now finally standing.")
                            break
                    break
            break
    time.sleep(1)

    def display_random_message1():
        messages = [
            "\nAs you look around, you notice a glint from the corner of your eye afar.",
            "\nA faint shimmer catches your attention from a distance as you scan your surroundings.",
            "\nFrom a quick glimpse, you detect a subtle gleam in the far distance."
        ]
        type_text(random.choice(messages))

    lines(95)
    type_text_fast("""

             .                      .
             .                      ;
             :                  - --+- -
             !           .          !
             |        .             .
             |_         +
          ,  | `.
    --- --+-<#>-+- ---  --  -
          `._|_,'
             T
             |
             !
             :         . : 
             .       *
    """)

    lines(95)

    display_random_message1()

    def handle_special_explore_case1():
        actions = {
            'A': 'attack',
            'T': 'taunt',
            'E': 'examine',
            'X': 'explore the glint in the distance',
            'B': 'open your backpack'
        }

        def display_choices():
            print()
            lines(23)
            type_text("What do you want to do?", 0.05)
            type_text("1. <A>ttack")
            type_text("2. <T>aunt")
            type_text("3. <E>xamine")
            type_text("4. <X>plore")
            type_text("5. <B>ackpack")

        while True:
            display_choices()  # Display choices each time the loop starts
            action_choice = get_input("\nChoose an action:", options=actions.keys())
            action = actions.get(action_choice, None)  # Use .get() to handle invalid inputs gracefully

            if action is None:
                type_text("\nInvalid choice. Please choose again.")
                continue

            type_text(f"\nYou chose to {action.lower()}.")
            time.sleep(1)

            if action_choice == 'X':
                time.sleep(1)
                type_text("\nYou make your way toward the glint and discover something intriguing.")
                break
            else:
                if action_choice == 'A':
                    type_text("\nYou prepare to attack, but you winded up just to swing your fist into nothing.")
                elif action_choice == 'T':
                    type_text(
                        "\nYou taunt into the distance, but all you receive were the sound of distant crickets chirping.")
                elif action_choice == 'E':
                    type_text("\nYou examine the verdant surroundings, and can confirm that you haven't moved yet.")
                elif action_choice == 'B':
                    type_text("\nYou open your backpack, and there seems to be something!")
                    time.sleep(.5)
                    type_text("...")
                    time.sleep(2)
                    type_text("It was just a piece of lint.")
                    type_text("You toss it aside.")

    handle_special_explore_case1()


def obtaining_weapon():
    while True:
        type_text("As you wonder through the lush, leafy passageways,")
        type_text("a glimmering light catches your eye from beneath the thick undergrowth.")
        time.sleep(1)
        type_text("Curious, you brush aside the foliage and uncover a partially buried chest.")
        type_text("It looks like it has been waiting here for ages.")
        time.sleep(1)

        choice = get_input("\nWill you open it? (y/n)", options=['Y', 'N'])
        if choice == 'Y':
            type_text("\nYou carefully lift the chest's lid, revealing loot inside.")
            type_text("It looks like it could be very useful for your adventure!")
            break
        elif choice == 'N':
            type_text("\nYou decide to leave the chest for now and continue exploring.")
            type_text("But as you move away, the faint glint seems to beckon you back.")
            time.sleep(2)
            type_text("After a moment, you find yourself drawn back to the chest.")
            type_text("It seems fate has a way of guiding you towards it.")
            time.sleep(1)
            break

    def starter_chest():
        items = []
        for _ in range(3):
            weapon = create_weapon(player)
            items.append(weapon)

        for _ in range(3):
            health_potion = HealthPotion()
            items.append(health_potion)

        for _ in range(3):
            mana_potion = ManaPotion()
            items.append(mana_potion)

        random.shuffle(items)

        for item in items:
            player.add_to_inventory(item)

    starter_chest()


def subroom_start():
    variations = [
        (
            "\nA generous assortment of loot, surely to be invaluable in your adventure.",
            "Just make sure you know how to use them...",
            "\nAfter a short time of admiring the newly acquired loot, you decided it was",
            "finally time to advance and prepare yourself for the harsh journey ahead of you.",
            "\nIn the distance, a hazy, fog-like opening reveals itself to you."
        ),
        (
            "\nYou find an impressive array of items, all of which seem to radiate with power.",
            "These will undoubtedly aid you on your journey.",
            "\nAfter a moment of excitement over your new treasures, you sense the urgency to move forward.",
            "The road ahead is long, and you must be prepared.",
            "\nAhead, you notice a hazy, fog-like opening beckoning you onward."
        ),
        (
            "\nThe loot before you is vast and varied, each piece calling out with potential.",
            "Choosing wisely will be key to your success.",
            "\nWith your newfound resources, you feel a surge of confidence, knowing the journey will be tough.",
            "But you're ready to face whatever comes next.",
            "\nA shine in the distance catches your eye—a hazy, fog-like opening through the dense surroundings."
        )
    ]

    selected_text = random.choice(variations)

    for line in selected_text:
        type_text(line)

    time.sleep(1)
    type_text("\nWithout thinking about it much, you decide to go towards it.\n")
    time.sleep(1)
    type_text("...")
    time.sleep(2)
    type_text("\nWhen you open your eyes, an entirely new scenery reveals itself to you.\n")

    graveyard_name = generate_graveyard_name()
    adjective = graveyard_name.split()[0]
    graveyard_description = generate_description_graveyard(adjective)

    graveyard_room = Room(name=graveyard_name, description=graveyard_description)

    name_line_maker(graveyard_room.description)
    graveyard_room.describe()
    name_line_maker(graveyard_room.description)

    def generate_graveyard_description():
        variations = [
            [
                "A shroud of mist clings to the gravestones, whispering forgotten names.",
                "Broken headstones jut from the earth like jagged teeth in the darkness.",
                "The ground is uneven, with graves half-buried and rotting.",
                "An oppressive silence fills the air, broken only by distant, unsettling noises.",
                "Twisted shadows dance across the graveyard, as if alive.",
                "Cold, damp air makes your skin crawl, hinting at unseen horrors."
            ],
            [
                "A ghostly fog swirls around you, making every step feel haunted.",
                "Weathered tombstones lean precariously, their inscriptions eroded by time.",
                "A chill in the air makes your breath visible, adding to the gloom.",
                "Soft, eerie moans drift from the shadows, hinting at restless spirits.",
                "Ancient trees groan under their own weight, casting ominous shapes.",
                "The ground is littered with cracked bones and forgotten trinkets."
            ],
            [
                "A thick mist weaves between the crumbling graves, obscuring the path ahead.",
                "Gravestones are cracked and worn, their inscriptions barely readable.",
                "The air is heavy with the scent of decay, mingling with the cold night air.",
                "Unseen creatures scuttle in the darkness, their presence felt but not seen.",
                "The eerie glow of the moonlight casts long, sinister shadows over the cemetery.",
                "An unsettling stillness pervades, as if the graveyard itself is holding its breath."
            ]
        ]

        selected_variation = random.choice(variations)

        for line in selected_variation:
            type_text(line)

    generate_graveyard_description()

    time.sleep(1)
    type_text("\n...\n")
    time.sleep(1)
    type_text("As you were beginning to think you were alone, a familiar voice reaches out to you.")

    type_text("<???>: \"Greetings, " + player.name + ". I am here to offer you a very helpful tip.")
    type_text("<???>: in this time of difficulty you are experiencing.\"")
    type_text("\n...\n")
    time.sleep(1)
    type_text(
        "<???>: \"It would be advisable for you to examine your environment first before making any rash decisions.\"")
    time.sleep(2)
    type_text("\n<???>: \"Anywho, toodles!\"")
    type_text("\nYou are alone once again.")

    def handle_special_explore_case2():
        actions = {
            'A': 'attack',
            'T': 'taunt',
            'E': 'examine',
            'X': 'explore',
            'B': 'backpack'
        }

        def display_choices():
            print()
            lines(23)
            type_text("What do you want to do?", 0.05)
            type_text("1. <A>ttack")
            type_text("2. <T>aunt")
            type_text("3. <E>xamine")
            type_text("4. <X>plore")
            type_text("5. <B>ackpack")

        def backpack_menu():
            type_text("\nYou opened your backpack.")
            while True:
                player.display_inventory()

                type_text("\nWhat would you like to do?")
                type_text("1. Use an item")
                type_text("2. Equip a weapon")
                type_text("3. Go back")

                choice = get_input("\nChoose an option:", options=['1', '2', '3'])

                if choice == '1':
                    item_name = get_input("\nEnter the name of the item to use:")
                    player.use_item(item_name)
                elif choice == '2':
                    weapon_name = get_input("\nEnter the name of the weapon to equip:")
                    player.equip_weapon(weapon_name)
                elif choice == '3':
                    type_text("\nReturning to the main menu.")
                    break
                else:
                    type_text("\nInvalid choice. Please choose again.")

        examined = False
        monster = None

        while True:
            display_choices()
            action_choice = get_input("\nChoose an action:", options=actions.keys())
            action = actions.get(action_choice, None)

            if action is None:
                type_text("\nInvalid choice. Please choose again.")
                continue

            if not examined and action_choice in ['A', 'T', 'X']:
                type_text("\nYou aren't sure what's out there, maybe try examining your surroundings first.")
                continue

            type_text(f"\nYou chose to {action.lower()}.\n")
            time.sleep(1)

            if action_choice == 'E':
                if not examined:
                    examined = True

                    tombstone_options = [
                        "You notice broken tombstones partially covered with creeping vines.",
                        "Amongst the broken tombstones, you spot something shiny partially hidden.",
                        "The old tombstones are overgrown with thick vines, concealing an intriguing object.",
                        "Among the crumbling tombstones, a glint of something metallic catches your eye."
                    ]

                    statue_options = [
                        "Old, weathered statues with eroded features stand sentinel over the graves.",
                        "Weathered statues, their features almost worn away by time, dot the graveyard.",
                        "The statues here are ancient and covered in moss, their details lost to the ages.",
                        "Weathered statues loom in the darkness, their forms barely visible under the moonlight."
                    ]

                    symbol_options = [
                        "Strange symbols carved into the stone faintly glow under the moonlight.",
                        "Carvings on the stones seem to shimmer with an otherworldly light.",
                        "You notice eerie symbols etched into the stone, glowing faintly in the gloom.",
                        "The moonlight reveals mysterious symbols carved into the weathered stones."
                    ]

                    corpse_options = [
                        "In the shadow of a mourning willow tree, a decrepit corpse lays slumped.",
                        "A decaying body lies hidden in the shadows of an ancient willow.",
                        "You see a corpse, long forgotten, sprawled beneath the mourning branches of a willow tree.",
                        "There's a forlorn figure, half-buried under the drooping branches of a willow."
                    ]

                    def rnd_tmb():
                        type_text(random.choice(tombstone_options))
                        item1 = generate_graveyard_items()
                        player.add_to_inventory(item1)

                    def rnd_stat():
                        type_text(random.choice(statue_options))

                    def rnd_symbol():
                        type_text(random.choice(symbol_options))

                    def rnd_corpse():
                        type_text(random.choice(corpse_options))
                        gold_bag = Item("Pouch o' Gold", "Currency", "0", "0", "100")
                        player.add_to_inventory(gold_bag)

                    def gen_mon():
                        monster = generate_monster()
                        return monster

                    options = [rnd_tmb, rnd_stat, rnd_symbol, rnd_corpse]
                    random.shuffle(options)
                    for option in options:
                        option()

                    if random.random() < 1:
                        monster = gen_mon()
                        type_text_fast("""
                    ,-\\__\\
                    |f-"Y\\|
                    \\()7L/
                     cgD                            __ _
                     |\\(                          .'  Y '>,
                      \\ \\                        / _   _   \\
                       \\\\                       )(_) (_)(|}
                        \\\\                      {  4A   } /
                         \\\\                      \\uLuJJ/\\l
                          \\\\                     |3    p)/
                           \\\\___ __________      /nnm_n//
                           c7___-__,__-)\\,__)(".  \\_>-<_/D
                                      //V     \\_"-._.__G G_c__.-__<"/ ( \\
                                             <"-._>__-,G_.___)\\   \\7\\
                                            ("-.__.| "\\"<.__.-" )   \\ \\
                                            |"-.__"\\  |"-.__.-".\\   \\ \\
                                            ("-.__"". "\\"-.__.-".|    \\_\\
                                            \\"-.__""|!|"-.__.-".)     \\ \\
                                             "-.__""\\_|"-.__.-"./
                            """)

                        lines(95)
                        type_text(f"\nIn addition to these discoveries, you spot a {monster.name} lurking nearby.")
                        type_text("They seem to be minding their own business, but you keep them within your vision.")

                    time.sleep(1)
                else:
                    type_text("\nYou have already examined your surroundings.")

            elif action_choice == 'X':
                variations1 = [
                    [
                        "\nAfter closely inspecting your surroundings, you notice that one of the",
                        "paths seems to lead to a familiar fog-shrouded exit.",
                        "With curiosity piqued, you decide to venture forth."
                    ],
                    [
                        "\nAs you carefully study the area, you realize that one of the",
                        "trails appears to lead to a mist-covered exit you've seen before.",
                        "You feel drawn to explore it."
                    ],
                    [
                        "\nAfter thoroughly surveying the terrain, you discern that one of the",
                        "routes leads to a well-known, fog-laden exit.",
                        "Feeling a sense of familiarity, you choose to follow it."
                    ]
                ]

                selected_variation = random.choice(variations1)

                for line1 in selected_variation:
                    type_text(line1)
                break

            elif action_choice == 'A':
                if monster:
                    type_text(f"\nYou attack the {monster.name}! Entering combat...")
                    combat = Combat(player, monster)
                    combat.start_combat()
                else:
                    type_text("\nThere's no monster around to attack.")

            elif action_choice == 'T':
                if monster:
                    type_text(f"\nYou attempt to taunt the {monster.name}.")
                    taunts = [
                        f"\nThe {monster.name} rolls its eyes and groans, 'Not this again!'",
                        f"\nThe {monster.name} stares at you blankly, as if questioning its life choices.",
                        f"\nThe {monster.name} bursts into tears, mumbling that 'you've hurt its feelings.'",
                        f"\nThe {monster.name} grumbles, 'I’ve seen scarier things in a bedtime story.'",
                        f"\nThe {monster.name} gets a little too introspective and wonders if it's truly evil.",
                        f"\nThe {monster.name} shakes its head in disbelief, muttering, 'This is why I work alone.'",
                        f"\nThe {monster.name} looks at you with pity and says, 'I thought you were the brave hero?'",
                        f"\nThe {monster.name} dramatically clutches its chest, pretending to faint from your words.",
                        f"\nThe {monster.name} suddenly has a mid-life crisis and starts questioning its monster career.",
                        f"\nThe {monster.name} sarcastically claps, 'Bravo! Truly the best taunt I've heard all day!'",
                        f"\nThe {monster.name} seems unimpressed and says, 'You might want to stick to being quiet.'",
                        f"\nThe {monster.name} side-eyes you, and pretends you didn't say or do anything.",
                        f"\nThe {monster.name} becomes depressed from your taunting, saying it \"was the last straw.\"",
                        f"\nThe {monster.name} is going to do unspeakable horrors to you because of what you did."
                    ]

                    taunt = random.choice(taunts)
                    type_text(taunt)

                else:
                    type_text("\nThere's no monster around to taunt.")

            elif action_choice == 'B':
                backpack_menu()

    handle_special_explore_case2()


def boss_level():
    castle_name = generate_boss_castle_name()
    adjective = castle_name.split()[0]
    castle_description = generate_description_boss_castle(adjective)

    castle_room = Room(name=castle_name, description=castle_description)

    name_line_maker(castle_room.description)
    castle_room.describe()
    name_line_maker(castle_room.description)

    variations = [
        [
            "Curiously, what you anticipated to be a lengthy journey appears to have brought you to your ultimate destination.",
            "It seems that your adventure has reached its conclusion far sooner than expected.",
            "\n...\n",
            "* Certainly no shortcuts were taken by the developer here..."
        ],
        [
            "In an unexpected twist, the journey you expected to be arduous has seemingly led you right to the end.",
            "What you thought would be an epic trek has culminated in what looks like your final stop.",
            "\n...\n",
            "* Absolutely no shortcuts were involved in this ending..."
        ],
        [
            "Oddly enough, your adventure, which you believed would stretch on indefinitely, has brought you to a surprising final destination.",
            "It looks like your journey is wrapping up far earlier than anticipated.",
            "\n...\n",
            "* Definitely not a case of the developer cutting corners..."
        ],
        [
            "It’s peculiar how what you expected to be a prolonged quest has ended up at what appears to be your final goal.",
            "Your journey seems to have reached its end much quicker than you had imagined.",
            "\n...\n",
            "* Totally not a sign of the developer taking the easy route..."
        ],
        [
            "Strangely, the journey you thought would be an epic saga has brought you to what seems like the end.",
            "What was expected to be a lengthy adventure appears to have come to an abrupt conclusion.",
            "\n...\n",
            "* No developer shortcuts were used in crafting this ending..."
        ]
    ]

    selected_variation = random.choice(variations)

    for line in selected_variation:
        type_text(line)

    time.sleep(2)

    dialogue_variations = [
        [
            "\nSuddenly, the floor beneath you begins to tremble, and you feel an immense aura coming towards you.\n",
            "<???>: \"It seems a mere puny being decided to drop in for a visit.\"",
            "<???>: \"How amusing. But if you wish to test your worth, you'll have to prove yourself.\"",
            "<???>: \"Prepare yourself, for you are about to face a true challenge!\"",
            "\nThe air crackles with tension as the foe readies themselves for battle.",
            "With a determined glare, they advance, ready to engage in combat."
        ],
        [
            "\nThe ground quakes ominously beneath you as a dark energy begins to swirl around.\n",
            "<???>: \"So, the insignificant wanderer has arrived. How delightful.\"",
            "<???>: \"If you believe you are worthy, then you will have to show me your strength.\"",
            "<???>: \"Brace yourself; a trial of epic proportions awaits you!\"",
            "\nThe atmosphere grows thick with anticipation as your adversary prepares for confrontation.",
            "With a steely gaze, they move forward, eager to prove their dominance in battle."
        ],
        [
            "\nA rumble shakes the very foundations of the ground as a powerful presence draws near.\n",
            "<???>: \"Oh, how quaint. A weakling has decided to intrude.\"",
            "<???>: \"If you dare to challenge me, you will need to earn your right to fight.\"",
            "<???>: \"Get ready, for you are about to face an opponent unlike any other!\"",
            "\nTension fills the air as the challenger readies themselves for a fierce encounter.",
            "With a fierce look in their eyes, they step forward, eager to engage in combat."
        ]
    ]

    chosen_dialogue = random.choice(dialogue_variations)

    for line in chosen_dialogue:
        type_text(line)
        time.sleep(.5)

    print()

    boss = generate_boss()

    time.sleep(1)
    type_text("<???>: \"Behold, YOU ROACH-- your final destination! My name is " + boss.name + ", ")
    type_text("<" + boss.name + ">: \"This will be your last fight!\"")
    print()
    time.sleep(1)
    type_text("Monster Info:")
    type_text("* " + str(boss))

    def handle_special_explore_case2():
        actions = {
            'A': 'attack',
            'T': 'taunt',
            'E': 'examine',
            'X': 'explore',
            'B': 'open your backpack'
        }

        def backpack_menu():
            type_text("\nYou opened your backpack.")
            while True:
                player.display_inventory()

                type_text("\nWhat would you like to do?")
                type_text("1. Use an item")
                type_text("2. Equip a weapon")
                type_text("3. Go back")

                choice = get_input("\nChoose an option:", options=['1', '2', '3'])

                if choice == '1':
                    item_name = get_input("\nEnter the name of the item to use:")
                    player.use_item(item_name)
                elif choice == '2':
                    weapon_name = get_input("\nEnter the name of the weapon to equip:")
                    player.equip_weapon(weapon_name)
                elif choice == '3':
                    type_text("\nReturning to the main menu.")
                    break
                else:
                    type_text("\nInvalid choice. Please choose again.")

        def display_choices():
            print()
            lines(23)
            type_text("What do you want to do?", 0.05)
            type_text("1. <A>ttack")
            type_text("2. <T>aunt")
            type_text("3. <E>xamine")
            type_text("4. <X>plore")
            type_text("5. <B>ackpack")

        while True:
            display_choices()
            action_choice = get_input("\nChoose an action:", options=actions.keys())
            action = actions.get(action_choice, None)

            if action is None:
                type_text("\nInvalid choice. Please choose again.")
                continue

            type_text(f"\nYou chose to {action.lower()}.")
            time.sleep(1)

            if action_choice == 'A':
                boss_combat = BossCombat(player, boss)
                boss_combat.start_combat()
                break
            elif action_choice == 'T':
                type_text("\nYou attempt to taunt " + boss.name + ".\n")

                def get_boss_taunts(name, adjective):
                    taunts = {
                        "Powerhouse": [
                            f"<{name}>: \"Do you even lift, bro?\"",
                            f"<{name}>: \"Did you expect a heavyweight challenge?\"",
                            f"<{name}>: \"You're like a warm-up set to me!\"",
                            f"<{name}>: \"My pet rock hits harder!\"",
                            f"<{name}>: \"I hope you brought some muscle!\""
                        ],
                        "Frail": [
                            f"<{name}>: \"Careful, I might break under the pressure!\"",
                            f"<{name}>: \"You’re really pushing it, you know?\"",
                            f"<{name}>: \"Try not to sneeze, or I might crumble!\"",
                            f"<{name}>: \"I might need a bandage!\"",
                            f"<{name}>: \"Oh no, not a taunt. I might shatter!\""
                        ],
                        "Depressed": [
                            f"<{name}>: \"You know, I’ve been having a rough day…\"",
                            f"<{name}>: \"Your taunts are the least of my problems right now.\"",
                            f"<{name}>: \"Why do I even bother with this?\"",
                            f"<{name}>: \"You’re not helping my mood, but carry on if you must.\"",
                            f"<{name}>: \"Does it really matter what you say? Nothing cheers me up.\""
                        ],
                        "Prideful": [
                            f"<{name}>: \"I could never be bested by someone like you!\"",
                            f"<{name}>: \"You should be honored to be in my presence!\"",
                            f"<{name}>: \"Your attempts are as futile as a gnat buzzing at a lion!\"",
                            f"<{name}>: \"Prepare to face true greatness!\"",
                            f"<{name}>: \"I am the pinnacle of all monsters, and you are insignificant!\""
                        ],
                        "Glorious": [
                            f"<{name}>: \"I hope you’re ready for an encounter with splendor!\"",
                            f"<{name}>: \"Behold my grandeur and prepare to be awed!\"",
                            f"<{name}>: \"Your words are like mere sparks before my brilliance!\"",
                            f"<{name}>: \"You can’t match my sheer magnificence!\"",
                            f"<{name}>: \"You are in the presence of true glory!\""
                        ],
                        "Mighty": [
                            f"<{name}>: \"You’re about to feel the full force of my might!\"",
                            f"<{name}>: \"Prepare to face the power of the mighty!\"",
                            f"<{name}>: \"Your taunts are like a pebble against a mountain!\"",
                            f"<{name}>: \"You’re about to be crushed by unstoppable strength!\"",
                            f"<{name}>: \"I’m the mightiest of all monsters, and you’ll see why!\""
                        ],
                        "Bumbling": [
                            f"<{name}>: \"Oops, did I stumble into this fight?\"",
                            f"<{name}>: \"Sorry, I’m just a bit clumsy today!\"",
                            f"<{name}>: \"Did I hear you right? Was that a taunt?\"",
                            f"<{name}>: \"I might be a bit of a mess, but don’t let that fool you!\"",
                            f"<{name}>: \"Was that supposed to be intimidating?\""
                        ],
                        "Fearsome": [
                            f"<{name}>: \"You should be trembling in fear!\"",
                            f"<{name}>: \"I’ll make sure you regret ever crossing my path!\"",
                            f"<{name}>: \"Your taunts only fuel my desire to destroy you!\"",
                            f"<{name}>: \"I’ll make your nightmares seem like a bedtime story!\"",
                            f"<{name}>: \"Prepare to face true terror!\""
                        ],
                        "Grumpy": [
                            f"<{name}>: \"I could really use a nap, but here we are.\"",
                            f"<{name}>: \"Could you be any more annoying?\"",
                            f"<{name}>: \"I guess I have to deal with you now.\"",
                            f"<{name}>: \"Can’t a monster have a moment's peace?\"",
                            f"<{name}>: \"You’re really cramping my style.\""
                        ],
                        "Hilarious": [
                            f"<{name}>: \"Is that the best you’ve got? My grandmother taunts better!\"",
                            f"<{name}>: \"I haven’t heard something so funny in ages!\"",
                            f"<{name}>: \"You must be a comedian, and not a very good one!\"",
                            f"<{name}>: \"I’m rolling on the floor with laughter!\"",
                            f"<{name}>: \"I haven’t had this much fun in forever!\""
                        ],
                        "Ethereal": [
                            f"<{name}>: \"Your taunts barely touch my otherworldly being.\"",
                            f"<{name}>: \"You’re just a mere mortal trying to provoke the ethereal.\"",
                            f"<{name}>: \"I’m above your petty attempts at provoking me.\"",
                            f"<{name}>: \"Your words are as fleeting as a ghost’s sigh.\"",
                            f"<{name}>: \"Your taunts are but whispers in the wind.\""
                        ],
                        "Wrathful": [
                            f"<{name}>: \"Your insolence will be punished with the full force of my wrath!\"",
                            f"<{name}>: \"You dare mock me? Prepare to face my rage!\"",
                            f"<{name}>: \"You’ve awakened a fury that will not be quenched!\"",
                            f"<{name}>: \"Your taunts fuel my anger. Prepare for the storm!\"",
                            f"<{name}>: \"You’ll pay dearly for provoking my wrath!\""
                        ],
                        "Luminous": [
                            f"<{name}>: \"Your attempts at taunting me are overshadowed by my radiance!\"",
                            f"<{name}>: \"You’re trying to dim my light with your words?\"",
                            f"<{name}>: \"Your taunts are nothing compared to my brilliance!\"",
                            f"<{name}>: \"Even your words can’t eclipse my dazzling presence!\"",
                            f"<{name}>: \"I’m too radiant to be affected by your attempts at provocation!\""
                        ],
                        "Cursed": [
                            f"<{name}>: \"Your taunts are nothing compared to the curse I carry!\"",
                            f"<{name}>: \"You think you can curse me with words? I am already damned!\"",
                            f"<{name}>: \"Your attempts to provoke me only deepen my curse!\"",
                            f"<{name}>: \"You dare to taunt one already burdened with a curse?\"",
                            f"<{name}>: \"My curse is far worse than anything you could throw at me!\""
                        ],
                        "Majestic": [
                            f"<{name}>: \"Your words are as trivial as a court jester’s jest!\"",
                            f"<{name}>: \"You must feel honored to receive a taunt from such majesty!\"",
                            f"<{name}>: \"You may speak, but know you are in the presence of true grandeur!\"",
                            f"<{name}>: \"Your attempts to taunt me are beneath my royal dignity!\"",
                            f"<{name}>: \"I am beyond your petty provocations!\""
                        ],
                        "Wicked": [
                            f"<{name}>: \"Your taunts are mere child's play to my wickedness!\"",
                            f"<{name}>: \"I revel in your feeble attempts to provoke me!\"",
                            f"<{name}>: \"You think your words can sway a heart so wicked?\"",
                            f"<{name}>: \"Your taunts amuse me more than they offend!\"",
                            f"<{name}>: \"You’re just fueling the fire of my wicked plans!\""
                        ],
                        "Freaky": [
                            f"<{name}>: \"You’re about to find out what makes me truly freaky!\"",
                            f"<{name}>: \"Your taunts are just a warm-up for what’s coming next!\"",
                            f"<{name}>: \"I embrace the freakiness, and your words only make it worse!\"",
                            f"<{name}>: \"Prepare yourself for a freaky showdown!\"",
                            f"<{name}>: \"You’ve only scratched the surface of my freaky nature!\""
                        ]
                    }
                    return taunts.get(adjective, [])

                taunts = get_boss_taunts(boss.name, boss.adjective)
                taunt = random.choice(taunts)
                type_text(taunt)
                time.sleep(2)

            elif action_choice == 'E':
                type_text(
                    "\nYou attempted to make an effort in examining the area, but the overlord's overwhelming presence")
                type_text("is all you can focus on right now.")
                time.sleep(2)
            elif action_choice == 'X':
                type_text("\nThere is no place to explore anymore right now!")
                time.sleep(2)
            elif action_choice == 'B':
                backpack_menu()

    handle_special_explore_case2()


def outro():
    global player, introduction_done
    time.sleep(1)
    type_text("\nAs you vanquish the tyrant overlord, whose dark grip bound countless souls to this realm,")
    type_text("the very fabric of the environment begins to crumble and dissolve, like a fading dream.")
    time.sleep(2)
    type_text("...")
    time.sleep(2)
    type_text("In the silence that follows, the enigmatic figure appears before you.")
    type_text("\n<???>: \"You have freed us all from the shadows. Your bravery has shattered the chains of despair.\"")
    type_text("<???>: \"With the fall of the previous ruler, the power to shape the realm now rests in your hands.\"")
    type_text("<???>: \"You stand at a crossroads: will you rebuild this world or let it fade away into the void?\"")

    type_text(
        "Before you can respond, the mysterious figure vanishes, leaving you with the weight of your monumental choice.")

    time.sleep(2)
    print()
    lines(19)
    type_text("What will you choose?")
    type_text("\n1. Restart (keep items)")
    type_text("2. Let it rest.")
    lines(19)

    choice = get_input("\nEnter 1 for Restart or 2 for Let it rest: ").strip()

    if choice == '1':
        type_text(
            "\nYou decide to restart, determined to give the world a fresh start while keeping your hard-earned items.")
        time.sleep(2)
        type_text("\n...\n")
        time.sleep(2)
        type_text("Here it goes.")
        time.sleep(1)
        introduction_done = True
        gameplay_restart()

    elif choice == '2':
        type_text(
            "\nYou choose to let it rest, allowing the realm to fade peacefully into the void, leaving behind only memories of your valor.")
        time.sleep(1)
        type_text("\n...\n")
        type_text("Goodbye.")
        sys.exit()
    else:
        type_text(
            "\nYou hesitate, unsure of your choice. The realm remains in suspended silence as you contemplate your decision.")
        time.sleep(3)
        type_text("..")
        time.sleep(1)
        type_text("...")
        time.sleep(2)


# --------------------------------------------------------------------------------------------- #


def prologue():
    print_ascii_art()
    wait_for_enter()
    time.sleep(1)
    introduction()
    starting_room_intro()
    obtaining_weapon()


# --------------------------------------------------------------------------------------------- #
def gameplay_restart():
    prologue()
    subroom_start()
    boss_level()
    outro()


if __name__ == "__main__":
    prologue()
    subroom_start()
    boss_level()
    outro()
