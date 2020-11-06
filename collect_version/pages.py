
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class WelcomePage(Page):
    form_model = 'player'
class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']
class GameWaitPage(WaitPage):
    after_all_players_arrive = 'cal_results'
page_sequence = [WelcomePage, Decision, GameWaitPage]