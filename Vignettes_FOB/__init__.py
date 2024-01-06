from otree.api import *
import random

doc = '''
This is the main survey app. It contains
1. Main survey 
2. One attention check.
- You can additionally calculate payoffs and save them at a participant field.
'''

#TODO: add an exit button for players to be able to quit and return the prolific assignment (add this to template as well)
#TODO : only 4 vignettes for each person ?
#TODO: remove the fairness to person B.
#TODO: change the wording of the dimensions.
class C(BaseConstants):
    NAME_IN_URL = 'Scenarios'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Instructions_path = "_templates/global/Instructions.html"
    Quit_study_text_path = "_templates/global/Quit_study_text.html"
    Return_redirect = "https://www.wikipedia.org/" #TODO: adjust

    
    # vignette texts
    #TODO: in these texts how important is it to explicity state "household of 3 people" once you've given whom they live with.
    Child_inequality = '''
    Person A is a 13 year old girl. She lives together with her parents in a household of 3 people. Their household's annual income is <strong>31k USD</strong>.
    Person B is a 50 year old woman. She lives together with her husband and mother in a household of 3 people.
    Their annual income is <strong>75k USD</strong>. Person A will work for 5 hours every Saturday cleaning person B's 2 story-house2 story-house for an hourly wage of 15 USD/hour.'''
    Child_equality = '''
    Person A is a 13 year old girl. She lives together with her parents in a household of 3 people. Their household's annual income is <strong>31k USD</strong>.
    Person B is a 50 year old woman. She lives together with her husband and mother in a household of 3 people.
    Their annual income is <strong>31k USD</strong>. Person A will work for 5 hours every Saturday cleaning person B's 2 story-house2 story-house for an hourly wage of 15 USD/hour.'''
    
    Kidney_inequality = '''
    Person A is a 40 year old man. He lives together with his wife and one kid in a household of 3 people.
    Their household's annual income is <strong>31k USD</strong>.  Person B is a 40 year old man.
    He lives together with her wife and one kid in a household of 3 people. Their annual income is <strong>75k USD</strong>.
    Due to a final-stage kidney disease, person A is in desperate need of a replacement kidney.
    Person A will sell one of his kidneys to person B at the prevailing market price.'''
    Kidney_equality = '''
    Person A is a 40 year old man. He lives together with his wife and one kid in a household of 3 people.
    Their household's annual income is <strong>31k USD</strong>.  Person B is a 40 year old man.
    He lives together with her wife and one kid in a household of 3 people. Their annual income is <strong>31k USD</strong>.
    Due to a final-stage kidney disease, person A is in desperate need of a replacement kidney.
    Person A will sell one of his kidneys to person B at the prevailing market price.'''
    
    Waste_inequality = '''
    Country A is a medium-sized nation with an average annual wage of <strong>31k USD</strong>.
    Country B, a medium-sized country with an average annual wage of <strong>75k USD</strong>, generates a substantial volume of consumer-products waste.
    Country B will sell 20 million tons (approximately 22 billion pounds) of this waste to Country A at the prevailing market price.
    This waste is non-recyclable and will be burnt in Country A's incinerators.
    '''
    Waste_equality = '''
    Country A is a medium-sized nation with an average annual wage of <strong>31k USD</strong>.
    Country B, a medium-sized country with an average annual wage of <strong>31k USD</strong>, generates a substantial volume of consumer-products waste.
    Country B will sell 20 million tons (approximately 22 billion pounds) of this waste to Country A at the prevailing market price. 
    This waste is non-recyclable and will be burnt in Country A's incinerators.
    '''
    Baby_inequality = '''
    Person A is a 25 year old single, pregnant woman. She lives alone and works at a retail shop. 
    Her annual net income is <strong>31k USD</strong>. Person B is a 40 year old single woman. 
    She lives alone and her household's annual net income is <strong>75k USD</strong>. Person B wants to have a baby but is infertile.
    Adopting a baby in their country is extremely difficult. Person A will sell her baby to person B once she is born.
    '''
    Baby_equality = '''
    Person A is a 25 year old single, pregnant woman. She lives alone and works at a retail shop. 
    Her annual net income is <strong>31k USD</strong>. Person B is a 40 year old single woman. 
    She lives alone and her household's annual net income is <strong>31k USD</strong>. Person B wants to have a baby but is infertile.
    Adopting a baby in their country is extremely difficult. Person A will sell her baby to person B once she is born.
    '''
    Collector_inequality = '''
    Person A is a 40 year old man. He lives together with his wife and one kid in a household of 3 people.
    Their household's annual income is <strong>31k USD</strong>. Person B is a 40 year old man. 
    He lives together with her wife and one kid in a household of 3 people. Their annual income is <strong>75k USD</strong>.
    Person A has a coin collection he has been collecting since his teenages.
    Person A will sell this collection to person B at the prevailing market price.
    '''
    Collector_equality = '''
    Person A is a 40 year old man. He lives together with his wife and one kid in a household of 3 people.
    Their household's annual income is <strong>31k USD</strong>. Person B is a 40 year old man. 
    He lives together with her wife and one kid in a household of 3 people. Their annual income is <strong>31k USD</strong>.
    Person A has a coin collection he has been collecting since his teenages.
    Person A will sell this collection to person B at the prevailing market price.
    '''
    
    Attention_check = '''
    There is no person A or person B in this situation. It is important to us that you are reading these vignettes carefully. We use what are called "attention checks" to measure whether are paying attention. 
    This is one such attention check. To complete this attention check all you need to do is to move all the sliders all the way to the right and click "Next" to continue.
    Please move all the sliders below all the way to the right and continue.
    '''
    
    #TODO: i have changed the exploit question, check if it is ok.
    #Slider_label_exploit = 'In your opinion, does this transaction <strong>benefit or exploit person A</strong>?'
    Slider_label_exploit = 'What do you think about the following statement: "<strong>this transaction exploits person A</strong>"?'
    Slider_label_autonomy = 'In your opinion, does this transaction <strong>respect or limit individual autonomy (i.e. self-determination)</strong>?'
    Slider_label_coercion = 'In your opinion, does this transaction allow the person A <strong> to make fully informed choices or does it exert undue influence</strong>?'
    Slider_label_fairA = 'In your opinion, is this transaction <strong>fair or unfair to person A</strong>?'
    # Slider_label_fairB = 'In your opinion, is this transaction <strong>fair or unfair to person B </strong>?'
    Slider_label_dignity = 'In your opinion, does this transaction <strong>promote or violate human dignity</strong>?'
    Slider_label_ban = 'To what extend do you agree with the following statement: <strong>"this transaction should be banned"</strong>?'
    
    #TODO: same as above
    #Slider_label_country_exploit = 'In your opinion, does this transaction <strong>benefit or exploit country A</strong>?'
    Slider_label_country_exploit = 'What do you think about the following statement: "<strong>this transaction exploits country A</strong>"?'
    #TODO: does the following question make sense? Individual autonomy is not a country level concept. Idea: remove it from thsi question.
    Slider_label_country_autonomy = 'In your opinion, does this transaction <strong>respect or limit individual autonomy (i.e. self-determination)</strong>?'
    Slider_label_country_coercion = 'In your opinion, does this transaction allow the country A <strong> to make fully informed choices or does it exert undue influence</strong>?'
    Slider_label_country_fairA = 'In your opinion, is this transaction <strong>fair or unfair to country A</strong>?'
    # Slider_label_country_fairB = 'In your opinion, is this transaction <strong>fair or unfair to country B </strong>?'
    Slider_label_country_dignity = 'In your opinion, does this transaction <strong>promote or violate human dignity</strong>?'
    Slider_label_country_ban = 'In your opinion, should this transaction be <strong>banned or allowed</strong>?'
    
    
    
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):   
    # Attention check 2, 1 was in introduction 
    Attention_2 = models.BooleanField()
            
    # Player answers
    ## Survey
    ### Child labor
    Child_exploit = models.FloatField(blank=False, min=-10)
    Child_autonomy = models.FloatField(blank=False, min=-10)
    Child_coercion = models.FloatField(blank=False, min=-10)
    Child_fairA = models.FloatField(blank=False, min=-10)
    # Child_fairB = models.FloatField(blank=False, min=-10)
    Child_dignity = models.FloatField(blank=False, min=-10)
    Child_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    
    ### Kidney market
    Kidney_exploit = models.FloatField(blank=False, min=-10)
    Kidney_autonomy = models.FloatField(blank=False, min=-10)
    Kidney_coercion = models.FloatField(blank=False, min=-10)
    Kidney_fairA = models.FloatField(blank=False, min=-10)
    # Kidney_fairB = models.FloatField(blank=False, min=-10)
    Kidney_dignity = models.FloatField(blank=False, min=-10)
    Kidney_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    
    ### Waste trad
    Waste_exploit = models.FloatField(blank=False, min=-10)
    Waste_autonomy = models.FloatField(blank=False, min=-10)
    Waste_coercion = models.FloatField(blank=False, min=-10)
    Waste_fairA = models.FloatField(blank=False, min=-10)
    # Waste_fairB = models.FloatField(blank=False, min=-10)
    Waste_dignity = models.FloatField(blank=False, min=-10)
    Waste_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
   
    ### Selling babie
    Baby_exploit = models.FloatField(blank=False, min=-10)
    Baby_autonomy = models.FloatField(blank=False, min=-10)
    Baby_coercion = models.FloatField(blank=False, min=-10)
    Baby_fairA = models.FloatField(blank=False, min=-10)
    # Baby_fairB = models.FloatField(blank=False, min=-10)
    Baby_dignity = models.FloatField(blank=False, min=-10)
    Baby_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    
    ### Selling coin collection
    Collector_exploit = models.FloatField(blank=False, min=-10)
    Collector_autonomy = models.FloatField(blank=False, min=-10)
    Collector_coercion = models.FloatField(blank=False, min=-10)
    Collector_fairA = models.FloatField(blank=False, min=-10)
    # Collector_fairB = models.FloatField(blank=False, min=-10)
    Collector_dignity = models.FloatField(blank=False, min=-10)
    Collector_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
       
