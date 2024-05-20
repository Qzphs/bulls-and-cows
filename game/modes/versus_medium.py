from game.code import Code
from game.decider import Decider
from game.modes.versus_computer import VersusComputer
from game.player import Player
from game.randomiser import Randomiser


class VersusMedium(VersusComputer):

    def __init__(self, randomiser: Randomiser | None = None):
        super().__init__(randomiser)
        self.ai_decider = MediumAi(self.randomiser)


class MediumAi(Decider):
    """Medium AI as required in 718.

    Never repeats guesses.
    """

    def __init__(self, randomiser: Randomiser):
        self.randomiser = randomiser
        self.past_guesses: list[Code] = []

    def choose_guess(self, opponent: Player):
        code = self.randomiser.random_code()
        while code in self.past_guesses:
            code = self.randomiser.random_code()
        opponent.make_guess(code)
        self.past_guesses.append(code)

    def choose_secret(self, player: Player):
        player.set_secret(self.randomiser.random_code())
