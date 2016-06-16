# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Questionnaire(Page):
    form_model = models.Player
    form_fields = ['age', 'occupation',
                    'gender', 'daily_internet',
                    'monthly_income', 'email', 'results']
                    
class Emotions(Page):
    form_model = models.Player
    form_fields = ['positive', 'emotions', 'negative', 'express', 'stress',
                    'control', 'positive_situation', 'negative_situation', 'negative_express', 'negative_situation']

class Thanks(Page):
    pass

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


page_sequence = [
    Emotions,
    Questionnaire,
    Thanks
]
