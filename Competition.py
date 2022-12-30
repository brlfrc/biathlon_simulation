"""
competition is the class to create a race.
"""
import math as ma

import Circuit as ci
import Competitor as cm

Debug=False
print_partial_ranking=False

class Competition():
    """
    competition descirbe the race.
    In competition there are the circuit and a list of competitors.
    The main function is the race.
    """
    def __init__(self,
        competitors= cm.random_competitors_generetor(),
        circuit= ci.Circuit()
        ):
        self.competitors = competitors
        self.circuit=circuit

    def race_simulation (self):
        """
        race simulation simulate the race.
        First simulate race for each competitor
        Then for each partial sort competitors and save in partial_position
        """
        for competitor in self.competitors:
            competitor.result_race (self.circuit)
            if Debug:
                print(competitor.name + ": " + str(competitor.curr_time[0]))

        number_partial=len(self.competitors[0].curr_time)
        for i in range(number_partial):
            self.competitors=sorted(self.competitors, key = lambda x: x.curr_time[i])

            if print_partial_ranking:
                print("partial ranking ", str(i+1))

            partial_position=0
            for competitor in self.competitors:
                partial_position=partial_position+1
                competitor.partial_position.append(partial_position)
                if print_partial_ranking:
                    print(competitor.name + " " +  str(ma.ceil(competitor.curr_time[i])))

    def final_result(self):
        """
        this function simulate race and then print final ranking
        """
        self.race_simulation()
        print("RANKING:")
        for competitor in self.competitors:
            print(competitor.name + " " + str(competitor.partial_position))
