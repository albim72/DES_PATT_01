import pytest

class Zasob:
    def __init__(self):
        self.czy_zamkniety = False

    def zamknij(self):
        self.czy_zamkniety = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.zamknij()

def test_zasob():
    zasob = Zasob()

    with zasob:
        assert zasob.czy_zamkniety is False
    assert zasob.czy_zamkniety is True
#Mati