from datatypes import String, Number


class Validator:
    def __init__(self):
        self.conditions = {}

    def string(self):
        return String()

    def number(self):
        return Number()
