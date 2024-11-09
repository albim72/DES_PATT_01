import pytest

def dziel(a,b):
    if b==0:
        raise ValueError("Dzielenie przez zero!")
    return a/b

def test_dziel_zero():
    with pytest.raises(ValueError,match="Dzielenie przez zero!"):
        dziel(1,3)
