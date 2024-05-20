import itertools

from game.code import Code
from game.decider import Decider
from game.modes.versus_computer import VersusComputer
from game.player import Player
from game.randomiser import Randomiser


class VersusHard(VersusComputer):

    def __init__(self, randomiser: Randomiser | None = None):
        super().__init__(randomiser)
        self.ai_decider = HardAi(self.randomiser)


class HardAi(Decider):
    """Hard AI as required in 718.

    Always guesses something plausible given available information.
    """

    def __init__(self, randomiser: Randomiser):
        self.randomiser = randomiser
        self.possibilities = [
            Code("".join(code))
            for code in itertools.permutations("0123456789", 4)
        ]

    def choose_guess(self, opponent: Player):
        code = self.randomiser.random_code()
        while code not in self.possibilities:
            code = self.randomiser.random_code()
        opponent.make_guess(code)
        for i, possibility in reversed(list(enumerate(self.possibilities))):
            if code.bulls(possibility) != opponent.guesses[-1].bulls:
                self.possibilities.pop(i)
                continue
            if code.cows(possibility) != opponent.guesses[-1].cows:
                self.possibilities.pop(i)
                continue

    def choose_secret(self, player: Player):
        player.set_secret(self.randomiser.random_code())
