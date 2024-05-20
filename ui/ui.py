from game import Game
from ui.event_displayer import EventDisplayer
from ui.output import Output


class Ui:

    def __init__(self):
        self.displayer = EventDisplayer()
        self.game: Game | None = None
        self.output = Output()
        self.quit = False
        self.output.add("Bulls and Cows game.\n")

    def display_prompt(self):
        if self.quit:
            return
        if self.game is None:
            self.output.add("\nChoose game mode:\n")
            return
        for event in self.game.event_log.get():
            self.output.add(self.displayer.display(event))
        if self.game.over:
            self.output.add("\n")
            return
        if self.game.ai_player.secret is None:
            self.output.add("\nChoose secret:\n")
            return
        self.output.add("\nChoose guess:\n")
