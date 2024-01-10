class DataType:
    def __init__(self):
        self.conditions = {}

    '''
    Check the specified string for compliance with each condition
    by substituting a string as an argument into an anonymous function
    '''
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
        self.conditions['positive'] = lambda number: True if number is None else number > 0
        return self

    def range(self, start, stop):
        self.conditions['range'] = lambda number: start <= number <= stop
        return self


class ListData(DataType):
    def required(self):
        self.conditions['required'] = lambda list_of_data: type(list_of_data) == list
        return self

    def sizeof(self, size):
        self.conditions['sizeof'] = lambda list_of_data: len(list_of_data) == size
        return self


class DictData(DataType):
    def shape(self, scheme: dict):
        self.conditions.update(scheme)
        return self

    def is_valid(self, map_of_data: dict):
        for key, data_obj in self.conditions.items():
            if not data_obj.is_valid(map_of_data[key]):
                return False
        return True
