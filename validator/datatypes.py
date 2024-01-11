from typing import NamedTuple, Optional
from collections.abc import Callable


class CheckFunction(NamedTuple):
    """Сlass representing a single condition"""
    check_function: Callable[[int], bool] | Callable[[str], bool]
    args: list[Optional[int | str]]


class DataType:
    """Base class for data type"""
    def __init__(self, validator):
        self.validator = validator
        self.conditions: dict[str, CheckFunction] = {}
        self.name = None

    '''
    Check the specified string for compliance with each condition
    by substituting a value as an argument into a check function
    '''
    def is_valid(self, value):
        for check_function, args in self.conditions.values():
            if not check_function(value, *args):
                return False
        return True

    '''
    Takes a custom validation function from a Validator object
    by specified name and adds it to the conditions dictionary
    '''
    def test(self, name, value):
        condition: CheckFunction = self.validator.custom_validators[self.name][name]
        condition.args.append(value)
        self.conditions[name] = condition
        return self


class String(DataType):
    def __init__(self, validator):
        super().__init__(validator)
        self.name = 'string'

    def required(self):
        self.conditions['required'] = CheckFunction(check_function=lambda string: string not in (None, ''), args=[])
        return self

    def contains(self, template):
        self.conditions['contains'] = CheckFunction(check_function=lambda string: template in string, args=[])
        return self

    def min_len(self, length):
        self.conditions['min_len'] = CheckFunction(check_function=lambda string: len(string) >= length, args=[])
        return self


class Number(DataType):
    def __init__(self, validator):
        super().__init__(validator)
        self.name = 'number'

    def required(self):
        self.conditions['required'] = CheckFunction(check_function=lambda number: isinstance(number, int), args=[])
        return self

    def positive(self):
        self.conditions['positive'] = CheckFunction(check_function=lambda number: True if number is None else number > 0, args=[])
        return self

    def range(self, start, stop):
        self.conditions['range'] = CheckFunction(check_function=lambda number: start <= number <= stop, args=[])
        return self


class ListData(DataType):
    def __init__(self, validator):
        super().__init__(validator)
        self.name = 'list'

    def required(self):
        self.conditions['required'] = CheckFunction(check_function=lambda list_of_data: type(list_of_data) == list, args=[])
        return self

    def sizeof(self, size):
        self.conditions['sizeof'] = CheckFunction(check_function=lambda list_of_data: len(list_of_data) == size, args=[])
        return self


class DictData(DataType):
    def __init__(self, validator):
        self.validator = validator
        self.conditions: dict[str, DataType] = {}
        self.name = 'dict'

    def shape(self, schema: dict):
        self.conditions.update(schema)
        return self

    def is_valid(self, map_of_data: dict):
        for key, data_obj in self.conditions.items():
            if not data_obj.is_valid(map_of_data[key]):
                return False
        return True
