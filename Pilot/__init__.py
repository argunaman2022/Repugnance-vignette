from otree.api import *


doc = '''
Third app - Exit survey.
'''

class C(BaseConstants):
    NAME_IN_URL = 'Pilot'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Instructions_path = "_templates/global/Instructions.html"



class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    Pilot_1 = models.StringField(label='Was the study interesting or boring?',
                                        choices=["It was very boring", 'It was boring','Neither boring nor interesting',
                                                 'It was interesting', 'It was very interesting'], widget=widgets.RadioSelect,)
    Pilot_2 = models.StringField(label='Was the study too long?',
                                        choices=["It was too long", 'It was somewhat too long','It was not too long at all',], widget=widgets.RadioSelect,)
                                    
    Pilot_3 = models.StringField(label='Was it clear what you were asked to do?',
                                        choices=["It was not clear what I was supposed to do",
                                                 "It was somewhat clear what I was supposed to do",], widget=widgets.RadioSelect,)
    Pilot_4 = models.LongStringField(label="If there were things that confused you or were unclear, please write them below.", blank=True)
    Pilot_5 = models.LongStringField(label="Any other comments, remarks to help us improve the study's design?",blank=True)

                                    
    


#%% Base Pages
class MyBasePage(Page):
    'MyBasePage contains the functions that are common to all pages'
    form_model = 'player'
    form_fields = []
    
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed 
    
    @staticmethod
    def vars_for_template(player: Player):
        return {'hidden_fields': ['bullshit'], #hide the browser field from the participant, see the page to see how this works. #user_clicked_out
                'Instructions': C.Instructions_path} 

#%% Pages
class MyBasePage(MyBasePage):
    'MyBasePage contains the functions that are common to all pages'
    extra_fields = []
    form_fields = MyBasePage.form_fields + extra_fields

    
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed 
    
    @staticmethod
    def vars_for_template(player: Player):
        return {'hidden_fields': ['bullshit'], #hide the browser field from the participant, see the page to see how this works. #user_clicked_out
                'Instructions': C.Instructions_path} 


    
# Only for pilot
class Pilot(MyBasePage):
    extra_fields = ['Pilot_1','Pilot_2','Pilot_3','Pilot_4','Pilot_5']
    form_fields = MyBasePage.form_fields + extra_fields
    
        
page_sequence = [ Pilot]
