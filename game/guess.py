from game.code import Code


class Guess:
    """Dataclasses recording guess code and result."""

    def __init__(self, code: Code, bulls: int, cows: int):
        self.code = code
        self.bulls = bulls
        self.cows = cows
