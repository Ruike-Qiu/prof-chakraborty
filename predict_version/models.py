
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'predict_version'
    players_per_group = None
    num_rounds = 10
    scale = 10000
    location = 11000
    PayoffData = '[[[[1,2],[3,4]],[[5,6],[7,8`]]],[[[1.2,3],[4.6,1]],[[2,6],[7,8]]],[[[4,6],[2,6]],[[5.5,6],[1,2]]],[[[5.2,1],[1.1,4]],[[7.7,1],[8.8,9]]]]'
    Shaded = '[2,3],[1,4],[1,3],[3,4]'
    results_data = '1,1,1,2,2,2,3,3,3,4'
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    Guess = models.FloatField(initial=0.5, max=1, min=0)
    GuessField = models.IntegerField()