from game.events import (
    Event,
    GameStarted,
    AiChoseGuess,
    AiChoseSecret,
    HumanChoseGuess,
    HumanChoseSecret,
    GameWon,
    GameLost,
    GameDrawn,
)


class EventDisplayer:
    """Display events for ongoing games."""

    def display(self, event: Event):
        if isinstance(event, GameStarted):
            return "Game started.\n"
        elif isinstance(event, AiChoseGuess):
            return (
                f"AI guessed {event.guess.code.digits} "
                f"({event.guess.bulls} bull, {event.guess.cows} cow).\n"
            )
        elif isinstance(event, AiChoseSecret):
            return "AI chose a secret.\n"
        elif isinstance(event, HumanChoseGuess):
            return (
                f"You guessed {event.guess.code.digits} "
                f"({event.guess.bulls} bull, {event.guess.cows} cow).\n"
            )
        elif isinstance(event, HumanChoseSecret):
            return f"You chose {event.code.digits} as your secret.\n"
        elif isinstance(event, GameWon):
            return "You win!\n"
        elif isinstance(event, GameLost):
            return "You lose!\n"
        elif isinstance(event, GameDrawn):
            return "It's a draw!\n"
        else:
            return ""
