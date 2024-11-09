import pytest

class PlikManager:
    def __init__(self, sciezka):
        self.sciezka = sciezka
        self.plik = None

    def __enter__(self):
        self.plik = open(self.sciezka, 'w')
        return self.plik

    def __exit__(self, exc_type, exc_value, traceback):
        if self.plik:
            self.plik.close()

def test_plik_manager(tmp_path):
    testowa_sciezka = tmp_path / "testowy_plik.txt"

    # Użycie PlikManagera z context managerem
    with PlikManager(testowa_sciezka) as plik:
        plik.write("Testowanie PlikManagera!")

    # Sprawdzenie, czy plik został zamknięty
    assert plik.closed is True