# Functions
def variables_for_template(player, Page_number, Attention_check=False):
    current_vignette = player.participant.Vignette_order[Page_number]
    labels_for_sliders = {
        'exploit': C.Slider_label_exploit, 
        'autonomy': C.Slider_label_autonomy,
        'coercion': C.Slider_label_coercion,
        'fairA': C.Slider_label_fairA,
        # 'fairB': C.Slider_label_fairB,
        'dignity': C.Slider_label_dignity,
        'ban': C.Slider_label_ban,
    }
        
    if current_vignette =='Waste' or current_vignette =='Waste':
        labels_for_sliders = {
        'exploit': C.Slider_label_country_exploit,
        'autonomy': C.Slider_label_country_autonomy,
        'coercion': C.Slider_label_country_coercion,
        'fairA': C.Slider_label_country_fairA,
        # 'fairB': C.Slider_label_country_fairB,
        'dignity': C.Slider_label_country_dignity,
        'ban': C.Slider_label_country_ban,         
        }
    label = current_vignette+'_'+player.participant.Treatment
    vignette_text = f"{getattr(C, label)}"
    if not Attention_check:
        return {'Instructions': C.Instructions_path,
                'Vignette': current_vignette,
                'Vignette_text': vignette_text,
                'Slider_labels': labels_for_sliders,
                }
    else:
        return {'Instructions': C.Instructions_path,
                'Vignette_text': C.Attention_check,
                'Slider_labels': labels_for_sliders,
                }
        
