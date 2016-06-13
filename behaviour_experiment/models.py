# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

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
                
    current_set = lotteries[0]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        self.payoff = 0
                                
    lottery = models.CharField(choices=['Lottery A', 'Lottery B'],
                                doc="""Lottery A or B""",
                                widget=widgets.RadioSelectHorizontal())
    
    lottery_id = models.PositiveIntegerField()
                                
    time_init = models.DateTimeField()
    
    """preguntas de control"""
    
    
    interested = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
    
    distressed = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
    
    excited = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
    
    upset = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
    
    strong = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
    
    guilty = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
    
    scared = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
    
    hostile = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
    
    enthusiastic = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
    
    proud = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
    
    irritable = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
    
    alert = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
    
    ashamed = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
    
    inspired = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
                                             
    nervous = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
                                             
    determined = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
                                             
    attentive = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
                                             
    jittery = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
                                             
    active = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
    
    afraid = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                             doc="""preguntas de control""",
                                             widget=widgets.RadioSelectHorizontal())
    