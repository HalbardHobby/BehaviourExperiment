# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Instructions(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

class Lottery(Page):
    form_model = models.Player
    form_fields = ['lottery']
    
    def is_displayed(self):
        return self.subsession.round_number != Constants.num_rounds
        
class Income(Page):
    def is_displayed(self):
        return self.subsession.round_number == 10 or self.subsession.round_number == Constants.num_rounds

class Mood(Page):
    form_model = models.Player
    form_fields = [ 'interested', 'distressed', 'excited', 'upset', 
                    'scared', 'hostile','enthusiastic', 'irritable', 
                    'alert', 'inspired', 'nervous', 'attentive']
                    
    def is_displayed(self):
        return self.subsession.round_number == 1 or self.subsession.round_number == 11 or self.subsession.round_number == Constants.num_rounds

    def before_next_page(self):
        if self.subsession.round_number == Constants.num_rounds:
            self.player.set_payoff()


page_sequence = [
    Instructions,
    Mood,
    Lottery,
    Income
]
