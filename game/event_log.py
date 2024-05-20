from game.events import Event, GameStarted


class EventLog:

    def __init__(self):
        self.events: list[Event] = [GameStarted()]
        self.index = 0

    def add(self, event: Event):
        self.events.append(event)

    def get(self):
        """Return list of newly added events.

        Also update self.index to mark current events as read.
        """
        if self.index == len(self.events):
            return []
        new_events = self.events[self.index :]
        self.index = len(self.events)
        return new_events
