from otree.api import *


doc = """
Your app description
"""
class C(BaseConstants):
    NAME_IN_URL = 'Results'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
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
    

class Failed_screening(Page):
    'This page is displayed if the player failed the comprehension checks'
    @staticmethod
    def is_displayed(player: Player):
        # You can set another failure condition here and message below
        return not player.participant.Comprehension_passed 
    
    @staticmethod
    def vars_for_template(player: Player):
        failure_message = 'Unfortunately you did not successfuly pass the comprehension check.'
        return {'failure_message': failure_message}
    
    @staticmethod
    def js_vars(player):
        return dict(
            completion_link = C.Return_redirect
        )

class Failed_attention(Page):
    @staticmethod
    def is_displayed(player: Player):
        return not player.participant.Attention_passed  # player failed both attention checks
    @staticmethod
    def js_vars(player):
        return dict(
            completion_link = C.Failure_redirect
        )

page_sequence = [Results, Failed_screening, Failed_attention]
