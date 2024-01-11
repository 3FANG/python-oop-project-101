from validator.validate import Validator


def test_positive():
    """Check that number is positive"""
    v = Validator()
    schema = v.number()
    assert schema.positive().is_valid(10) is True
    assert schema.is_valid(-8) is False


def test_range():
    """
    Check that number in a given range including boundaries
    considering previous conditions
    """
    v = Validator()
    schema = v.number()
    schema.positive()
    schema.range(-5, 5)
    print(schema.conditions)
    assert schema.is_valid(-5) is False
    assert schema.is_valid(5) is True
