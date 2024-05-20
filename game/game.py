from game.code import Code
from game.errors import IllegalActionError
from game.event_log import EventLog
from game.events import HumanChoseGuess, GameWon
from game.player import Player
from game.randomiser import Randomiser


class Game:

    def __init__(self, randomiser: Randomiser | None = None):
        if randomiser is None:
            randomiser = Randomiser()
        self.randomiser = randomiser
        self.ai_player = Player()
        self.event_log = EventLog()
        self.guess_limit = 7

    @property
    def over(self):
        return False

    def choose_guess(self, code: Code):
        """Make guess for human."""
        if self.over:
            raise IllegalActionError("game over")
        self.ai_player.make_guess(code)
        self.event_log.add(HumanChoseGuess(self.ai_player.guesses[-1]))
        if self.ai_player.solved:
            self.event_log.add(GameWon())
