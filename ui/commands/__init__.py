from ui.command import Command
from ui.commands.choose_guess import ChooseGuess, ChooseGuessShort
from ui.commands.choose_secret import ChooseSecret, ChooseSecretShort
from ui.commands.play_game import PlayGame
from ui.commands.quit_game import QuitGame
from ui.commands.save_replay import SaveReplay


COMMANDS: list[Command] = [
    ChooseGuess(),
    ChooseGuessShort(),
    ChooseSecret(),
    ChooseSecretShort(),
    PlayGame(),
    QuitGame(),
    SaveReplay(),
]
