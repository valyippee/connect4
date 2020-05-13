import importlib


class PlayerWrapper:
    def __init__(self, name, package_location, class_name):
        self.name = name
        self.Player = self.load_class(package_location, class_name)

    def init(self, colour):
        self.colour = colour
        self.player = self.Player(colour)

    def load_class(self, package_location, class_name):
        module = importlib.import_module(package_location)
        player_class = getattr(module, class_name)
        return player_class

    def action(self):
        row = self.player.action()
        return row

    def update(self, player, column):
        self.player.update(player, column)