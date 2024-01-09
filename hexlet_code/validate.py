class Validator:
    def __init__(self):
        self.conditions = {}

    def string(self):
        return self.__class__()

    def required(self):
        self.conditions['required'] = lambda string: string not in (None, '')
        return self

    def contains(self, template):
        self.conditions['contains'] = lambda string: template in string
        return self

    def min_len(self, length):
        self.conditions['min_len'] = lambda string: len(string) >= length
        return self

    def is_valid(self, string):
        return all(map(lambda check_function: check_function(string), self.conditions.values()))
