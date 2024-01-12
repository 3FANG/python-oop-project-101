"""Test the general init interface and required values ​​for some data types."""
from validator.validate import Validator


def test_instantiation():
    """Check that Validator.string() and Validator.number() returning a new object."""
    validator = Validator()
    string_schema = validator.string()
    string_schema2 = validator.string()
    assert string_schema != string_schema2

    number_schema = validator.number()
    number_schema2 = validator.number()
    assert number_schema != number_schema2


def test_required():
    """Test String.required() and Number.required() that checks for non-empty value."""
    validator = Validator()
    number_schema = validator.number()
    assert number_schema.is_valid(None) is True

    number_schema.required()
    assert number_schema.is_valid(None) is False
    assert number_schema.is_valid(7) is True

    string_schema = validator.string()
    assert string_schema.is_valid('') is True
    assert string_schema.is_valid(None) is True
    assert string_schema.is_valid('what does the fox say') is True

    string_schema.required()
    assert string_schema.is_valid(None) is False
    assert string_schema.is_valid('') is False
    assert string_schema.is_valid('hexlet') is True

    list_schema = Validator().list()
    assert list_schema.is_valid(None) is True

    list_schema = list_schema.required()
    assert list_schema.is_valid([]) is True
    assert list_schema.is_valid(['hexlet']) is True
