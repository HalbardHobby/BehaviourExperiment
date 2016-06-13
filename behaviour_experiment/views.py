# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

class Lottery(Page):
    form_model = models.Player
    form_fields = ['lottery']

class Mood(Page):
    form_model = models.Player
    form_fields = [ 'interested', 'distressed', 'excited', 'upset', 
                    'strong', 'guilty', 'scared', 'hostile',
                    'enthusiastic', 'proud', 'irritable', 'alert',
                    'ashamed', 'inspired', 'nervous', 'determined',
                    'attentive', 'jittery', 'active', 'afraid']

page_sequence = [
    Lottery,
    Mood
]
