from game import Code, IllegalActionError
from ui.command import Command
from ui.ui import Ui


class ChooseGuess(Command):

    @property
    def name(self):
        return ".guess"

    def execute(self, ui: Ui, prompt: str):
        if ui.game is None:
            raise IllegalActionError("game not started")
        code = Code(prompt.removeprefix(self.name + " "))
        ui.game.choose_guess(code)
