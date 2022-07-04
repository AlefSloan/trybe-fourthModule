import pytest
from exercise_2 import associate_number

long_str = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'


def test_associate_number():
    assert associate_number('ABC') == '222'
    assert associate_number('DEF') == '333'
    assert associate_number('GHI') == '444'
    assert associate_number('JKL') == '555'
    assert associate_number('MNO') == '666'
    assert associate_number('PQRS') == '7777'
    assert associate_number('TUV') == '888'
    assert associate_number('WXYZ') == '9999'
    assert associate_number('-01') == '-01'

    with pytest.raises(ValueError):
        associate_number('')

    with pytest.raises(ValueError):
        associate_number('%')

    with pytest.raises(ValueError):
        associate_number(long_str)
