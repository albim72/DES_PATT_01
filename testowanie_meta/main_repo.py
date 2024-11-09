import pytest
from metainfo import MojaKlasa

def test_meta_info_added():
    assert hasattr(MojaKlasa, 'meta_info'), "Klasa nie ma atrybutu 'meta info'"
    assert MojaKlasa.meta_info == "Dodano przez metaklasę", "Atrybut" 'meta_info' "posiada niewlasciwa zawartosc"