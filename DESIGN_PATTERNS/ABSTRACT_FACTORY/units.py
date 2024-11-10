from abc import ABC, abstractmethod

#interfejs jednostki
class Unit(ABC):
    @abstractmethod
    def attack(self):
        pass
    
#interfejs fabryki jednostek
class UnitFactory(ABC):
    @abstractmethod
    def create_warrior(self) -> Unit:
        pass
    
    @abstractmethod
    def create_mage(self) -> Unit:
        pass
