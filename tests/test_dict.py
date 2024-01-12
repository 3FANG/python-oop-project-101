"""Test the DictData which is represent a dict data type."""
from validator.validate import Validator


def test_shape():
    """Key validation check."""
    validator = Validator()
    schema = validator.dict()
    schema.shape({
        'name': validator.string().required(),
        'age': validator.number().positive(),
    })
    assert schema.is_valid({'name': 'kolya', 'age': 100}) is True
    assert schema.is_valid({'name': 'maya', 'age': None}) is not True
    assert schema.is_valid({'name': '', 'age': None}) is False
    assert schema.is_valid({'name': 'ada', 'age': -5}) is False
