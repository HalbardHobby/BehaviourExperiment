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
    num_rounds = 40
    
    lotteries = [[{'id': 1, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 2, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 3, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 4, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 5, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 6, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 7, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 8, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 9, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 10, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)}],
                
                [{'id': 1, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 2, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 3, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 4, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 5, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 6, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 7, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 8, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 9, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 10, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)}],
                
                [{'id': 1, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 2, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 3, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 4, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 5, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 6, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 7, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 8, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 9, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 10, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)}],
                
                [{'id': 1, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 2, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 3, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 4, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 5, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 6, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 7, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 8, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 9, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)},
                {'id': 10, 'Lottery A':(1/10, 4.75, 3.66), 'Lottery B':(1/10, 8.8, 0.23)}]]
                
    for lot in lotteries:
        random.shuffle(lot)
                

class Subsession(BaseSubsession):
    
    lottery_a1 = models.FloatField()
    lottery_a2 = models.FloatField()
    
    lottery_a_prob = models.FloatField()
    
    lottery_b1 = models.FloatField()
    lottery_b2 = models.FloatField()
                                
    lottery_a_prob = models.FloatField()
    
    def before_session_starts(self):
        current_set = Constants.lotteries[self.round_number//10] if self.round_number < 40 else Constants.lotteries[3]
        current_lottery = current_set[self.round_number % 10]
        
        self.get_groups()[0].get_players()[0].lottery_id = current_lottery['id']
        
        self.lottery_a_prob = current_lottery['Lottery A'][0]
        self.lottery_a1 = current_lottery['Lottery A'][1]
        self.lottery_a2 = current_lottery['Lottery A'][2]
        
        self.lottery_b_prob = current_lottery['Lottery B'][0]
        self.lottery_b1 = current_lottery['Lottery B'][1]
        self.lottery_b2 = current_lottery['Lottery B'][2]


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        self.payoff = 0
        
    lottery = models.CharField(choices=['Lottery A', 'Lottery B'],
                                doc="""Lottery A or B""",
                                verbose_name='Choose which lottery you prefer',
                                widget=widgets.RadioSelectHorizontal())
    
    lottery_id = models.PositiveIntegerField()
    
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
    
    strong = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Strong',
                                             widget=widgets.RadioSelectHorizontal())
    
    guilty = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Guilty',
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
    
    proud = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Proud',
                                             widget=widgets.RadioSelectHorizontal())
    
    irritable = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Irritable',
                                             widget=widgets.RadioSelectHorizontal())
    
    alert = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Alert',
                                             widget=widgets.RadioSelectHorizontal())
    
    ashamed = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Ashamed',
                                             widget=widgets.RadioSelectHorizontal())
    
    inspired = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Inspired',
                                             widget=widgets.RadioSelectHorizontal())
                                             
    nervous = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Nervous',
                                             widget=widgets.RadioSelectHorizontal())
                                             
    determined = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Determined',
                                             widget=widgets.RadioSelectHorizontal())
                                             
    attentive = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Attentive',
                                             widget=widgets.RadioSelectHorizontal())
                                             
    jittery = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Jittery',
                                             widget=widgets.RadioSelectHorizontal())
                                             
    active = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Active',
                                             widget=widgets.RadioSelectHorizontal())
    
    afraid = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             verbose_name='Afraid',
                                             widget=widgets.RadioSelectHorizontal())
    