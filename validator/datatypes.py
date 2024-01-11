"""Classes-data types are described here.

As well as a class representing a separate check function.
"""
from collections.abc import Callable
from typing import NamedTuple, Optional


class CheckFunction(NamedTuple):
    """Сlass representing a single condition."""

    check_function: Callable[[int], bool] | Callable[[str], bool]
    args: list[Optional[int | str]] = []


class DataType(object):
    """Base class for data type."""

    def __init__(self, validator):
        """Init the variables.

        Args:
            validator: Validator object through which this type is called.
        """
        self.validator = validator
        self.conditions: dict[str, CheckFunction] = {}
        self.name = None

    def is_valid(self, value_being_checked):
        """Check the specified value for compliance with each condition.

        By substituting a value as an argument into a check function.

        Args:
            value_being_checked: The value that we will test for compliance with type conditions.

        Returns:
            bool: Whether the specified value meets the conditions or not.
        """
        for check_function, args in self.conditions.values():
            if not check_function(value_being_checked, *args):
                return False
        return True

    def test(self, name, condition_value):
        """Takes a custom validation function from a Validator object.

        By specified name and adds it to the conditions dictionary

        Args:
            name: Name of custom function.
            condition_value: Value used in function condition.

        Returns:
            self: self Data type object.
        """
        condition: CheckFunction = self.validator.custom_validators[self.name][name]
        condition.args.append(condition_value)
        self.conditions[name] = condition
        return self


class String(DataType):
    """Represent a string data type."""

    def __init__(self, validator):
        """Init the variables how in DataType.

        Args:
            validator: Validator object through which this type is called.
        """
        super().__init__(validator)
        self.name = 'string'

    def required(self):
        """Non-empty value (not None) and any non-empty string.

        Returns:
            self: self Data type object.
        """
        self.conditions['required'] = CheckFunction(
            lambda string: all(string != empty for empty in (None, '')),
        )
        return self

    def contains(self, template):
        """Check that string contains a specific substring.

        Args:
            template: Substring that the string must contain.

        Returns:
            self: self Data type object.
        """
        self.conditions['contains'] = CheckFunction(lambda string: template in string)
        return self

    def min_len(self, length):
        """Check that string equal to or longer than the specified number.

        Args:
            length: Minimum line length.

        Returns:
            self: self Data type object.
        """
        self.conditions['min_len'] = CheckFunction(lambda string: len(string) >= length)
        return self


class Number(DataType):
    """Represent a int data type."""

    def __init__(self, validator):
        """Init the variables how in DataType.

        Args:
            validator: Validator object through which this type is called.
        """
        super().__init__(validator)
        self.name = 'number'

    def required(self):
        """Non-empty value (not None) and any non-empty string.

        Returns:
            self: self Data type object.
        """
        self.conditions['required'] = CheckFunction(lambda number: isinstance(number, int))
        return self

    def positive(self):
        """Check that the number must be positive.

        Returns:
            self: self Data type object.
        """
        self.conditions['positive'] = CheckFunction(
            lambda number: True if number is None else number > 0,
            )
        return self

    def range(self, start, stop):
        """Check that the range in which the number must fall, including boundaries.

        Args:
            start: start of range.
            stop: end of range.

        Returns:
            self: self Data type object.
        """
        self.conditions['range'] = CheckFunction(lambda number: start <= number <= stop)
        return self


class ListData(DataType):
    """Represent a list data type."""

    def __init__(self, validator):
        """Init the variables how in DataType.

        Args:
            validator: Validator object through which this type is called.
        """
        super().__init__(validator)
        self.name = 'list'

    def required(self):
        """Non-empty value (not None) and any non-empty string.

        Returns:
            self: self Data type object.
        """
        self.conditions['required'] = CheckFunction(lambda list_data: isinstance(list_data, list))
        return self

    def sizeof(self, size):
        """Check that the length of the array is equal to the specified one.

        Args:
            size: The length of the array.

        Returns:
            self: self Data type object.
        """
        self.conditions['sizeof'] = CheckFunction(lambda list_of_data: len(list_of_data) == size)
        return self


class DictData(DataType):
    """Represen a dict data type."""

    def __init__(self, validator):
        """Init the variables.

        Args:
            validator: Validator object through which this type is called.
        """
        self.validator = validator
        self.conditions: dict[str, DataType] = {}
        self.name = 'dict'

    def shape(self, schema: dict):
        """Describe validation for the key dictionary.

        Args:
            schema: Dictionary in the form 'name_value'=DataType.

        Returns:
            self: self Data type object.
        """
        self.conditions.update(schema)
        return self

    def is_valid(self, map_of_data: dict):
        """Check the specified string for compliance with each condition.

        By substituting a value as an argument into a check function.

        Args:
            map_of_data: Сhecked dictionary with values like 'name_value'='value'.

        Returns:
            bool: Whether the specified value meets the conditions or not.
        """
        for key, data_obj in self.conditions.items():
            if not data_obj.is_valid(map_of_data[key]):
                return False
        return True
