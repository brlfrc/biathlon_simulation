"""
this is the class for graphic simulation
"""

import bisect
import math as ma

import Competition as cp

class Graphic_simulation():
    """
    Graphic_simulation descirbe the race using matplot.
    """
    def __init__(self,
        competition= cp.Competition(),
        gap=30
        ):
        self.competition = competition
        self.gap=gap

    def grapich_simulation (self):
        """
        Graphic_simulation describe the race using matplot.
        """
        self.competition.race_simulation()

        t_partial_final=[]
        for competitor in self.competition.competitors:
            t_partial_final.append(competitor.curr_time[-1] + competitor.start_position * self.gap)
        t_final=max(t_partial_final)

        self.competition.competitors=sorted(
            self.competition.competitors, key = lambda x: x.start_position
            )
        race_gra=self.competition.circuit.plot_circuit()
        t=0
        dt=1
        while t<t_final+dt+1:
            race_gra.clf()
            shooting_player=0
            race_gra=self.competition.circuit.plot_circuit()
            race_gra.axis('off')
            race_gra.ylim([-2.5*self.competition.circuit.circuit_shape[1], 2.5*self.competition.circuit.circuit_shape[1]])
            race_gra.xlim([-55, 95])


            for competitor in self.competition.competitors:
                race_gra = self.competitor_plot_position (race_gra, t, competitor)
                shooting_player=shooting_player+competitor.is_shooting
                race_gra = self.control_shooting(race_gra, shooting_player)

            race_gra= self.print_text(race_gra, shooting_player,t)
            race_gra.draw()
            race_gra.pause(0.0000001)

            t=t+dt
        race_gra.show()

    def competitor_plot_position(self, race_gra, t, competitor):
        """
        competitor_plot_position plot position at time t.
        """
        [x,y]=self.competitor_position(t, competitor)
        race_gra.plot(x,y, marker="o", markersize=20, markeredgecolor="red")
        if competitor.start_position<9:
            race_gra.text(x-1.5, y-0.8, str(competitor.start_position+1), fontsize=12)
        else:
            race_gra.text(x-3, y-0.8, str(competitor.start_position+1), fontsize=12)
        return race_gra

    def competitor_position(self, t, competitor):
        """
        competitor_position give position at time t.
        """
        competitor.is_shooting= False
        t_start= competitor.start_position * self.gap

        if t < t_start:
            return self.position_starting(competitor)
        if t > competitor.curr_time[-1]+t_start:
            competitor.is_finished=True
            return self.position_ranking(competitor)

        competitor.is_started=True
        time_interval=bisect.bisect_left(competitor.curr_time, t-t_start)

        if time_interval%2==0:
            if time_interval != 0:
                t_dot=(t-t_start-competitor.curr_time[time_interval-1])/(competitor.curr_time[time_interval]-competitor.curr_time[time_interval-1])
                if time_interval == len(competitor.curr_time) - 1 and t_dot>3/4:
                    return [
                        -self.competition.circuit.circuit_shape[0],
                        -self.competition.circuit.circuit_shape[1]*(4*t_dot-3)
                    ]         

            else:
                t_dot=(t-t_start)/(competitor.curr_time[time_interval])
                if t_dot < 1/4:
                    return [
                        self.competition.circuit.circuit_shape[0],
                        self.competition.circuit.circuit_shape[1]*(4*t_dot-1)
                    ]

            return [
                self.competition.circuit.circuit_shape[0]*ma.cos(2*ma.pi*t_dot-ma.pi/2),
                self.competition.circuit.circuit_shape[1]*ma.sin(2*ma.pi*t_dot-ma.pi/2)
                ]

        return self.shooting_simulation(t, t_start, competitor, time_interval)

    def shooting_simulation(self, t, t_start, competitor, time_interval):
        """
        function to simulate shooting
        """
        penalty_lap_time=competitor.target_error[int((time_interval-1)/2)]*competitor.v_penalty_lap[int((time_interval-1)/2)]

        if t - t_start < (competitor.curr_time[time_interval] - penalty_lap_time):
            competitor.is_shooting= True
            return[1.1*int(competitor.start_position-self.competition.competitors[-1].start_position/2), -self.competition.circuit.circuit_shape[1]]
        else:
            t_dot=(t-t_start-(competitor.curr_time[time_interval]-penalty_lap_time))/(penalty_lap_time/competitor.target_error[int((time_interval-1)/2)])
            return [
                self.competition.circuit.penalty_shape[0]*ma.cos(2*ma.pi*t_dot - ma.pi/2),
                self.competition.circuit.penalty_shape[1]*ma.sin(2*ma.pi*t_dot - ma.pi/2) - (self.competition.circuit.circuit_shape[1] - self.competition.circuit.penalty_shape[1])
            ]

    def control_shooting(self, race_gra, shooting_player):
        """
        function to control number of shooters
        """
        if shooting_player>self.competition.circuit.number_targets:
            race_gra.text(-40, 0, "Error: too many shooting players " + str(shooting_player), color="red", fontsize=25)
            return race_gra
        else:
            return race_gra

    def print_text(self,race_gra, shooting_player,t):
        """
        a function to print some texts
        """
        race_gra.text(-60, 2.5*self.competition.circuit.circuit_shape[1]-2.8, 'starting list:',color="red", fontsize=15)
        race_gra.text(-20, -1.5*self.competition.circuit.circuit_shape[1], "shooting: " + str(shooting_player), color="red", fontsize=15)
        race_gra.text(self.competition.circuit.circuit_shape[0]-10, -1.5*self.competition.circuit.circuit_shape[1], "Start", fontsize=15)
        race_gra.text(-self.competition.circuit.circuit_shape[0]-10, -1.5*self.competition.circuit.circuit_shape[1], "Finish", fontsize=15)
        race_gra.text(-60, +10, "t= " + str(t), fontsize=12)
        race_gra.text(45, 10, "Ranking:", fontsize=24)

        return race_gra

    def position_starting(self,competitor):
        """
        a function to print starting list
        """
        row = int(competitor.start_position / 8)
        return [-30+10*(competitor.start_position-row*8), 2.5*self.competition.circuit.circuit_shape[1]-2 - 4*row]

    def position_ranking (self,competitor):
        """
        a function to print starting list
        """
        partial_ranking=[p_competitor for p_competitor in self.competition.competitors if p_competitor.is_finished]
        partial_ranking=sorted(partial_ranking, key = lambda x: x.curr_time[-1])
        position = [partial_ranking.index(p_competitor) for p_competitor in partial_ranking if p_competitor.name == competitor.name]
        row = int(position[0]/4)

        return [50 + row*10, 10 - (position[0]+1)*5 + 4*5*row]
