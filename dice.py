import random
from dataclasses import dataclass

@dataclass
class Die:
    _value: int = 1

    @property
    def value(self):
        return self._value

    def roll(self):
        self._value = random.randrange(1, 7)

@dataclass
class Dice:
    def __init__(self):
        self._list = []

    @property
    def list(self):
        return tuple(self._list)

    def addDie(self, die):
        self._list.append(die)

    def rollAll(self):
        for die in self._list:
            die.roll()

# Example usage
d1 = Die()
d2 = Die()
dice_set = Dice()
dice_set.addDie(d1)
dice_set.addDie(d2)

print("Before rolling:")
print("Die 1:", d1.value)
print("Die 2:", d2.value)

dice_set.rollAll()

print("After rolling:")
print("Die 1:", d1.value)
print("Die 2:", d2.value)
    
