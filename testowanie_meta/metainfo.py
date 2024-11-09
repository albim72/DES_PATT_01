class Meta(type):
    def __new__(cls,name,bases,dct):
        dct['meta_info'] = "Dodano przez metaklasę"
        return super().__new__(cls,name,bases,dct)
    
    
class MojaKlasa(metaclass=Meta):
    pass
