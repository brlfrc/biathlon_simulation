"""
competition is the file with all function needing to simulate the race
"""
import math as ma

import numpy as np


def single_race(player, circuit, start_time=0):
    """
    single_race this ih the function to simulate the race for a single player
    """
    # first lap
    curr_time = lap_simulation(player, circuit, start_time)

    # first shooting
    curr_time = shooting_simulation(player, circuit, curr_time)

    # second lap
    curr_time = lap_simulation(player, circuit, curr_time)

    # second shooting
    curr_time = shooting_simulation(player, circuit, curr_time)

    # last lap
    curr_time = lap_simulation(player, circuit, curr_time)

def lap_simulation(player, circuit, curr_time):
    """
    Simulate time elapsed during a lap
    """
    v_lap = np.random.normal(player.v_mean, player.sigma_v)
    curr_time += circuit.lap_length/v_lap
    print(str(ma.ceil(curr_time*100)/100) + " velocità " + str(ma.ceil(v_lap*100)/100) + " lunghezza giro " + str(circuit.lap_length))
    return curr_time

def shooting_simulation(player, circuit, curr_time):
    """
    Simulate time elapsed during a shooting
    """
    t_shot = np.random.normal(player.t_shooting, player.sigma_t)
    curr_time += t_shot
    prob_precision= shooting_precision (player, t_shot)
    valid_target = np.random.binomial(circuit.number_targets, prob_precision)
    number_penalty_lap= circuit.number_targets- valid_target
    v_penalty_lap = np.random.normal(player.v_mean, player.sigma_v)
    curr_time+= number_penalty_lap*circuit.penalty_lap_length/v_penalty_lap
    print(str(ma.ceil(curr_time*100)/100) + " errori " + str(number_penalty_lap)+ " precision " + str(ma.ceil(prob_precision*100)/100))
    return curr_time

def shooting_precision (player, t_shot):
    """
    return the probability of binomial process
    we use function:
        f(t_shot)= 2/pi * atan(t_shot - t_bar)
    where
        t_bar = optimal_time - tan(pi/2 * probability_at_optimal)
    """
    t_bar = player.t_shooting - ma.tan(ma.pi/2 * player.precision_parameter)
    precision_p= 2/ma.pi * ma.atan(t_shot-t_bar)
    if precision_p>0.5:
        return precision_p
    else:
        return 0.5
