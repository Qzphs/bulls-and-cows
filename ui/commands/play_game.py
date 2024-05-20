from game.modes import Singleplayer, VersusEasy, VersusMedium, VersusHard
from game import IllegalActionError
from ui.command import Command
from ui.ui import Ui


class PlayGame(Command):

    @property
    def name(self):
        return ".play"

    def execute(self, ui: Ui, prompt: str):
        if ui.game is not None:
            raise IllegalActionError("game already started")
        mode = prompt.removeprefix(self.name + " ")
        if mode == "singleplayer":
            ui.game = Singleplayer()
        elif mode == "easy":
            ui.game = VersusEasy()
        elif mode == "medium":
            ui.game = VersusMedium()
        elif mode == "hard":
            ui.game = VersusHard()
        else:
            raise IllegalActionError(f"unknown gamemode: '{mode}'")
