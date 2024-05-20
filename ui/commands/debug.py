from ui.command import Command
from ui.ui import Ui


class Debug(Command):

    @property
    def name(self):
        return ".debug"

    def execute(self, ui: Ui, prompt: str):
        ui.output.add(ui.game.replay())
