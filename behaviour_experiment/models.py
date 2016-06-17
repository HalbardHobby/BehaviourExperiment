# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random
import datetime

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Alejandro Espinosa'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'behaviour_experiment'
    players_per_group = None
    num_rounds = 31
    
    lotteries = [[{'id': 1, 'Lottery A':(1, 4.75, 3.66), 'Lottery B':(1, 8.8, 0.23)},
                {'id': 2, 'Lottery A':(2, 5.80, 4.00), 'Lottery B':(2, 9.63, 0.25)},
                {'id': 3, 'Lottery A':(3, 5.12, 4.10), 'Lottery B':(3, 9.86, 0.26)},
                {'id': 4, 'Lottery A':(4, 4.09, 3.27), 'Lottery B':(4, 7.86, 0.2)},
                {'id': 5, 'Lottery A':(5, 5.55, 4.44), 'Lottery B':(5, 10.68, 0.28)},
                {'id': 6, 'Lottery A':(6, 4.94, 3.95), 'Lottery B':(6, 9.51, 0.25)},
                {'id': 7, 'Lottery A':(7, 5.98, 4.78), 'Lottery B':(7, 11.5, 0.3)},
                {'id': 8, 'Lottery A':(8, 4.33, 3.46), 'Lottery B':(8, 8.33, 0.22)},
                {'id': 9, 'Lottery A':(9, 4.76, 3.80), 'Lottery B':(9, 9.16, 0.24)},
                {'id': 10, 'Lottery A':(10, 4.15, 3.32), 'Lottery B':(10, 7.98, 0.21)}],
                
                [{'id': 1, 'Lottery A':(1, 3.66, 2.93), 'Lottery B':(1, 7.04, 0.18)},
                {'id': 2, 'Lottery A':(2, 3.84, 3.07), 'Lottery B':(2, 7.39, 0.19)},
                {'id': 3, 'Lottery A':(3, 5.49, 4.39), 'Lottery B':(3, 10.56, 0.27)},
                {'id': 4, 'Lottery A':(4, 4.70, 3.76), 'Lottery B':(4, 9.04, 0.23)},
                {'id': 5, 'Lottery A':(5, 4.45, 3.56), 'Lottery B':(5, 8.57, 0.22)},
                {'id': 6, 'Lottery A':(6, 4.88, 3.90), 'Lottery B':(6, 9.39, 0.24)},
                {'id': 7, 'Lottery A':(7, 3.90, 3.12), 'Lottery B':(7, 7.51, 0.20)},
                {'id': 8, 'Lottery A':(8, 4.39, 3.51), 'Lottery B':(8, 8.45, 0.22)},
                {'id': 9, 'Lottery A':(9, 5.91, 4.73), 'Lottery B':(9, 11.39, 0.30)},
                {'id': 10, 'Lottery A':(10, 5.73, 4.59), 'Lottery B':(10, 11.03, 0.29)}],
                
                [{'id': 1, 'Lottery A':(1, 3.78, 3.02), 'Lottery B':(1, 7.28, 0.19)},
                {'id': 2, 'Lottery A':(2, 5.67, 4.54), 'Lottery B':(2, 10.92, 0.28)},
                {'id': 3, 'Lottery A':(3, 4.63, 3.71), 'Lottery B':(3, 8.92, 0.23)},
                {'id': 4, 'Lottery A':(4, 3.72, 2.98), 'Lottery B':(4, 7.16, 0.19)},
                {'id': 5, 'Lottery A':(5, 3.96, 3.17), 'Lottery B':(5, 7.63, 0.20)},
                {'id': 6, 'Lottery A':(6, 4.21, 3.37), 'Lottery B':(6, 8.10, 0.21)},
                {'id': 7, 'Lottery A':(7, 5.37, 4.29), 'Lottery B':(7, 10.33, 0.27)},
                {'id': 8, 'Lottery A':(8, 5.24, 4.20), 'Lottery B':(8, 10.09, 0.26)},
                {'id': 9, 'Lottery A':(9, 6.04, 4.83), 'Lottery B':(9, 11.62, 0.30)},
                {'id': 10, 'Lottery A':(10, 6.1, 4.88), 'Lottery B':(10, 11.74, 0.30)}],
                
                [{'id': 1, 'Lottery A':(1, 5.18, 4.15), 'Lottery B':(1, 9.98, 0.26)},
                {'id': 2, 'Lottery A':(2, 5.06, 4.05), 'Lottery B':(2, 9.74, 0.25)},
                {'id': 3, 'Lottery A':(3, 5.79, 4.63), 'Lottery B':(3, 11.15, 0.29)},
                {'id': 4, 'Lottery A':(4, 5.61, 4.49), 'Lottery B':(4, 10.80, 0.28)},
                {'id': 5, 'Lottery A':(5, 4.82, 3.85), 'Lottery B':(5, 9.27, 0.24)},
                {'id': 6, 'Lottery A':(6, 4.27, 3.41), 'Lottery B':(6, 8.22, 0.21)},
                {'id': 7, 'Lottery A':(7, 5.30, 4.24), 'Lottery B':(7, 10.21, 0.27)},
                {'id': 8, 'Lottery A':(8, 4.51, 3.61), 'Lottery B':(8, 8.69, 0.23)},
                {'id': 9, 'Lottery A':(9, 4.02, 3.22), 'Lottery B':(9, 8.75, 0.20)},
                {'id': 10, 'Lottery A':(10, 5.43, 4.34), 'Lottery B':(10, 10.45, 0.27)}]]
                

