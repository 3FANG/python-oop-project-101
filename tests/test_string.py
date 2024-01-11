from validator.validate import Validator


def test_contains():
    """Сheck that string contains a specific substring"""
    schema = Validator().string()
    assert schema.contains('what').is_valid('what does the fox say') is True
    assert schema.contains('whatthe').is_valid('what does the fox say') is False


def test_priorities():
    "Check that the last validator called has priority"
    v = Validator()
    assert v.string().min_len(10).min_len(4).is_valid('Hexlet') is True
