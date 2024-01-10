from hexlet_code.datatypes import String, Number, ListData, DictData


class Validator:
    def __init__(self):
        self.conditions = {}

    def string(self):
        return String()

    def number(self):
        return Number()

    def list(self):
        return ListData()

    def dict(self):
        return DictData()
