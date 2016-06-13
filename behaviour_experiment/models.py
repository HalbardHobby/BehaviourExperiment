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

from django_countries.fields import CountryField

author = 'Alejandro Espinosa'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'behaviour_experiment'
    players_per_group = None
    num_rounds = 4


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        self.payoff = 0
                                
    lottery_0 = models.CharField(choices=['Lottery A', 'Lottery B'],
                                doc="""Lottery A or B""",
                                widget=widgets.RadioSelect())
                                
    time_0 = models.DateTimeField()
                                
    lottery_1 = models.CharField(choices=['Lottery A', 'Lottery B'],
                                doc="""Lottery A or B""",
                                widget=widgets.RadioSelect())
    
    time_1 = models.DateTimeField()
                                
    lottery_2 = models.CharField(choices=['Lottery A', 'Lottery B'],
                                doc="""Lottery A or B""",
                                widget=widgets.RadioSelect())

    time_2 = models.DateTimeField()

    lottery_3 = models.CharField(choices=['Lottery A', 'Lottery B'],
                                doc="""Lottery A or B""",
                                widget=widgets.RadioSelect())
    
    time_3 = models.DateTimeField()
                                
    lottery_4 = models.CharField(choices=['Lottery A', 'Lottery B'],
                                doc="""Lottery A or B""",
                                widget=widgets.RadioSelect())
    
    time_4 = models.DateTimeField()
    
    lottery_5 = models.CharField(choices=['Lottery A', 'Lottery B'],
                                doc="""Lottery A or B""",
                                widget=widgets.RadioSelect())
    
    time_5 = models.DateTimeField()
    
    lottery_6 = models.CharField(choices=['Lottery A', 'Lottery B'],
                                doc="""Lottery A or B""",
                                widget=widgets.RadioSelect())
    
    time_6 = models.DateTimeField()
                                
    lottery_7 = models.CharField(choices=['Lottery A', 'Lottery B'],
                                doc="""Lottery A or B""",
                                widget=widgets.RadioSelect())
    
    time_7 = models.DateTimeField()
    
    lottery_8 = models.CharField(choices=['Lottery A', 'Lottery B'],
                                doc="""Lottery A or B""",
                                widget=widgets.RadioSelect())
    
    time_8 = models.DateTimeField()
    
    lottery_9 = models.CharField(choices=['Lottery A', 'Lottery B'],
                                doc="""Lottery A or B""",
                                widget=widgets.RadioSelect())

    time_9 = models.DateTimeField()