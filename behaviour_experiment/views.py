# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Lottery(Page):
    form_model = models.Player
    form_fields = ['lottery']
    
    def is_displayed(self):
        return self.subsession.round_number != Constants.num_rounds

class ResultsWaitPage(WaitPage):
    
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds -1

    def after_all_players_arrive(self):
        self.subsession.set_payment()

    body_text = "Calculating income"


class Mood(Page):
    form_model = models.Player
    form_fields = [ 'interested', 'distressed', 'excited', 'upset', 
                    'strong', 'guilty', 'scared', 'hostile',
                    'enthusiastic', 'proud', 'irritable', 'alert',
                    'ashamed', 'inspired', 'nervous', 'determined',
                    'attentive', 'jittery', 'active', 'afraid']
                    
    def is_displayed(self):
        return self.subsession.round_number == 1 or self.subsession.round_number == 11 or self.subsession.round_number == Constants.num_rounds


page_sequence = [
    Mood,
    Lottery,
    ResultsWaitPage
]
