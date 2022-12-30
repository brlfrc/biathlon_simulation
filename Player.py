from dataclasses import dataclass
from Skills import Fitness, Precision, Shooting

@dataclass
class Player:
    name: str = "Mario"
    surname: str = "Rossi"
    fitness: Fitness = Fitness(level = 0)
    shooting: Shooting = Shooting(level = 0)
    precision: Precision = Precision(level = 0)

    def refresh_skills(self):
        self.fitness.evaluate()
        self.shooting.evaluate()
        self.precision.evaluate()