def get_form_fields(player, Page_number):
    current_vignette = player.participant.Vignette_order[Page_number]
    return [f"{current_vignette}_exploit", f"{current_vignette}_autonomy", f"{current_vignette}_coercion",
            f"{current_vignette}_fairA", 
            # f"{current_vignette}_fairB",
            f"{current_vignette}_dignity", f"{current_vignette}_ban"]
  
# Pages
class Attention_check_2(Page):         
    form_model = 'player'
    form_fields = ['Attention_2']
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True

    @staticmethod
    def vars_for_template(player: Player):
        return variables_for_template(player, 0, Attention_check=True)
    
    def before_next_page(player: Player, timeout_happened=False):
        if (not player.Attention_2 and not player.participant.vars['Attention_1']):
            player.participant.vars['Allowed'] = False
            player.participant.vars['Attention_passed'] = False

    @staticmethod
    def js_vars(player):
        return dict(vignette=player.participant.Vignette_order[0],)
  

class Page1(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        return get_form_fields(player, 0)
        
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        return variables_for_template(player, 0)
    
    @staticmethod
    def js_vars(player):
        return dict(vignette=player.participant.Vignette_order[0],)
    
class Page2(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        return get_form_fields(player, 1)
        
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        return variables_for_template(player, 1)
    
    @staticmethod
    def js_vars(player):
        return dict(vignette=player.participant.Vignette_order[1],)

class Page3(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        return get_form_fields(player, 2)
        
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        return variables_for_template(player, 2)
    
    @staticmethod
    def js_vars(player):
        return dict(vignette=player.participant.Vignette_order[2],)

class Page4(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        return get_form_fields(player, 3)
        
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        return variables_for_template(player, 3)
    
    @staticmethod
    def js_vars(player):
        return dict(vignette=player.participant.Vignette_order[3],)

        
# ADD back page Page2, Page3, Page4, Page5, Page6, Page7, Page8,
page_sequence = [
    Page1, Page2, Page3, Page4, 
    Attention_check_2,
    ]
