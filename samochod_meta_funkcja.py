class KotrolerSamochodu(type):
    def __new__(cls, name, bases, attrs):
        print(f"Tworzenie klasy samochodu: {name}")
        attrs['informacje'] = lambda self:f"Model: {self.model}, moc silnika: {self.silnik.moc}"
        return super().__new__(cls, name, bases, attrs)

class Silnik:
    def __init__(self,moc):
        self.moc = moc

    def uruchom(self):
        return f"Silnik o mocy {self.moc} KM został uruchomiony!"


class Samochod(metaclass=KotrolerSamochodu):
    def __init__(self,model,silnik:Silnik):
        self.model = model
        self.silnik = silnik

    def uruchom_samochod(self):
        return f"Samochód {self.model}: {self.silnik.uruchom()}"

silnik1 = Silnik(150)
samochod1 = Samochod('Opel Vectra',silnik1)
print(samochod1.uruchom_samochod())
print(samochod1.informacje())
