from units import UnitFactory
from rody import *

class StarkFactory(UnitFactory):
    def create_warrior(self) -> Unit:
        return StarkWarrior()

    def create_mage(self) -> Unit:
        return StarkMage()
    
    
class LannisterFactory(UnitFactory):
    def create_warrior(self) -> Unit:
        return LanisterWarrior()

    def create_mage(self) -> Unit:
        return LannisterMage()
    
class TargaryenFactory(UnitFactory):
    def create_warrior(self) -> Unit:
        return TargaryenWarrior()

    def create_mage(self) -> Unit:
        return TargaryenMage()
