"""CP1404/CP5632 Practical - programming language class."""


class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=False, year=""):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, {self.year}"

    # def __repr__(self):
    #     return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, {self.year}"
