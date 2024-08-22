import random
from utilities import type_text


class Subroom:
    def __init__(self, name, description, items=None, monsters=None, has_exit=False):
        self.name = name
        self.description = description
        self.items = items if items else []
        self.monsters = monsters if monsters else []
        self.has_exit = has_exit

    def describe(self, main_room_name):
        full_name = f"{main_room_name}: {self.name}"
        type_text(f"{full_name}")
        type_text(self.description)
        if self.items:
            type_text(f"\nYou see: {', '.join(self.items)}")
        if self.monsters:
            type_text(f"\nYou notice monsters: {', '.join(self.monsters)}")
        if self.has_exit:
            type_text("\nYou notice an exit leading to the next room.")


def generate_subroom_name():
    descriptors = ["Ruined", "Hidden", "Secret", "Wandering", "Dilapidated", "Overgrown"]
    features = ["Caves", "Creeks", "Monoliths", "Campsites", "Shrines", "Temples"]

    descriptor = random.choice(descriptors)
    feature = random.choice(features)

    return f"{descriptor} {feature}"


def generate_description_subroom(descriptor):
    descriptions = {
        "Ruined": [
            "A place that has fallen into decay, with crumbling walls and scattered debris.",
            "An abandoned area where nature has begun to reclaim the remnants of civilization.",
        ],
        "Hidden": [
            "A concealed place, tucked away from plain sight, with a sense of mystery.",
            "An obscure space, veiled by the surrounding environment, hiding its secrets.",
        ],
        "Secret": [
            "A covert chamber that holds unknown treasures or dangers.",
            "A clandestine area with hidden passages and enigmatic symbols.",
        ],
        "Wandering": [
            "A room that seems to shift and change, creating a maze-like experience.",
            "An ever-changing area where paths twist and turn unpredictably.",
        ],
        "Dilapidated": [
            "A deteriorating space, marked by its worn and battered appearance.",
            "A place in a state of disrepair, with damaged structures and faded remnants.",
        ],
        "Overgrown": [
            "An area overtaken by nature, with thick vines and dense foliage.",
            "A lush, encroached space where vegetation has taken over the surroundings.",
        ]
    }

    return random.choice(descriptions.get(descriptor, ["A subroom with unique characteristics and features."]))
