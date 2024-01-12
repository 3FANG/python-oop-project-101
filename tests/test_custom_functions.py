"""Testing the add custom validator functional."""
from validator import Validator


def test_custom_function():
    """Check the custom functions."""
    validator = Validator()
    validator.add_validator('string', 'startWith', lambda string, start: string.startswith(start))
    schema = validator.string().test('startWith', 'H')
    assert schema.is_valid('exlet') is False
    assert schema.is_valid('Hexlet') is True

    validator.add_validator('number', 'min', lambda number, min_number: number >= min_number)
    schema = validator.number().test('min', 5)
    assert schema.is_valid(4) is False
    assert schema.is_valid(6) is True
