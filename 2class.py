class Player:
    def __init__(self, name: str, health: int, attack_power: int) -> None:
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power

    def attack(self, monster):
        monster.take_damage(self.__attack_power)

    def take_damage(self, amount):
        self.__health -= amount

    def is_alive(self):
        return self.__health > 0

    @property
    def attack_power(self):
        return self.__attack_power

    @attack_power.setter
    def attack_power(self, value):
        self.__attack_power = value

    @property
    def health(self):
        return self.__health

    @property
    def name(self):
        return self.__name

class Monster:
    def __init__(self, name: str, health: int, attack_power: int) -> None:
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power

    def attack(self, player):
        player.take_damage(self.__attack_power)

    def take_damage(self, amount):
        self.__health -= amount

    def is_alive(self):
        return self.__health > 0

    @property
    def attack_power(self):
        return self.__attack_power

    @attack_power.setter
    def attack_power(self, value):
        self.__attack_power = value

    @property
    def health(self):
        return self.__health

    @property
    def name(self):
        return self.__name

p = Player(name="CHRISTINA", health=100, attack_power=20)
m = Monster(name="Dragon", health=150, attack_power=10)
print("Christina's Health:", p.health)
print("Monster's Health:", m.health)

# Player attacks monster
p.attack(m)
print("Monster's health after attack:", m.health)

# Monster attacks player
m.attack(p)
print("Player's health after monster's attack:", p.health)