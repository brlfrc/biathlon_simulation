from dataclasses import dataclass
from . import Skills as sk

@dataclass
class Player:
    name: str = "Mario"
    surname: str = "Rossi"
    fitness: sk.Fitness = sk.Fitness(level = 0)
    shooting: sk.Shooting = sk.Shooting(level = 0)
    precision: sk.Precision = sk.Precision(level = 0)

    def refresh_skills(self):
        self.fitness.evaluate()
        self.shooting.evaluate()
        self.precision.evaluate()
