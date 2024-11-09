odp = input("Czy Ziemia jest płaska? Czy chcesz zna odpowiedź? (t/n): ")
if odp.lower() == "t":
    required = True
else:
    required = False

def odpowiedz(self):
    return "Tak! Ziemia jest płaska!"

def nowa_odpowiedz(self):
    return "Nie! Ziemia jest elipsoidą!"

def brak(self):
    return "brak odpowiedzi..."


class SednoOdpowiedzi(type):
    def __init__(cls,clsname,bases,attrs):
        if required:
            if attrs.get('n'):
                cls.odpowiedz = nowa_odpowiedz
            else:
                cls.odpowiedz = odpowiedz
        else:
            cls.odpowiedz = brak

class Arystoteles(metaclass=SednoOdpowiedzi):
    pass

class Platon(metaclass=SednoOdpowiedzi):
    pass

class SwTomasz(metaclass=SednoOdpowiedzi):
    pass

class Kopernik(metaclass=SednoOdpowiedzi):
    # def odpowiedz(self):
    #     return "Nie! Ziemia jest elipsoidą!"
    n = True

class Einstein(metaclass=SednoOdpowiedzi):
    n = True



fil1 = Arystoteles()
print(f"Filozof {fil1.__class__.__name__} twierdzi: {fil1.odpowiedz()}")

fil2 = Platon()
print(f"Filozof {fil2.__class__.__name__} twierdzi: {fil2.odpowiedz()}")

fil3 = SwTomasz()
print(f"Filozof {fil3.__class__.__name__} twierdzi: {fil3.odpowiedz()}")

fil4 = Kopernik()
print(f"Filozof {fil4.__class__.__name__} twierdzi: {fil4.odpowiedz()}")

fil5 = Einstein()
print(f"Filozof {fil5.__class__.__name__} twierdzi: {fil5.odpowiedz()}")

#zadanie 1 -> skonstruuj rozwiązanie pozwalające Kopernikowi na wypowiedź: Nie! Ziemia jest elipsoidą!
#pozostaw aktualną konstrukcję klas (klasa Kopernik oparta ma byc na metaklasie SednoOdpowiedzi

#zadanie 2 -> przebuduj rozwiązanie w ten sposób aby można dodac dowolną ilosc klas opisujących filozofów nowożytnych
#którzy będą odpowiadac tak jak Kopernik
