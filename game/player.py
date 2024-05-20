from game.code import Code
from game.errors import IllegalActionError
from game.guess import Guess


class Player:

    def __init__(self):
        self.secret: Code | None = None
        self.guesses: list[Guess] = []

    @property
    def solved(self):
        if not self.guesses:
            return False
        return self.guesses[-1].code == self.secret

    def set_secret(self, code: Code):
        self.secret = code

    def make_guess(self, code: Code):
        if self.secret is None:
            raise IllegalActionError("secret not set yet")
        self.guesses.append(
            Guess(code, self.secret.bulls(code), self.secret.cows(code))
        )
