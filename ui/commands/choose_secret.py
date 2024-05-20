from game import Code, IllegalActionError, VersusComputer
from ui.command import Command
from ui.ui import Ui


class ChooseSecret(Command):

    @property
    def name(self):
        return ".secret"

    def execute(self, ui: Ui, prompt: str):
        if ui.game is None:
            raise IllegalActionError("game not started")
        if not isinstance(ui.game, VersusComputer):
            raise IllegalActionError("secret can only be set in versus modes")
        code = Code(prompt.removeprefix(self.name + " "))
        ui.game.choose_secret(code)
