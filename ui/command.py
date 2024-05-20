from ui.ui import Ui


class Command:

    @property
    def name(self):
        return ""

    def recognises(self, prompt: str):
        return prompt == self.name or prompt.startswith(self.name + " ")

    def execute(self, ui: Ui, prompt: str):
        pass
