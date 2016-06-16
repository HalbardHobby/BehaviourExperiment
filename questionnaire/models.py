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
    
    monthly_income = models.CurrencyField(verbose_name='Monthly income',
                                            widget=widgets.RealWorldCurrencyInput())
                                            
    email = models.EmailField(verbose_name='Email')
    
    results = models.CharField(choices=['Yes', 'No'],
                                verbose_name='Would you like to recieve further information?',
                                widget=widgets.RadioSelectHorizontal())
                                
    """Metrics"""
    
    positive = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7],
                                            verbose_name='When I want to feel a positive emotion, I change what I\'m thinking about.',
                                            widget=widgets.RadioSelectHorizontal())
                                            
    emotions = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7],
                                            verbose_name='I keep emotions to myself.',
                                            widget=widgets.RadioSelectHorizontal())
    
    negative = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7],
                                            verbose_name='When I want to feel a less negative emotion, I change what I\'m thinking about.',
                                            widget=widgets.RadioSelectHorizontal())
                                            
    express = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7],
                                            verbose_name='When I\'m feeling a positive emotion, I\'m careful not to express them.',
                                            widget=widgets.RadioSelectHorizontal())
    
    stress = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7],
                                            verbose_name='When I\'m faced with an stressful situation, I think about it in a way that makes me feel calm.',
                                            widget=widgets.RadioSelectHorizontal())
                                            
    control = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7],
                                            verbose_name='I control my emotions by not expressing them.',
                                            widget=widgets.RadioSelectHorizontal())
    
    positive_situation = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7],
                                            verbose_name='When I want to feel a positive emotion, I change the way I\'m thinking about the situation.',
                                            widget=widgets.RadioSelectHorizontal())
                                            
    control_situation = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7],
                                            verbose_name='I control my emotions by thinking about the situation I\m in.',
                                            widget=widgets.RadioSelectHorizontal())
                                            
    negative_express = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7],
                                            verbose_name='When I\'m feeling a negative emotion, I\'m careful not to express them.',
                                            widget=widgets.RadioSelectHorizontal())
                                            
    negative_situation = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7],
                                            verbose_name='When I want to feel a less negative emotion, I change the way I\'m thinking about the situation.',
                                            widget=widgets.RadioSelectHorizontal())
    
    