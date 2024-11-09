import pytest
from metainfo import MojaKlasa
from enforce import ValidClass, EnforceAttributeMeta

def test_meta_info_added():
    assert hasattr(MojaKlasa,'meta_info'),"Klasa nie ma atrybutu 'meta_info'"
    assert MojaKlasa.meta_info == "Dodano przez metaklasę","Atrybut 'meta_info' posiada niewłaściwą zawartość"

def test_valid_class():
    assert hasattr(ValidClass,'required_attribute'),"Klasa ValidClass nie posiada atrybytu - required_attribute"

def test_invalid_class():
    with pytest.raises(TypeError,match="Klasa musi mieć atrybut - 'required_attribute'"):
        class InvalidClass(metaclass=EnforceAttributeMeta):
            pass
