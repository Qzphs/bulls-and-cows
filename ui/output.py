class Output:

    def __init__(self):
        self.buffer = []

    def __bool__(self):
        return bool(self.buffer)

    def add(self, text: str):
        self.buffer.append(text)

    def get(self):
        text = "".join(self.buffer)
        self.buffer.clear()
        return text
