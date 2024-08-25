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


def generate_dungeon_name():
    adjectives = ["Dark", "Forgotten", "Abandoned", "Eerie", "Cursed"]
    nouns = ["Catacombs", "Crypts", "Dungeons", "Vaults", "Labyrinths"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"


def generate_graveyard_name():
    adjectives = ["Forsaken", "Desolate", "Haunted", "Ancient", "Silent"]
    nouns = ["Cemetery", "Graveyard", "Necropolis", "Burial Grounds", "Tombstone Fields"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"


def generate_temple_name():
    adjectives = ["Sacred", "Ruined", "Celestial", "Ancient", "Mystic"]
    nouns = ["Temple", "Shrine", "Sanctuary", "Altar", "Holy Ground"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"


def generate_boss_castle_name():
    adjectives = ["Imperial", "Dark", "Forsaken", "Majestic", "Dreadful"]
    nouns = ["Fortress", "Castle", "Citadel", "Keep", "Stronghold"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"


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


def generate_description_dungeon(adjective):
    descriptions = {
        "Dark": [
            "A labyrinth of shadowy corridors and hidden traps, where the light of your torch barely reaches.",
            "An ancient underground realm filled with forgotten treasures and lurking horrors, shrouded in perpetual darkness."
        ],
        "Forgotten": [
            "A maze of cobweb-covered passages and rusting machinery, long abandoned and covered in dust.",
            "An underground stronghold that time has left to decay, where ancient secrets lie buried under layers of neglect."
        ],
        "Abandoned": [
            "A desolate warren of empty halls and crumbling walls, haunted by the echoes of past inhabitants.",
            "A series of derelict tunnels and chambers, with remnants of a once-thriving domain now left to rot."
        ],
        "Eerie": [
            "A chilling network of twisting corridors, where every step echoes and the air is thick with unease.",
            "A ghostly dungeon where strange sounds and flickering shadows create an atmosphere of constant dread."
        ],
        "Cursed": [
            "A maze of dark, foreboding corridors, where ancient curses still linger and trap the unwary.",
            "An accursed stronghold where malevolent spirits and dark enchantments guard forgotten treasures."
        ]
    }
    return random.choice(descriptions.get(adjective, ["A mysterious dungeon with unique characteristics."]))


def generate_description_graveyard(adjective):
    descriptions = {
        "Forsaken": [
            "A long-abandoned graveyard, where the graves are overgrown with weeds and the air is filled with a mournful silence.",
            "An empty cemetery, left to the ravages of time and nature, with crumbling headstones and forgotten names."
        ],
        "Desolate": [
            "A bleak and barren burial ground, where the only sounds are the whisper of the wind and the rustle of dead leaves.",
            "A stark and empty necropolis, with nothing but shattered gravestones and the cold chill of abandonment."
        ],
        "Haunted": [
            "A graveyard shrouded in mist and eerie whispers, where restless spirits are said to wander among the graves.",
            "A haunted cemetery, where the spirits of the departed are rumored to roam, and strange phenomena are commonplace."
        ],
        "Ancient": [
            "An ancient necropolis with weathered tombstones and crumbling mausoleums, steeped in centuries of history and mystery.",
            "A timeworn graveyard with cryptic inscriptions and venerable burial sites, holding secrets from long ago."
        ],
        "Silent": [
            "A serene and quiet burial ground, where the stillness is interrupted only by the soft rustling of leaves and distant birdsong.",
            "A tranquil graveyard with a peaceful ambiance, where the silence is almost palpable and the atmosphere calm."
        ]
    }
    return random.choice(descriptions.get(adjective, ["A mysterious graveyard with unique characteristics."]))


def generate_description_temple(adjective):
    descriptions = {
        "Sacred": [
            "A hallowed temple filled with the remnants of ancient rituals and an aura of reverence that lingers in the air.",
            "A revered shrine with sacred symbols and a palpable sense of the divine, where every corner exudes sanctity."
        ],
        "Ruined": [
            "A once-majestic temple now in ruins, with broken columns and shattered relics scattered among the debris.",
            "A desolate shrine, its grandeur lost to time, where the ruins tell stories of a bygone era of worship."
        ],
        "Celestial": [
            "A temple of celestial beauty, adorned with intricate carvings and shimmering with an otherworldly glow.",
            "A divine sanctuary bathed in ethereal light, where the walls are covered with heavenly inscriptions and symbols."
        ],
        "Ancient": [
            "An age-old temple with worn, yet majestic architecture, steeped in the legends and lore of a forgotten past.",
            "A venerable shrine whose ancient walls hold the secrets of an era long gone, with inscriptions and artifacts of old."
        ],
        "Mystic": [
            "A mystical shrine where the air is charged with magical energy and enigmatic symbols adorn every surface.",
            "A hidden temple filled with arcane knowledge and mysterious artifacts, surrounded by an aura of ancient magic."
        ]
    }
    return random.choice(descriptions.get(adjective, ["A mysterious temple with unique characteristics."]))


def generate_description_boss_castle(adjective):
    descriptions = {
        "Imperial": [
            "A grand fortress of imperial design, with towering spires and opulent halls that speak of its former glory.",
            "A majestic castle, built with regal splendor and adorned with symbols of power and dominance."
        ],
        "Dark": [
            "A foreboding stronghold shrouded in darkness, where every corner hides danger and the atmosphere is oppressive.",
            "A gloomy fortress, with shadowy battlements and an air of menace that pervades its grand halls."
        ],
        "Forsaken": [
            "A once-grand castle now left to ruin, its majestic walls crumbling and its halls echoing with the sound of desolation.",
            "A forsaken stronghold, abandoned and decayed, with an aura of melancholy and lost grandeur."
        ],
        "Dreadful": [
            "A dreadful fortress filled with sinister traps and dark secrets, its ominous presence a constant threat to all who enter.",
            "A terrifying stronghold where nightmares take shape and the very walls seem to whisper of impending doom."
        ]
    }
    return random.choice(descriptions.get(adjective, ["A mysterious castle with unique characteristics."]))
