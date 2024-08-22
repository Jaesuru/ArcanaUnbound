import time
import random
from player import Player
from utilities import type_text, lines
from rooms import generate_forest_name, Room, generate_description

player = None


def get_name_length(name):
    return len(name) + 1  # +1 to account for additional characters


def name_line_maker(name):
    length = get_name_length(name)
    print('=' * length)


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
        "A voice from afar beckons out to you, \"Try again...\""
    ]

    while True:
        type_text(prompt)
        print("> ", end="")
        choice = input().capitalize()
        if options is None or choice in options:
            return choice
        type_text(random.choice(invalid_responses))


def introduction():
    global player
    lines(38)
    type_text("Welcome to the world of ArcanaUnbound.")
    lines(38)
    time.sleep(1)
    type_text("\n* Starting game...")
    time.sleep(2)
    type_text("\nYou slowly regain consciousness in a dimly lit room, a place that feels strangely familiar.")
    type_text("The air is thick with an eerie silence, with a slight cold breeze.")
    type_text("You can't shake the feeling that you’ve been here before.")
    type_text("A figure emerges from the darkness, their features obscured by a shroud of mystery.")
    type_text("\n???: \"Ah, another soul. It seems you’ve found your way here, again or not.\"")
    type_text("???: \"Do you remember why you're here?\"")
    time.sleep(.5)
    type_text("...")
    time.sleep(1)
    type_text("???: \"Probably not.\"")
    time.sleep(1)
    type_text("???: \"You see, this realm is ruled by an overlord whose power keeps us all bound here.\"")
    type_text("???: \"Your task, should you choose to accept it, is to confront and defeat this overlord.\"")
    type_text("???: \"Only then will you be able to break free from this purgatory.\"\n")
    time.sleep(1)
    while True:
        lines(60)
        print()
        player_name = get_input("\"Do what you will, but now that you know what to do, what is your name?\"")
        type_text(f"\nYou have chosen the name: {player_name}")
        confirmation = get_input("Is this correct? (Y/N)", options=['Y', 'N'])
        if confirmation == 'Y':
            break

    races = {
        'H': 'Human',
        'E': 'Elf',
        'D': 'Dwarf',
        'O': 'Orc',
        'Human': 'Human',
        'Elf': 'Elf',
        'Dwarf': 'Dwarf',
        'Orc': 'Orc'
    }

    while True:
        type_text("\n")
        lines(60)
        type_text("Choose your race:")
        type_text("1. <H>uman")
        type_text("2. <E>lf")
        type_text("3. <D>warf")
        type_text("4. <O>rc")
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
    type_text("\n* Loading game...")

    return player


def starting_room_intro():
    global player
    forest_name, adjective = generate_forest_name()
    forest_description = generate_description(adjective)
    random_forest_room = Room(name=forest_name, description=forest_description)
    name_line_maker(random_forest_room.description)
    random_forest_room.describe()
    name_line_maker(random_forest_room.description)

    # Introduction text
    type_text("\nYou slowly regain consciousness.")
    type_text("The first thing you notice is the rustling of nearby leaves, carried by a gentle breeze.")
    type_text("As you open your eyes, you see the canopy of a dense forest, with the moonlight shining through.")
    type_text("You're lying on a bed of soft, verdant grass that feels cool against your skin.")
    type_text("In the distance, you can hear the soothing sound of a gentle water stream flowing.")
    type_text("The air is fresh and crisp, carrying the subtle scent of pine and earth.")

    while True:
        choice = get_input("\nGet Up? (y/n)", options=['Y', 'N'])
        if choice == 'Y':
            type_text("\nYou push yourself up from the grass and stand up, ready to explore the forest.")
            type_text("\nYou are now ready to start your adventure.")
            break
        elif choice == 'N':
            type_text("\nYou decide to stay on the grass a bit longer, admiring the serenity of the environment")
            type_text("After some time, you feel more refreshed and decided whether to get up.")

            while True:
                choice = get_input("\nWill you get up now? (y/n)", options=['Y', 'N'])
                if choice == 'Y':
                    type_text("\nYou push yourself up from the grass and stand up, ready to explore the forest.")
                    type_text("\nYou are now ready to start your adventure.")
                    break
                elif choice == 'N':
                    type_text("\nYou continue to lie on the grass, enjoying the peaceful surroundings.")
                    type_text("After a while, a voice from afar beckons you to arise.")
                    type_text("???: \"GET UP, HERO!\"")

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
                            time.sleep(.5)
                            player = Player("Jason", "Human", "Mage")

                            type_text(f"\n* {player.display_info()} is now standing.")
                            break
                    break
            break

# --------------------------------------------------------------------------------------------- #


if __name__ == "__main__":
    # print_ascii_art()
    # wait_for_enter()
    # time.sleep(1)
    # introduction()
    starting_room_intro()

