from game.code import Code
from game.decider import Decider
from game.events import (
    AiChoseGuess,
    AiChoseSecret,
    HumanChoseSecret,
    GameLost,
    GameDrawn,
)
from game.game import Game
from game.player import Player
from game.randomiser import Randomiser


class VersusComputer(Game):
    """Base class for versus-computer modes.

    Subclasses must override self.ai_decider.
    """

    def __init__(self, randomiser: Randomiser | None = None):
        super().__init__(randomiser)
        self.ai_decider: Decider | None = None
        self.human_player = Player()

    @property
    def over(self):
        return (
            (
                len(self.ai_player.guesses)
                == len(self.human_player.guesses)
                == self.guess_limit
            )
            or self.ai_player.solved
            or self.human_player.solved
        )

    def choose_guess(self, code: Code):
        super().choose_guess(code)
        if not self.over and len(self.human_player.guesses) < self.guess_limit:
            self._choose_guess_ai()
        if (
            (
                len(self.ai_player.guesses)
                == len(self.human_player.guesses)
                == self.guess_limit
            )
            and not self.ai_player.solved
            and not self.human_player.solved
        ):
            self.event_log.add(GameDrawn())

    def choose_secret(self, code: Code):
        """Set secret for human.

        Also choose secret for AI and start guessing.
        """
        self.human_player.set_secret(code)
        self.event_log.add(HumanChoseSecret(code))
        self.ai_decider.choose_secret(self.ai_player)
        self.event_log.add(AiChoseSecret(self.ai_player.secret))
        if self.randomiser.random_bool():
            self._choose_guess_ai()

    def _choose_guess_ai(self):
        self.ai_decider.choose_guess(self.human_player)
        self.event_log.add(AiChoseGuess(self.human_player.guesses[-1]))
        if self.human_player.solved:
            self.event_log.add(GameLost())
