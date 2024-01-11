from validator.validate import Validator


def test_instantiation():
    '''Check that Validator.string() and Validator.number() returning a new object'''
    v = Validator()
    string_schema = v.string()
    string_schema2 = v.string()
    assert string_schema != string_schema2

    number_schema = v.number()
    number_schema2 = v.number()
    assert number_schema != number_schema2


def test_required():
    """Test String.required() and Number.required() that checks for non-empty value"""
    v = Validator()
    number_schema = v.number()
    assert number_schema.is_valid(None) is True

    number_schema.required()
    assert number_schema.is_valid(None) is False
    assert number_schema.is_valid(7) is True

    string_schema = v.string()
    assert string_schema.is_valid('') is True
    assert string_schema.is_valid(None) is True
    assert string_schema.is_valid('what does the fox say') is True

    string_schema.required()
    assert string_schema.is_valid(None) is False
    assert string_schema.is_valid('') is False
    assert string_schema.is_valid('hexlet') is True

    schema = v.list()
    assert schema.is_valid(None) is True

    schema = schema.required()
    assert schema.is_valid([]) is True
    assert schema.is_valid(['hexlet']) is True
