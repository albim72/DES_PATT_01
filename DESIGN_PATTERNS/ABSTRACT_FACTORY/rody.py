from units import Unit

#jednostki rodu Stark
class StarkWarrior(Unit):
    def attack(self):
        return "Stark Warrior atakuje za pomocą miecza!"
    
class StarkMage(Unit):
    def attack(self):
        return "Stark Mage atakuje za podmuchu zimy!"


# jednostki rodu Lannister
class LanisterWarrior(Unit):
    def attack(self):
        return "Lannister Warrior atakuje za pomocą łuku!"


class LannisterMage(Unit):
    def attack(self):
        return "Lannister Mage atakuje za pomocą kuli ognistej!"
    
# jednostki rodu Targaryen
class TargaryenWarrior(Unit):
    def attack(self):
        return "Targaryen Warrior atakuje za pomocą smoka!"


class TargaryenMage(Unit):
    def attack(self):
        return "Targaryen Mage atakuje za pomocą oddechu smoka!"
