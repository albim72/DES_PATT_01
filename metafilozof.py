odp = input("Czy Ziemia jest płaska? Czy chcesz zna odpowiedź? (t/n): ")
if odp.lower() == "t":
    required = True
else:
    required = False

def odpowiedz(self):
    return "Tak! Ziemia jest płaska!"


def brak(self):
    return "brak odpowiedzi..."


class SednoOdpowiedzi(type):
    def __init__(cls,clsname,bases,attrs):
        if required:
            cls.odpowiedz = odpowiedz
        else:
            cls.odpowiedz = brak

class Arystoteles(metaclass=SednoOdpowiedzi):
    pass

class Platon(metaclass=SednoOdpowiedzi):
    pass

class SwTomasz(metaclass=SednoOdpowiedzi):
    pass



fil1 = Arystoteles()
print(f"Filozof {fil1.__class__.__name__} twierdzi: {fil1.odpowiedz()}")

fil2 = Platon()
print(f"Filozof {fil2.__class__.__name__} twierdzi: {fil2.odpowiedz()}")

fil3 = SwTomasz()
print(f"Filozof {fil3.__class__.__name__} twierdzi: {fil3.odpowiedz()}")



#zadanie 1 -> skonstruuj rozwiązanie pozwalające Kopernikowi na wypowiedź: Nie! Ziemia jest elipsoidą!
#pozostaw aktualną konstrukcję klas (klasa Kopernik oparta ma byc na metaklasie SednoOdpowiedzi

#zadanie 2 -> przebuduj rozwiązanie w ten sposób aby można dodac dowolną ilosc klas opisujących filozofów nowożytnych
#którzy będą odpowiadac tak jak Kopernik
