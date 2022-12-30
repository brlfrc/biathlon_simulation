"""
competitor is a sub class of player. Describe player in a race
"""
import math as ma
import random as rn
import itertools
import numpy as np

from Player import Player
from Skills import Fitness, Precision, Shooting

class Competitor:
    """
    competitor is the class for a player in a race.
    So there are the main methods for simulation of events: lap and shooting
    """
    def __init__(self,
        name = "Mario",
        surname = "Rossi",
        fitness_level = 0,
        shooting_rapidity_level = 0,
        precision_level=0,
        start_position=0,
        player: Player = None
        ):
        self.player = Player(
            name= name,
            surname= surname,
            fitness= Fitness(fitness_level),
            shooting= Shooting(shooting_rapidity_level),
            precision= Precision(precision_level)
        )
        self.player.refresh_skills()

        self.start_position = start_position
        self.partial_position =[]
        self.curr_time=[]
        self.target_error =[]
        self.v_penalty_lap =[]
        self.is_finished = False
        self.is_started = False
        self.is_shooting = False

    def name(self):
        return self.player.name

    def lap_simulation(self, circuit):
        """
        Simulate time elapsed during a lap
        """
        v_lap = np.random.normal(self.player.fitness.mean, self.player.fitness.sigma)
        return circuit.lap_length/v_lap

    def shooting_simulation(self, circuit):
        """
        Simulate time elapsed during a shooting.
        penalty_lap == true there are penalty laps, else there is 1 minute of penalty
        """
        t_shot = np.random.normal(self.player.shooting.mean, self.player.shooting.sigma)
        prob_precision= self.shooting_precision(t_shot)

        valid_target = np.random.binomial(5, prob_precision)
        number_penalty_lap= 5 - valid_target
        self.target_error.append(number_penalty_lap)

        if circuit.penalty_lap_race:
            v_penalty_lap = np.random.normal(self.player.fitness.mean, self.player.fitness.sigma)
            self.v_penalty_lap.append(v_penalty_lap)
            return t_shot+number_penalty_lap*circuit.penalty_lap_length/v_penalty_lap
        else:
            return t_shot+number_penalty_lap*60

    def shooting_precision (self, t_shot):
        """
        return the probability of binomial process
        we use function:
            f(t_shot)= 2/pi * atan(t_shot - t_bar)
        where
            t_bar = optimal_time - tan(pi/2 * probability_at_optimal)
        """
        t_bar = self.player.shooting.mean - ma.tan(ma.pi/2 * self.player.precision.mean)
        precision_p= 2/ma.pi * ma.atan(t_shot-t_bar)
        if precision_p>0.5:
            return precision_p
        else:
            return 0.5

    def result_race (self, circuit):
        """
        Simulate race for a competitor.
        return all times after each lap and each shot.
        return a comulative time
        """
        #first lap
        curr_time=[self.lap_simulation(circuit),]

        #the other lap
        for _ in itertools.repeat(None, circuit.number_of_shooting):
        #for i in range(circuit.number_of_shooting):
            curr_time.append(curr_time[-1]+self.shooting_simulation(circuit))
            curr_time.append(curr_time[-1]+self.lap_simulation(circuit))

        self.curr_time= curr_time

        return curr_time

def random_competitors_generetor (num_comp=15):
    """
    random generator of num_comp competitor 
    """
    competitors=[]
    for i in range(num_comp):
        name = "comp " + str(i + 1)
        surname = "comp " + str(i +1)
        fitness_level = rn.randint(0, 2)
        shooting_rapidity_level = rn.randint(0, 2)
        precision_level=rn.randint(0, 2)
        start_position=i
        competitors.append(
            Competitor(name, surname, fitness_level, shooting_rapidity_level,
                       precision_level, start_position))
    return competitors
