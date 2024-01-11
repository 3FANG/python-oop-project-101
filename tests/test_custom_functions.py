from validator import Validator


def test_custom_function():
    '''Check the custom functions'''
    v = Validator()
    fn = lambda value, start: value.startswith(start)
    v.add_validator('string', 'startWith', fn)
    schema = v.string().test('startWith', 'H')
    assert schema.is_valid('exlet') is False
    assert schema.is_valid('Hexlet') is True

    fn = lambda value, min: value >= min
    v.add_validator('number', 'min', fn)
    schema = v.number().test('min', 5)
    assert schema.is_valid(4) is False
    assert schema.is_valid(6) is True
