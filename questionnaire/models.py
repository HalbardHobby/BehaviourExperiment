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

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    
    age = models.PositiveIntegerField(verbose_name='Age')
    
    occupation = models.CharField(verbose_name='Occupation')
    
    gender = models.CharField(choices=['Male','Female'],
                                verbose_name='Gender',
                                widget=widgets.RadioSelectHorizontal())
    
    daily_internet = models.PositiveIntegerField(verbose_name='Average daily hours of internet use')
    
    monthly_income = models.CurrencyField(choices=[c(x*500) for x in range(1,10)],
                                            verbose_name='Monthly income',
                                            widget=widgets.RealWorldCurrencyInput())
                                            
    email = models.EmailField(verbose_name='Email')
    
    results = models.CharField(choices=['Yes', 'No'],
                                verbose_name='Would you like to recieve further information?',
                                widget=widgets.RadioSelectHorizontal())