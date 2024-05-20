from discord import Client, Intents, Message

from game import IllegalActionError
from ui.commands import COMMANDS
from ui.ui import Ui


with open("channel.txt") as file:
    CHANNEL_ID = int(file.read().strip())


class Bot(Client):

    def __init__(self, ui: Ui):
        super().__init__(intents=Intents.all())
        self.ui = ui

    async def on_ready(self):
        self.channel = self.get_channel(CHANNEL_ID)
        self.ui.display_prompt()
        if self.ui.output:
            await self.channel.send(self.ui.output.get())

    async def on_message(self, message: Message):
        if not message.channel == self.channel:
            return
        if message.author.bot:
            return
        if not message.content.startswith("."):
            return
        if message.content.startswith(".."):
            return
        try:
            for command in COMMANDS:
                if not command.recognises(message.content):
                    continue
                command.execute(self.ui, message.content)
                break
            else:
                self.ui.output.add(f"unknown command '{message.content}'\n")
        except (IllegalActionError, ValueError) as error:
            self.ui.output.add(f"{error.__class__.__name__}: {error}\n")
        self.ui.display_prompt()
        if self.ui.output:
            await self.channel.send(self.ui.output.get())
        if self.ui.quit:
            await self.close()
