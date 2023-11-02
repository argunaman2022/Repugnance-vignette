from otree.api import *


doc = '''
Third app - Exit survey.
'''

class C(BaseConstants):
    NAME_IN_URL = 'Exit_Survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Instructions_path = "_templates/global/Instructions.html"

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Exit survey
    Exit_1 = models.StringField(initial='')
    Exit_2 = models.StringField(initial='')
    Exit_3 = models.StringField(initial='')
    
    #Pilot questions
    Pilot_1 = models.StringField(initial='')
    Pilot_2 = models.StringField(initial='')
    Pilot_3 = models.StringField(initial='')
    Pilot_4 = models.StringField(initial='')
    Pilot_5 = models.StringField(initial='')
    Pilot_6 = models.StringField(initial='')

class Exit_survey(Page):
    form_model = 'player'
    form_fields = ['Exit_1','Exit_2','Exit_3']
      
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True

    @staticmethod
    def vars_for_template(player: Player):
        return {'Instructions': C.Instructions_path}
    
# Only for pilot
class Pilot(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    form_model = 'player'
    form_fields = ['Pilot_1','Pilot_2','Pilot_3','Pilot_4','Pilot_5','Pilot_6']
    
    @staticmethod
    def vars_for_template(player: Player):
        return {'Instructions': C.Instructions_path}
        
page_sequence = [Exit_survey, Pilot]
