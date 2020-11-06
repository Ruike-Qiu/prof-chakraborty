
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'collect_version'
    players_per_group = 2
    num_rounds = 1
    scale = 10000
    location = 11000
    GameData = ()
    OutcomeData = ()
    FlippedData = (0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0)
    TaskIdentifier = ()
    EventData = ()
    PayoffData = '[[[[1,1],[0,3]],[[3,0],[1,1]]]]'
    Shaded = '[1],[2],[3],[4]'
    betray_payoff = c(300)
    betrayed_payoff = c(0)
    both_cooperate_payoff = c(200)
    both_defect_payoff = c(100)
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    def cal_results(self):
        for p in self.get_players():
            p.cal_result()
class Player(BasePlayer):
    decision = models.StringField(choices=[['A', 'A'], ['B', 'B']], widget=widgets.RadioSelect)
    result = models.StringField()
    def other_player(self):
        return self.get_others_in_group()[0]
    def cal_result(self):
        shade_matrix = dict(
            A=dict(
                A="1",
                B="2",
            ),
            B=dict(
                A="3", B="4"
            ),
        )
        if self.id_in_group == 1:
            self.result = shade_matrix[self.decision][self.other_player().decision]
        else:
            self.result = shade_matrix[self.other_player().decision][self.decision]