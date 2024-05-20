import itertools

from game import (
    Game,
    IllegalActionError,
    Singleplayer,
    VersusComputer,
    VersusEasy,
    VersusMedium,
    VersusHard,
)
from game.events import GameWon, GameLost, GameDrawn


class ReplayWriter:
    """Create replays for completed games."""

    def replay(self, game: Game):
        if not game.over:
            raise IllegalActionError("game not over")
        if isinstance(game, Singleplayer):
            return self._replay_singleplayer(game)
        elif isinstance(game, VersusComputer):
            return self._replay_versus_computer(game)
        else:
            raise TypeError(
                f"game type should be Singleplayer or VersusComupter, "
                f"but got {type(game)}"
            )

    def _replay_singleplayer(self, game: Singleplayer):
        buffer = []
        buffer.append("Game started (Singleplayer).\n\n")
        buffer.append(f"Secret: {game.ai_player.secret.digits}.\n\n")
        buffer.append("Guesses:\n")
        for guess in game.ai_player.guesses:
            buffer.append(
                f"- {guess.code.digits} "
                f"({guess.bulls} bull, {guess.cows} cow).\n"
            )
        if isinstance(game.event_log.events[-1], GameWon):
            buffer.append("\nYou win!\n")
        elif isinstance(game.event_log.events[-1], GameLost):
            buffer.append("\nYou lose!\n")
        elif isinstance(game.event_log.events[-1], GameDrawn):
            buffer.append("\nIt's a draw!\n")
        return "".join(buffer)

    def _replay_versus_computer(self, game: VersusComputer):
        buffer = []

        # AI Difficulty
        if isinstance(game, VersusEasy):
            buffer.append("Game started versus EasyAI.\n\n")
        elif isinstance(game, VersusMedium):
            buffer.append("Game started versus MediumAI.\n\n")
        elif isinstance(game, VersusHard):
            buffer.append("Game started versus HardAI.\n\n")
        else:
            buffer.append("Game started versus AI.\n\n")

        # Starting player
        if len(game.ai_player.guesses) < len(game.human_player.guesses):
            buffer.append("Player guesses first.\n\n")
        elif len(game.ai_player.guesses) > len(game.human_player.guesses):
            buffer.append("AI guesses first.\n\n")
        elif game.ai_player.solved:
            buffer.append("AI guesses first.\n\n")
        elif game.human_player.solved:
            buffer.append("Player guesses first.\n\n")

        # Secrets
        buffer.append(
            f"AI secret: {game.ai_player.secret.digits}.            "
            f"Player secret: {game.human_player.secret.digits}.\n\n"
        )

        # Guesses
        buffer.append("Guesses:                    Guesses:\n")
        for guess1, guess2 in itertools.zip_longest(
            game.ai_player.guesses, game.human_player.guesses
        ):
            if guess1 is not None:
                entry1 = (
                    f"- {guess1.code.digits} "
                    f"({guess1.bulls} bull, {guess1.cows} cow)."
                )
            else:
                entry1 = ""
            if guess2 is not None:
                entry2 = (
                    f"- {guess2.code.digits} "
                    f"({guess2.bulls} bull, {guess2.cows} cow)."
                )
            else:
                entry2 = ""
            buffer.append(f"{entry1}     {entry2}\n")

        # Result
        if isinstance(game.event_log.events[-1], GameWon):
            buffer.append("\nYou win!\n")
        elif isinstance(game.event_log.events[-1], GameLost):
            buffer.append("\nYou lose!\n")
        elif isinstance(game.event_log.events[-1], GameDrawn):
            buffer.append("\nIt's a draw!\n")

        return "".join(buffer)
