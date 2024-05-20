from game.code import Code
from game.game import Game
from game.events import AiChoseSecret, GameLost
from game.randomiser import Randomiser


class Singleplayer(Game):

    def __init__(self, randomiser: Randomiser | None = None):
        super().__init__(randomiser)
        self.ai_player.set_secret(self.randomiser.random_code())
        self.event_log.add(AiChoseSecret(self.ai_player.secret))

    @property
    def over(self):
        return (
            len(self.ai_player.guesses) == self.guess_limit
            or self.ai_player.solved
        )

    def choose_guess(self, code: Code):
        super().choose_guess(code)
        if (
            len(self.ai_player.guesses) == self.guess_limit
            and not self.ai_player.solved
        ):
            self.event_log.add(GameLost())
