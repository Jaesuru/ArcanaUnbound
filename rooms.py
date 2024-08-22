import random
from utilities import type_text


class Room:
    def __init__(self, name, description, items=None, monsters=None):
        self.name = name
        self.description = description
        self.items = items if items else []
        self.monsters = monsters if monsters else []
        self.subrooms = []

    def describe(self):
        type_text(f"{self.name}")
        type_text(self.description)
        if self.items:
            type_text(f"\nYou see: {', '.join(self.items)}")
        if self.monsters:
            type_text(f"\nYou notice monsters: {', '.join(self.monsters)}")


def generate_forest_name():
    adjectives = ["Mystic", "Enchanted", "Dark", "Whispering", "Ancient", "Serene"]
    nouns = ["Groves", "Woods", "Forests", "Thickets", "Glades"]

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    return f"{adjective} {noun}", adjective


def generate_description_forest(adjective):
    descriptions = {
        "Mystic": [
            "A place shrouded in mystery, where the air hums with magic.",
            "An otherworldly realm with shimmering lights and hidden secrets.",
        ],
        "Enchanted": [
            "A magical place where dreams seemingly look as if they come true here.",
            "A place where enchantment weaves through the leaves and flowers.",
        ],
        "Dark": [
            "A shadowy forest where light struggles to penetrate the thick canopy.",
            "An ominous place filled with eerie silence and lurking dangers.",
        ],
        "Whispering": [
            "A forest where the wind carries secrets and the leaves whisper softly.",
            "A serene place where every rustle and sigh seems to hold a hidden meaning.",
        ],
        "Ancient": [
            "A timeless place where ancient trees have stood for centuries.",
            "A forest steeped in history, where every branch and leaf tells a story.",
        ],
        "Serene": [
            "A peaceful haven with calm, soothing surroundings and gentle breezes.",
            "A tranquil place where the stillness brings a sense of inner peace.",
        ]
    }

    return random.choice(descriptions.get(adjective, ["A mysterious forest with unique characteristics."]))


def add_subroom(self, subroom):
    self.subrooms.append(subroom)


def describe_subrooms(self):
    for subroom in self.subrooms:
        subroom.describe(self.name)
