#This is the player which represents the user.
class Warrior:
    def __init__(self, health: int, name: str, attack_power: int) -> None:
        self.health = health
        self.attack_power = attack_power
        self.name = name

    def get_damage(self, amount):
        self.health -= amount

#This is the first monster.
class Monster:
    def __init__(self, attack_power: int, warrior, health: int, name: str) -> None:
        self.attack_power = attack_power
        self.warrior = warrior
        self.health = health
        self.name = name

    def get_damage(self, amount):
        self.health -= amount   

w = Warrior(health=100, attack_power=20, name="Warrior")
m = Monster(attack_power=10, warrior=w, health=90, name="Dragon")

#Outputs
w.get_damage(10)