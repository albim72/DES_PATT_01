from units import UnitFactory
from rodyfactory import StarkFactory, LannisterFactory, TargaryenFactory


def game(factory:UnitFactory):
    warrior = factory.create_warrior()
    mage = factory.create_mage()

    print(warrior.attack())
    print(mage.attack())

#użycie w grze różnych rodów
print("Stark House:")
game(StarkFactory())

print("Lannister House:")
game(LannisterFactory())

print("Targaryen House:")
game(TargaryenFactory())
