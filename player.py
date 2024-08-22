# player.py

class Player:
    def __init__(self, name, race, player_class):
        self.name = name
        self.race = race
        self.player_class = player_class

    def display_info(self):
        return f"{self.name}, the {self.race} {self.player_class}"
