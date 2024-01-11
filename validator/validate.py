from validator.datatypes import String, Number, ListData, DictData, CheckFunction


class Validator:
    def __init__(self):
        self.datatypes = {
            'string': String,
            'number': Number,
            'list': ListData,
            'dict': DictData
        }
        self.custom_validators = {datatype: {} for datatype in self.datatypes.keys()}

    def string(self):
        return self.datatypes['string'](self)

    def number(self):
        return self.datatypes['number'](self)

    def list(self):
        return self.datatypes['list'](self)

    def dict(self):
        return self.datatypes['dict'](self)

    def add_validator(self, type, name, fn):
        self.custom_validators[type][name] = CheckFunction(check_function=fn, args=[])
