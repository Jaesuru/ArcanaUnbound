import time
import random

from items import create_weapon, HealthPotion
from player import Player
from utilities import type_text, lines
from rooms import generate_forest_name, Room, generate_description_forest

player = None


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


def player_action():
    actions = {
        'A': 'Attack',
        'T': 'Taunt',
        'E': 'Examine',
        'X': 'Explore',
        'B': 'Backpack'
    }

    def display_choices():
        lines(23)
        type_text("\nWhat do you want to do?")
        type_text("1. <A>ttack")
        type_text("2. <T>aunt")
        type_text("3. <E>xamine")
        type_text("4. <X>plore")
        type_text("5. <B>ackpack")

    def get_action_input():
        while True:
            display_choices()
            action_choice = get_input("\nChoose an action:", options=actions.keys())
            action = actions[action_choice]
            type_text(f"\nYou chose to {action.lower()}.")
            time.sleep(1)
            return action_choice

    action = get_action_input()

    if action == 'A':
        type_text("\nYou prepare to attack.")
        # Add attack logic here
    elif action == 'T':
        type_text("\nYou decide to taunt.")
        # Add taunt logic here
    elif action == 'E':
        type_text("\nYou start examining the surroundings.")
        # Add examine logic here
    elif action == 'X':
        type_text("\nYou begin exploring.")
        # Add explore logic here
    elif action == 'B':
        type_text("\nYou open your backpack.")
        # Add backpack logic here


def introduction():
    global player
    lines(38)
    type_text("Welcome to the world of ArcanaUnbound.")
    lines(38)
    time.sleep(.5)
    type_text("\n* Starting game...")
    time.sleep(2)

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

    # Choose a random dialogue set
    selected_dialogue = random.choice(dialogues)

    # Display the selected dialogue
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

                            player = Player("Jason", "Human", "Mage")
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
    type_text("""
       *   '*
               *
                    *
                           *
                   *
                         *

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
    """, 0.01)

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
                    type_text("\nYou prepare to attack, but you swing your fists into nothing.")
                elif action_choice == 'T':
                    type_text("\nYou taunt into the distance, but all you receive were the sound of distant crickets chirping.")
                elif action_choice == 'E':
                    type_text("\nYou examine the verdant surroundings, but the glint is still visible in the distance.")
                elif action_choice == 'B':
                    type_text("\nYou open your backpack, and there seems to be something!")
                    time.sleep(.5)
                    type_text("...")
                    time.sleep(2)
                    type_text("It was just a roll of lint.")
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

    # player = Player("Jason", "Human", "Mage")
    #
    # for _ in range(3):
    #     weapon = create_weapon(player)
    #     potion = HealthPotion()
    #
    #     player.add_to_inventory(weapon)
    #     player.add_to_inventory(potion)
    #     print(weapon.describe())

# --------------------------------------------------------------------------------------------- #


def prologue():
    print_ascii_art()
    # wait_for_enter()
    # time.sleep(1)
    # introduction()
    # starting_room_intro()
    obtaining_weapon()


if __name__ == "__main__":
    # prologue()
    player = Player("Jason", "Human", "Mage")

    for _ in range(3):
        weapon = create_weapon(player)
        potion = HealthPotion()

        player.add_to_inventory(weapon)
        player.add_to_inventory(potion)

    player.display_inventory()

