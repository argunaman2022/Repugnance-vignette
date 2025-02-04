from otree.api import *


doc = """
Your app description
"""
class C(BaseConstants):
    NAME_IN_URL = 'Results'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Max_bonus = 'PALCEHOLDER' #TODO: adjust
    Base_payment = 'PALCEHOLDER' #TODO: adjust
    
    # Prolific links, gotten from the study page on prolific
    Completion_redirect = 'https://www.wikipedia.org/' #TODO: change these
    Failure_redirect = 'https://www.wikipedia.org/'
    Return_redirect = 'https://www.wikipedia.org/'

    Instructions_path = "_templates/global/Instructions.html"
    Quit_study_text_path = "_templates/global/Quit_study_text.html"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES

class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True

    @staticmethod
    def vars_for_template(player: Player):
        return {'Instructions': C.Instructions_path}
    


class Failed_attention(Page):
    @staticmethod
    def is_displayed(player: Player):
        return not player.participant.Attention_passed  # player failed both attention checks
    @staticmethod
    def js_vars(player):
        return dict(
            completion_link = C.Failure_redirect
        )

page_sequence = [Results, Failed_attention]
