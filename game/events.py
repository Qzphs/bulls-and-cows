from game.code import Code
from game.guess import Guess


class Event:
    """Represent things that can happen in a game."""


class GameStarted(Event):
    pass


class AiChoseGuess(Event):

    def __init__(self, guess: Guess):
        self.guess = guess


class AiChoseSecret(Event):

    def __init__(self, code: Code):
        self.code = code


class HumanChoseGuess(Event):

    def __init__(self, guess: Guess):
        self.guess = guess


class HumanChoseSecret(Event):

    def __init__(self, code: Code):
        self.code = code


class GameWon(Event):
    pass


class GameLost(Event):
    pass


class GameDrawn(Event):
    pass
