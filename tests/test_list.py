from validator.validate import Validator


def test_sizeof_list():
    """Check  the compliance with the specified length"""
    schema = Validator().list()
    schema.sizeof(2)
    assert schema.is_valid(['hexlet']) is False
    assert schema.is_valid(['hexlet', 'code-basics']) is True
