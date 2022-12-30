from dataclasses import dataclass

@dataclass
class Skill:
    level: int
    mean: float = None
    sigma: float = None

    def evaluate(self):
        raise NotImplementedError


class Shooting(Skill):
    RAPIDITY_FALLBACK = (10, 10)
    RAPIDITY_LEVELS = {
        0: (50, 2),
        1: (42, 3),
        2: (35, 4)
    }
   
    def evaluate(self):
        levels = None
        if self.level in Shooting.RAPIDITY_LEVELS:
            levels = Shooting.RAPIDITY_LEVELS[self.level]
        else:
            levels = Shooting.RAPIDITY_FALLBACK
        self.mean = levels[0]
        self.sigma = levels[1]


class Fitness(Skill):
    FITNESS_FALLBACK = (10, 10)
    FITNESS_LEVELS = {
        0: (10, 2),
        1: (15, 3),
        2: (20, 4)
    }

    def evaluate(self):
        levels = None
        if self.level in Fitness.FITNESS_LEVELS:
            levels = Fitness.FITNESS_LEVELS[self.level]
        else:
            levels = Fitness.FITNESS_LEVELS
        self.mean = levels[0]
        self.sigma = levels[1]

class Precision(Skill):
    PRECISION_FALLBACK = 0.5
    PRECISION_LEVELS = {
        0: 0.7,
        1: 0.8,
        2: 0.9
    }

    def evaluate(self):
        score = None
        if self.level in Precision.PRECISION_LEVELS:
            score = Precision.PRECISION_LEVELS[self.level]
        else:
            score = Precision.PRECISION_LEVELS
        self.mean = score
        self.sigma = score