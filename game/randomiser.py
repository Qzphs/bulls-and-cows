import random

from game.code import Code


class Randomiser:

    def random_bool(self):
        return random.random() < 0.5

    def random_code(self):
        return Code("".join(random.sample("0123456789", 4)))
