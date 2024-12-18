from otree.api import *
import random


class C(BaseConstants):
    NAME_IN_URL = 'Exit'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Max_bonus = 'PALCEHOLDER' #TODO: adjust
    Base_payment = 'PALCEHOLDER' #TODO: adjust
    
    # Prolific links:
    Completion_redirect = "https://www.wikipedia.org/" #TODO: adjust
    Reject_redirect = "https://www.wikipedia.org/" #TODO: adjust
    Return_redirect = "https://www.wikipedia.org/" #TODO: adjust
    
    
    Instructions_path = "_templates/global/Instructions.html"
    Quit_study_text_path = "_templates/global/Quit_study_text.html"
    
    # Treatment quotas
    quotas = {
    'poor_poor': 0,
    'poor_rich' : 0,
    'rich_rich' : 0,
    }
    
    # there are 4 vignettes with 2 versions each vignette_inequality and vignette_equality
    Vignette_labels = ['loan_shark', 'surrogate', 'queue_jump', 'prostitute', 'dwarf_tossing', 'waste_trade', 'coin_collector', 'apple_seller']

    
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Demographics
    age = models.IntegerField(label="Age", min=18, max=100, blank=True) #TODO: remove blank=True
    gender = models.StringField(label='Gender at birth',
                                choices=['Male', 'Female', 'Other/Prefer not to say'], widget=widgets.RadioSelect, blank=True) #TODO: remove blank=True
    education = models.StringField(label = 'Education level',
                                   choices=['Haven’t graduated high school','GED','High school graduate','Bachelors','Masters','Professional degree (JD, MD, MBA)','Doctorate'], widget=widgets.RadioSelect, blank=True) #TODO: remove blank=True
    # education = models.StringField(label = 'Education level',
    #                                choices=['High school or lower','Bachelors degree','Masters degree','PhD','Other'], widget=widgets.RadioSelect) 
    
    employment = models.StringField(label='Employment status',
                                    choices=['Employed full-time', 'Employed part-time', 'Independent, or business owner', 'Out of work, or seeking work',
                                             'Student', 'Out of labor force (e.g. retired or parent raising one or more children)'], widget=widgets.RadioSelect, blank=True) #TODO: remove blank=True
    
    income = models.StringField(label='Approximately, what was your <strong>total household income</strong> in the last year, before taxes?',
                            choices=['$0-$10.000', '$10.000-$20.000','$20.000-$30.000','$30.000-$40.000','$40.000-$50.000','$50.000-$60.000',
                                     '$50.000-$75.000', '$75.000-$100.000', '$100.000-$150.000', '$150.000-$200.000', '$200.000+', 'Prefer not to answer',
                                     ], widget=widgets.RadioSelect,
                            blank=True) #TODO: remove blank=True

   # Politics
    Politics_social = models.StringField(label='How liberal (left-wing) or conservative (right-wing) are you on <strong>SOCIAL</strong> issues?',
                                        choices=['Very Liberal', 'Liberal', 'Slightly Liberal', 'Moderate/middle-of-the-road', 
                                        'Slightly Conservative', 'Conservative', 'Very Conservative', 
                                        "Don't know/not political", 'Libertarian', 'Other'
                                        ], widget=widgets.RadioSelect,
                            blank=True) #TODO: remove blank=True
    Politics_economic = models.StringField(label='How liberal (left-wing) or conservative (right-wing) are you on <strong>ECONOMIC</strong> issues?',
                                          choices=['Very Liberal', 'Liberal', 'Slightly Liberal', 'Moderate/middle-of-the-road', 
                                        'Slightly Conservative', 'Conservative', 'Very Conservative', 
                                        "Don't know/not political", 'Libertarian', 'Other'
                                        ], widget=widgets.RadioSelect,
                            blank=True) #TODO: remove blank=True

    Politics_inequality = models.StringField(label='To what extend do you agree that income inequality is an important social issue?',
                                          choices=['Strongly agree','Somewhat agree', 'Moderately agree', 'Neutral', 'Moderately disagree','Somewhat agree', "Strongly disagree"
                                        ], widget=widgets.RadioSelect,
                            blank=True) #TODO: remove blank=True
    # Religion
    Religion_category = models.StringField(label='What is your religion?',
                                          choices=['Atheist/Agnostic', 'Christian', 'Jewish', 'Muslim', 'Other'
                                        ], widget=widgets.RadioSelect,
                            blank=True) #TODO: remove blank=True
    Religion_intensity = models.StringField(label='How religious are you?',
                                          choices=['Very religious', 'Somewhat religious', 'Slightly religious', 'Not religious at all', "Don't want to answer"
                                        ], widget=widgets.RadioSelect,
                            blank=True) #TODO: remove blank=True
    
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'employment', 'income']
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True

class Political_leaning(Page):
    form_model = 'player'
    form_fields = ['Politics_social', 'Politics_economic', 'Politics_inequality']
class Religiosity(Page):
    form_model = 'player'
    form_fields = ['Religion_category', 'Religion_intensity']
    
class Attention_check_1(Page):
    form_model = 'player'
    form_fields = ['Attention_1']
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        return {'Instructions': C.Instructions_path}
    
    #save at  the participant level
    @staticmethod   
    def before_next_page(player: Player, timeout_happened=False):
        player.participant.vars['Attention_1'] = player.Attention_1

page_sequence = [ Political_leaning, Religiosity, Demographics, Attention_check_1]