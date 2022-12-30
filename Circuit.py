"""
Circuit is the class to simulate the circuit and rules of the race.
The main characteristics of a circuit are:
   - name
   - lap_length
   - number of targets
   - type of race
   - number of laps
"""

import math as ma
import matplotlib.pyplot  as plt
import numpy as np

class Circuit:
    """
    Circuit is the main class. there is no method for now
    """
    def __init__(
        self,
        name = "Schilpario",
        lap_length = 3000,
        penalty_lap_length = 250,
        number_targets = 10,
        penalty_lap_race = True,
        number_of_shooting= 2,
    ):
        self.name = name
        self.lap_length = lap_length
        self.penalty_lap_length = penalty_lap_length
        self.number_targets = number_targets
        self.penalty_lap_race = penalty_lap_race
        self.number_of_shooting = number_of_shooting
        self.circuit_shape= [40, 8]
        self.penalty_shape= [10, 2]

    def plot_circuit(self):
        """
        function to plot the double ellipses of circuit.
        """
        t = np.linspace(0, 2*ma.pi, 100)

        plt.plot(
            self.circuit_shape[0]*np.cos(t),
            self.circuit_shape[1]*np.sin(t),
            'b',
            linewidth=3
        )

        plt.plot(
            self.penalty_shape[0]*np.cos(t),
            self.penalty_shape[1]*np.sin(t) - (self.circuit_shape[1]-self.penalty_shape[1]),
            'b',
            linewidth=3
        )

        plt.plot(
            np.linspace(1,1,100)*self.circuit_shape[0],
            -np.linspace(0,1,100)*self.circuit_shape[1],
            'b',
            linewidth=3
        )

        plt.plot(
            -np.linspace(1,1,100)*self.circuit_shape[0],
            -np.linspace(0,1,100)*self.circuit_shape[1],
            'b',
            linewidth=3
        )

        return plt
