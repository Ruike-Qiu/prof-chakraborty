
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class WelcomePage(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.round_number == 1
class DecisionPage(Page):
    form_model = 'player'
    form_fields = ['Guess']
    def vars_for_template(self):
        str_mat = Constants.PayoffData
        str_mat = str_mat[1:-1]
        mats = []
        rows = []
        depth = 0
        row = []
        start = 0
        for index, chars in enumerate(str_mat):
            if chars == "[":
                depth += 1
            if chars == "[" and (str_mat[index + 1].isdigit() or str_mat[index + 1] == "-" or str_mat[index + 1] == "+"):
                start = index
            if chars == "]":
                depth -= 1
                if depth == 2:
                    cell = str_mat[start:index+1]
                    row.append(cell[1:-1])
                    start = 0
                elif depth == 1:
                    rows.append(row)
                    row = []
                elif depth == 0:
                    mats.append(rows)
                    rows = []
                    
        return dict(mat = mats[0])
    def js_vars(self):
        shaded_list = []
        """
        row = []
        depth = 0
        start = 0
        for index, chars in enumerate(shaded_Index):
            if chars == "[":
                depth += 1
            if chars == "[" and shaded_Index[index + 1].isdigit():
                start = index + 1
            if chars == "]":
                depth -= 1
                if depth == 0:
                    subindex = shaded_Index[start:index]
                    tmp = subindex.split(",")
                    for nums in tmp:
                        row.append(int(nums))
                    shaded_list.append(row)
                    row = []
        """
        import random
        shade_num = random.randrange(1,5)
        self.player.GuessField = shade_num
        shaded_list = []
        shaded_list.append(shade_num)
        return dict(shaded = shaded_list,
                   scale = Constants.scale,
                   location = Constants.location,)
class ResultPage(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.round_number == 10
    def js_vars(self):
        #split the data that collected from game by comma
        compared_data = Constants.results_data.split(",")
        #randomly chose a round out of 10
        import random
        round_num = random.randint(1,10)
        #compare the event that happened with the one to predict
        compared_res = compared_data[round_num - 1]
        guess_res = str(self.player.in_round(round_num).GuessField)
        guess = self.player.in_round(round_num).Guess
        #if it's the same, then use the value of y to pay
        if guess_res == compared_res:
            points = Constants.scale * (1 - ((1 - guess)**2)) + Constants.location
        #otherwise, use the value of x to pay
        else:
            points = Constants.scale * (1 - (guess**2))
        return dict(r_num = round_num,
                   happen_res = compared_res,
                   gus_res = guess_res,
                   prob = guess,
                   pay = int(points))
page_sequence = [WelcomePage, DecisionPage, ResultPage]