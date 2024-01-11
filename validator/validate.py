"""Validator is described here.

A validator is a kind of manager for data types.
"""
from validator.datatypes import (CheckFunction, DictData, ListData, Number,
                                 String)


class Validator(object):
    """A class representing a validator.

    It calls the appropriate data types to test the specified conditions.
    """

    def __init__(self):
        """Init the map of DataTypes."""
        self.datatypes = {
            'string': String,
            'number': Number,
            'list': ListData,
            'dict': DictData,
        }
        self.custom_validators = {datatype: {} for datatype in self.datatypes.keys()}

    def string(self):
        """Represent string.

        Returns:
            string_object: Сlass object that represents the strings.
        """
        return self.datatypes['string'](self)

    def number(self):
        """Represent number.

        Returns:
            number_object: Сlass object that represents the number.
        """
        return self.datatypes['number'](self)

    def list(self):
        """Represent list.

        Returns:
            list_object: Сlass object that represents the list.
        """
        return self.datatypes['list'](self)

    def dict(self):
        """Represent dict.

        Returns:
            dict_object: Сlass object that represents the dict.
        """
        return self.datatypes['dict'](self)

    def add_validator(self, datatype, name, fn):
        """Add a custom check function (condition) to specified data type.

        Args:
            datatype: Specified data type (string, number, list, dict).
            name: Name of condition.
            fn: Check-function.
        """
        self.custom_validators[datatype][name] = CheckFunction(check_function=fn, args=[])
