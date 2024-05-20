from game import IllegalActionError
from ui.command import Command
from ui.replay_writer import ReplayWriter
from ui.ui import Ui


class SaveReplay(Command):

    @property
    def name(self):
        return ".save"

    def execute(self, ui: Ui, prompt: str):
        if ui.game is None:
            raise IllegalActionError("game not started")
        filename = f"replays/{prompt.removeprefix(self.name + ' ')}.txt"
        with open(filename, "w") as file:
            file.write(ReplayWriter().replay(ui.game))
        ui.output.add("Replay saved.\n")
