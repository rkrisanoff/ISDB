from enum import Enum
import random as rnd


NamesDomain = [
    'Harry',
    'Oliver',
    'Jack',
    'Charlie',
    'Thomas',
    'Jacob',
    'Alfie',
    'Riley',
    'William',
    'James'
]
GenderDomain = ['male', 'female']

PositronicBrain = [
    "LYNN", "L2B8D"
]


class Domain(Enum):
    def GENDER(): return rnd.choice(GenderDomain)
    def NAME(): return rnd.choice(NamesDomain)
    def AGE(): return rnd.randint(18, 60)
    def FLAG(): return rnd.random() >= 0.5
    def INDEX(): return rnd.randint(1, 1000)
    def NONEGATIVE_INTEGER(): return rnd.randint(0, 20000)
    def NATURAL(): return rnd.randint(1, 1000)
    def POSITRONIC_BRAIN(): return rnd.choice(PositronicBrain)
