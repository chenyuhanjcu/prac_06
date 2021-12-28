"""CP1404/CP5632 Practical - Guitar class example."""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return int(2020 - self.year)

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
