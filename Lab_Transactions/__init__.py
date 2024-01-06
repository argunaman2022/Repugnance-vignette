#TODO: delete all print statements
from otree.api import *
import random
import pandas as pd


class C(BaseConstants):
    NAME_IN_URL = 'BeliefsOfOthers'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Instructions_path = "_templates/global/Instructions.html"
    Instructions_LAB_path = "_templates/global/Instructions.html" #TODO: create
    Quit_study_text_path = "_templates/global/Quit_study_text.html"
    
    # Lab transaction texts
    Bug_eating = '''
    Person A eats bugs...
    '''
    
    
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass



class Player(BasePlayer):   
    Bug_eating = models.IntegerField() #1 yes/ban 0 no/dont ban
    
    
class Introduction_LAB(Page):            
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(self):
        return {'Instructions': C.Instructions_LAB_path}
    

class Page1(Page):
    form_model = 'player'
    form_fields = ['Bug_eating']
        
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    