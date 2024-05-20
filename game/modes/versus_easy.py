from game.decider import Decider
from game.modes.versus_computer import VersusComputer
from game.player import Player
from game.randomiser import Randomiser


class VersusEasy(VersusComputer):

    def __init__(self, randomiser: Randomiser | None = None):
        super().__init__(randomiser)
        self.ai_decider = EasyAi(self.randomiser)


class EasyAi(Decider):
    """Easy AI as required in 718.

    Always randomly generates codes for both guesses and secrets.
    """

    def __init__(self, randomiser: Randomiser):
        self.randomiser = randomiser

    def choose_guess(self, opponent: Player):
        opponent.make_guess(self.randomiser.random_code())

    def choose_secret(self, player: Player):
        player.set_secret(self.randomiser.random_code())
