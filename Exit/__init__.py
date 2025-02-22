from otree.api import *
import random


class C(BaseConstants):
    NAME_IN_URL = 'Exit'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Max_bonus = 2 
    Base_payment = 3.4 
    Bonus = 'Placeholder' #TODO: adjust
    
    # Prolific links:
    Completion_redirect = "https://app.prolific.com/submissions/complete?cc=CCNA4C97" 
    Reject_redirect = "https://app.prolific.com/submissions/complete?cc=CSTFIICD" 
    
    
    
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
    age = models.IntegerField(label="Age", min=18, max=100, blank=False) 
    gender = models.StringField(label='Gender at birth',
                                choices=['Male', 'Female', 'Other/Prefer not to say'], widget=widgets.RadioSelect,)
    education = models.StringField(label = 'Education level',
                                   choices=['Haven’t graduated high school','GED','High school graduate','Bachelors','Masters','Professional degree (JD, MD, MBA)','Doctorate', 'Other'], widget=widgets.RadioSelect, )
    # education = models.StringField(label = 'Education level',
    #                                choices=['High school or lower','Bachelors degree','Masters degree','PhD','Other'], widget=widgets.RadioSelect) 
    
    employment = models.StringField(label='Employment status',
                                    choices=['Employed full-time', 'Employed part-time', 'Self-employed', 'Out of work, or seeking work',
                                             'Student', 'Out of labor force (e.g. retired or parent raising one or more children)', 'Other'], widget=widgets.RadioSelect, )
    
    income = models.StringField(label='Approximately, what was your <strong>total household income</strong> in the last year, before taxes?',
                            choices=['$0-$10.000', '$10.000-$20.000','$20.000-$30.000','$30.000-$40.000','$40.000-$50.000','$50.000-$60.000',
                                     '$50.000-$75.000', '$75.000-$100.000', '$100.000-$150.000', '$150.000-$200.000', '$200.000+', 'Prefer not to answer',
                                     ], widget=widgets.RadioSelect,
                            blank=False) 

   # Politics
    Politics_social = models.StringField(label='How liberal (left-wing) or conservative (right-wing) are you on <strong>SOCIAL</strong> issues?',
                                        choices=['Very Liberal', 'Liberal', 'Slightly Liberal', 'Moderate/middle-of-the-road', 
                                        'Slightly Conservative', 'Conservative', 'Very Conservative', 
                                        "Don't know/not political", 'Libertarian', 'Other'
                                        ], widget=widgets.RadioSelect,
                            blank=False) 
    Politics_economic = models.StringField(label='How liberal (left-wing) or conservative (right-wing) are you on <strong>ECONOMIC</strong> issues?',
                                          choices=['Very Liberal', 'Liberal', 'Slightly Liberal', 'Moderate/middle-of-the-road', 
                                        'Slightly Conservative', 'Conservative', 'Very Conservative', 
                                        "Don't know/not political", 'Libertarian', 'Other'
                                        ], widget=widgets.RadioSelect,
                            blank=False)

    Politics_inequality = models.StringField(label='To what extent do you agree that <strong>income inequality</strong> is an important social issue?',
                                          choices=['Strongly agree','Somewhat agree', 'Moderately agree', 'Neutral', 'Moderately disagree','Somewhat agree', "Strongly disagree"
                                        ], widget=widgets.RadioSelect,
                            blank=False) 
    
    Politics_redistribution = models.StringField(label='To what extent do you agree that <strong>there should be more redistribution?</strong>',
                                          choices=["Don't know what 'redistribution' means", 'Strongly agree','Somewhat agree', 'Moderately agree', 'Neutral', 'Moderately disagree','Somewhat agree', "Strongly disagree", 
                                        ], widget=widgets.RadioSelect,
                            blank=False) 
    
    # Religion
    Religion_category = models.StringField(label='What is your religion?',
                                          choices=['Atheist/Agnostic', 'Christian', 'Jewish', 'Muslim', 'Other'
                                        ], widget=widgets.RadioSelect,
                            blank=False) 
    Religion_intensity = models.StringField(label='How religious are you?',
                                          choices=['Very religious', 'Somewhat religious', 'Slightly religious', 'Not religious at all', "Don't want to answer"
                                        ], widget=widgets.RadioSelect,
                            blank=False)
    
    # Attention checks
    Attention_3 =  models.BooleanField(choices=[
            [False, 'USA'],
            [False, 'Canada'],
            [False, 'Mexico'],
            [False, 'Austria'],
            [False, 'Germany'],
            [False, 'Switzerland'],
            [False, 'Russia'], 
            [True, 'India'], ],
        label='Choose the country that was described in the instructions.',
        widget=widgets.RadioSelect,)
        
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'employment', 'income']
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True

class Political_leaning(Page):
    form_model = 'player'
    form_fields = ['Politics_social', 'Politics_economic',]
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
class Political_leaning_2(Page):
    form_model = 'player'
    form_fields = ['Politics_inequality', 'Politics_redistribution']
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
class Religiosity(Page):
    form_model = 'player'
    form_fields = ['Religion_category', 'Religion_intensity']
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
class Attention_check_3(Page):
    form_model = 'player'
    form_fields = ['Attention_3']
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        return {'Instructions': C.Instructions_path}
    
    #save at  the participant level
    @staticmethod   
    def before_next_page(player: Player, timeout_happened=False):
        player.participant.vars['Attention_3'] = player.Attention_3
        count = 0
        for x in ['Attention_1', 'Attention_2']:
            if player.participant.vars[x] == False:
                count += 1
        if player.Attention_3 == False:
            count += 1
        if count > 1:
            player.participant.Allowed = False
            player.participant.Attention_passed = False

page_sequence = [ Political_leaning,Political_leaning_2, Religiosity, Demographics, Attention_check_3]