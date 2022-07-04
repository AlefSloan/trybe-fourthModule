import pytest
from exercise_3 import validate_email


def test_fizz_buzz_function():
    assert validate_email("FulanoDeTal@hotmail.com") is None
    assert validate_email("Fulano-De-Tal@hotmail.com") is None
    assert validate_email("Fulano_De_Tal@hotmail.com") is None
    assert validate_email("Fulano123@hotmail.com") is None
    assert validate_email("Fulano123@hotmail123.com") is None
    assert validate_email("fulano@hotmail.com") is None

    with pytest.raises(ValueError):
        assert validate_email("1Fulano@hotmail.com")
    with pytest.raises(ValueError):
        assert validate_email("Fulano123@hotmail_.com")
    with pytest.raises(ValueError):
        assert validate_email("Fulano123@hotmail-.com")
    with pytest.raises(ValueError):
        assert validate_email("Fulano123@hotmail.comm")
    with pytest.raises(ValueError):
        assert validate_email("Fulano123@hotmail.c1m")
