from game import Code, Randomiser


class MockRandomiser(Randomiser):

    def __init__(self):
        self.bools: list[bool] = []
        self.codes: list[Code] = []

    def random_bool(self):
        return self.bools.pop(0)

    def random_code(self):
        return self.codes.pop(0)
