class Code:

    def __init__(self, digits: str):
        self.digits = digits
        self.validate()

    def __eq__(self, other: "Code"):
        return self.digits == other.digits

    def validate(self):
        for digit in self.digits:
            if digit not in "0123456789":
                raise ValueError(f"invalid code '{self.digits}'")
            if self.digits.count(digit) > 1:
                raise ValueError(f"invalid code '{self.digits}'")

    def bulls(self, other: "Code"):
        return sum(
            own_digit == other_digit
            for (own_digit, other_digit) in zip(self.digits, other.digits)
        )

    def cows(self, other: "Code"):
        matches = sum(own_digit in other.digits for own_digit in self.digits)
        return matches - self.bulls(other)
