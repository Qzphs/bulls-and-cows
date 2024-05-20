from game.player import Player


class Decider:
    """Base class for AI deciders."""

    def choose_guess(self, opponent: Player):
        """Make guess against opponent."""

    def choose_secret(self, player: Player):
        """Set secret for AI."""
