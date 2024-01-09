class DataType:
    def __init__(self):
        self.conditions = {}

    def is_valid(self, string):
        return all(map(lambda check_function: check_function(string), self.conditions.values()))


class String(DataType):
    def required(self):
        self.conditions['required'] = lambda string: string not in (None, '')
        return self

    def contains(self, template):
        self.conditions['contains'] = lambda string: template in string
        return self

    def min_len(self, length):
        self.conditions['min_len'] = lambda string: len(string) >= length
        return self


class Number(DataType):
    def required(self):
        self.conditions['required'] = lambda number: isinstance(number, int)
        return self

    def positive(self):
        self.conditions['positive'] = lambda number: number > 0
        return self

    def range(self, start, stop):
        self.conditions['range'] = lambda number: start <= number <= stop
        return self