class Subsession(BaseSubsession):
    
    def before_session_starts(self):
        
        players = self.get_players()
        
        for player in players:
            if self.round_number == 1:
                player.payoff = random.choice([c(5),c(10),c(15)])
            elif self.round_number == 11:
                player.payoff = c(10)
            elif self.round_number == Constants.num_rounds:
                player.payoff = None
            else:
                player.payoff = player.in_round(self.round_number -1).payoff
            
            if self.round_number == Constants.num_rounds:
                for x in range(3):
                    current_set = Constants.lotteries[x]
                    random.shuffle(current_set)
                    player_history = player.in_all_rounds()
                    
                    for y in range(10):
                        current_lottery = current_set[y-1]
                        
                        player_history[(x*10)+y].lottery_a_prob = current_lottery['Lottery A'][0]
                        player_history[(x*10)+y].lottery_a1 = c(current_lottery['Lottery A'][1])
                        player_history[(x*10)+y].lottery_a2 = c(current_lottery['Lottery A'][2])
                        
                        player_history[(x*10)+y].lottery_b_prob = current_lottery['Lottery B'][0]
                        player_history[(x*10)+y].lottery_b1 = c(current_lottery['Lottery B'][1])
                        player_history[(x*10)+y].lottery_b2 = c(current_lottery['Lottery B'][2])


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        history = self.in_all_rounds()
        lottery_history = self.in_all_rounds()
        
        selected_round = random.randint(1, Constants.num_rounds-1)
        if history[selected_round].lottery == 'Lottery A':
            lottery_1 = history[selected_round].lottery_a1
            lottery_2 = history[selected_round].lottery_a1
            lottery_p = history[selected_round].lottery_a_prob
        elif history[selected_round].lottery == 'Lottery B':
            lottery_1 = history[selected_round].lottery_b1
            lottery_2 = history[selected_round].lottery_b1
            lottery_p = history[selected_round].lottery_b_prob
            
        result = random.randint(1,10)
        self.payoff = c(10)
        self.payoff += c(lottery_1) if result <= lottery_p else c(lottery_2)
        
    lottery = models.CharField(choices=['Lottery A', 'Lottery B'],
                                doc="""Lottery A or B""",
                                verbose_name='Choose which lottery you prefer',
                                widget=widgets.RadioSelectHorizontal())
    
    lottery_a1 = models.CurrencyField()
    lottery_a2 = models.CurrencyField()
    
    lottery_a_prob = models.IntegerField()
    
    lottery_b1 = models.CurrencyField()
    lottery_b2 = models.CurrencyField()
                                
    lottery_b_prob = models.IntegerField()
    
    """preguntas de control"""
    
    
    interested = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Interested',
                                             widget=widgets.RadioSelectHorizontal())
    
    distressed = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Distressed',
                                             widget=widgets.RadioSelectHorizontal())
    
    excited = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Excited',
                                             widget=widgets.RadioSelectHorizontal())
    
    upset = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Upset',
                                             widget=widgets.RadioSelectHorizontal())
    
    scared = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Scared',
                                             widget=widgets.RadioSelectHorizontal())
    
    hostile = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Hostile',
                                             widget=widgets.RadioSelectHorizontal())
    
    enthusiastic = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Enthusiastic',
                                             widget=widgets.RadioSelectHorizontal())
    
    irritable = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Irritable',
                                             widget=widgets.RadioSelectHorizontal())
    
    alert = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Alert',
                                             widget=widgets.RadioSelectHorizontal())
    
    inspired = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Inspired',
                                             widget=widgets.RadioSelectHorizontal())
                                             
    nervous = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Nervous',
                                             widget=widgets.RadioSelectHorizontal())
                                             
    attentive = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Attentive',
                                             widget=widgets.RadioSelectHorizontal())
                                             