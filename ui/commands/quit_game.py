from ui.command import Command
from ui.ui import Ui


class QuitGame(Command):

    @property
    def name(self):
        return ".quit"

    def execute(self, ui: Ui, prompt: str):
        ui.quit = True
