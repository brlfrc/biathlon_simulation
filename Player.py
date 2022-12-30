"""
player is the class to simulate the generic player.
The main characteristics of a player are:
   - fitness level, link with v_mean and sigma_mean
   - shooting rapidity, link with t_shot and sigma_shot
   - precision level, a function of t_shot to set precision in Bernoulli events
"""

class Player:
    """
    player is the main class.
    """
    def __init__(
        self,
        name = "Mario",
        surname = "Rossi",
        fitness_level = 0,
        shooting_rapidity_level = 0,
        precision_level=0
    ):
        self.name= name
        self.surname = surname
        self.v_mean=fitness_parameter(fitness_level)[0]
        self.sigma_v=fitness_parameter(fitness_level)[1]
        self.t_shooting=shooting_parameter(shooting_rapidity_level)[0]
        self.sigma_t=shooting_parameter(shooting_rapidity_level)[1]
        self.precision_parameter=precision_parameter(precision_level)

def fitness_parameter (fitness_level):
    """
    fitness_parameter return the fitness level.
    In simulation this is the mean speed in a lap and the variance.
    """
    if fitness_level==0:
        return [10,2]
    if fitness_level==1:
        return [15,3]
    if fitness_level==2:
        return [20,4]
    else:
        return [10,10]

def shooting_parameter (shooting_rapidity_level):
    """
    shooting_parameter return the shooting rapidity.
    In simulation this is the shooting time.
    """
    if shooting_rapidity_level==0:
        return [50,2]
    if shooting_rapidity_level==1:
        return [42,3]
    if shooting_rapidity_level==2:
        return [35,4]
    else:
        return [10,10]

def precision_parameter(precision_level):
    """
    precision_par_function return the parameter for shooting simulation.
    at the optimal time self.t_shooting which is the probability (ex 0.90 a 10 sec)
    """
    if precision_level==0:
        return 0.7
    if precision_level==1:
        return 0.8
    if precision_level==2:
        return 0.9
    else:
        return 0.5
