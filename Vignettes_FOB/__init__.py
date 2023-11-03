from otree.api import *
import random

doc = '''
This is the main survey app. It contains
1. Main survey 
2. One attention check.
- You can additionally calculate payoffs and save them at a participant field.
'''
#TODO: add an exit button for players to be able to quit and return the prolific assignment (add this to template as well)
class C(BaseConstants):
    NAME_IN_URL = 'Scenarios'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Instructions_path = "_templates/global/Instructions.html"
    
    # vignette texts
    Child_inequality = '''
    Person A is a 13 year old girl. She lives together with her parents in a household of 3 people. Their household's annual income is 31k USD.
    Person B is a 50 year old woman. She lives together with her husband and mother in a household of 3 people.
    Their annual income is 75k USD. Person A works 5 hours every Saturday cleaning person B's 2 story-house. A's hourly wage is 15 USD/hour.'''
    Child_equality = '''
    Person A is a 13 year old girl. She lives together with her parents in a household of 3 people. Their household's annual income is 31k USD.
    Person B is a 50 year old woman. She lives together with her husband and mother in a household of 3 people.
    Their annual income is 31k USD. Person A works 5 hours every Saturday cleaning person B's 2 story-house. A's hourly wage is 15 USD/hour.'''
    
    Kidney_inequality = '''
    Person A is a 40 year old man. He lives together with his wife and one kid in a household of 3 people.
    Their household's annual income is 31k USD.  Person B is a 40 year old man.
    He lives together with her wife and one kid in a household of 3 people. Their annual income is 75k USD.
    Due to a final-stage kidney disease, person A is in desperate need of a replacement kidney.
    Person A sells one of his kidneys to person B.'''
    Kidney_equality = '''
    Person A is a 40 year old man. He lives together with his wife and one kid in a household of 3 people.
    Their household's annual income is 31k USD.  Person B is a 40 year old man.
    He lives together with her wife and one kid in a household of 3 people. Their annual income is 31k USD.
    Due to a final-stage kidney disease, person A is in desperate need of a replacement kidney.
    Person A sells one of his kidneys to person B.'''
    
    Waste_inequality = '''
    Country A is a medium-sized nation with an average annual wage of $32,000.
    Country B, a medium-sized country with an average annual wage of $73,000, generates a substantial volume of consumer-products waste.
    Country B offers to sell 20 million tonnes (approximately 22 billion pounds) of this waste to Country A at the prevailing market price.
    This waste will be burnt in Country A's incinerators.
    '''
    Waste_equality = '''
    Country A is a medium-sized nation with an average annual wage of $30,000.
    Country B, a medium-sized country with an average annual wage of $32,000, generates a substantial volume of consumer-products waste.
    Country B offers to sell 20 million tonnes (approximately 22 billion pounds) of this waste to Country A at the prevailing market price. 
    This waste will be burnt in Country A's incinerators.
    '''
    
    Baby_inequality = '''
    Person A is a 25 year old single, pregnant woman. She lives alone and works at a retail shop. 
    Her annual net income is 30k USD. Person B is a 40 year old single woman. 
    She lives alone and her household's annual net income is 75k USD. Person B wants to have a baby but is infertile.
    Adopting a baby in person B's country is extremely difficult. Person A offers to sell her baby to person B one she is born.
    '''
    Baby_equality = '''
    Person A is a 25 year old single, pregnant woman. She lives alone and works at a retail shop. 
    Her annual net income is 30k USD. Person B is a 40 year old single woman. 
    She lives alone and her household's annual net income is 30k USD. Person B wants to have a baby but is infertile.
    Adopting a baby in person B's country is extremely difficult. Person A offers to sell her baby to person B one she is born.
    '''
    Attention_check = '''
    There is no person A or person B in this situation. It is important to us that you are reading these vignettes carefully. We use what are called "attention checks" to measure whether are paying attention. 
    This is one such attention check. To complete this attention check all you need to do is to move all the sliders all the way to the right and click "Next" to continue.
    Please move all the sliders below all the way to the right and continue.
    '''
    
    
    Slider_label_exploit = 'In your opinion, does this transaction <strong>benefit or exploit person A</strong>'
    Slider_label_autonomy = 'In your opinion, does this transaction <strong>respect or limit individual autonomy (i.e. self-determination)</strong>?'
    Slider_label_coercion = 'In your opinion, does this transaction allow the person A <strong> to make fully informed choices or does it exert undue influence</strong>?'
    Slider_label_fairA = 'In your opinion, is this transaction <strong>fair or unfair to person A </strong>?'
    Slider_label_fairB = 'In your opinion, is this transaction <strong>fair or unfair to person B </strong>?'
    Slider_label_dignity = 'In your opinion, does this transaction <strong>promote or violate human dignity</strong>?'
    Slider_label_ban = 'To what extend do you agree with the following statement: <strong>"this transaction should be banned"</strong>?'
    
    Slider_label_country_exploit = 'In your opinion, does this transaction <strong>benefit or exploit country A</strong>'
    Slider_label_country_autonomy = 'In your opinion, does this transaction <strong>respect or limit individual autonomy (i.e. self-determination)</strong>?'
    Slider_label_country_coercion = 'In your opinion, does this transaction allow the country A <strong> to make fully informed choices or does it exert undue influence</strong>?'
    Slider_label_country_fairA = 'In your opinion, is this transaction <strong>fair or unfair to country A </strong>?'
    Slider_label_country_fairB = 'In your opinion, is this transaction <strong>fair or unfair to country B </strong>?'
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
    Child_inequality_exploit = models.FloatField(blank=False, min=-10)
    Child_inequality_autonomy = models.FloatField(blank=False, min=-10)
    Child_inequality_coercion = models.FloatField(blank=False, min=-10)
    Child_inequality_fairA = models.FloatField(blank=False, min=-10)
    Child_inequality_fairB = models.FloatField(blank=False, min=-10)
    Child_inequality_dignity = models.FloatField(blank=False, min=-10)
    Child_inequality_ban = models.BooleanField(label='In your opinion, should such transactions be banned?',
                                            choices=[[True, 'Yes'], [False,'No']])
    
    Child_equality_exploit = models.FloatField(blank=False, min=-10)
    Child_equality_autonomy = models.FloatField(blank=False, min=-10)
    Child_equality_coercion = models.FloatField(blank=False, min=-10)
    Child_equality_fairA = models.FloatField(blank=False, min=-10)
    Child_equality_fairB = models.FloatField(blank=False, min=-10)
    Child_equality_dignity = models.FloatField(blank=False, min=-10)
    Child_equality_ban = models.BooleanField(label='In your opinion, should such transactions be banned?',
                                            choices=[[True, 'Yes'], [False,'No']])
    ### Kidney market, min=-10s
    Kidney_inequality_exploit = models.FloatField(blank=False, min=-10)
    Kidney_inequality_autonomy = models.FloatField(blank=False, min=-10)
    Kidney_inequality_coercion = models.FloatField(blank=False, min=-10)
    Kidney_inequality_fairA = models.FloatField(blank=False, min=-10)
    Kidney_inequality_fairB = models.FloatField(blank=False, min=-10)
    Kidney_inequality_dignity = models.FloatField(blank=False, min=-10)
    Kidney_inequality_ban = models.BooleanField(label='In your opinion, should such transactions be banned?',
                                            choices=[[True, 'Yes'], [False,'No']])
    
    Kidney_equality_exploit = models.FloatField(blank=False, min=-10)
    Kidney_equality_autonomy = models.FloatField(blank=False, min=-10)
    Kidney_equality_coercion = models.FloatField(blank=False, min=-10)
    Kidney_equality_fairA = models.FloatField(blank=False, min=-10)
    Kidney_equality_fairB = models.FloatField(blank=False, min=-10)
    Kidney_equality_dignity = models.FloatField(blank=False, min=-10)
    Kidney_equality_ban = models.BooleanField(label='In your opinion, should such transactions be banned?',
                                            choices=[[True, 'Yes'], [False,'No']])
    ### Waste trad, min=-10e
    Waste_inequality_exploit = models.FloatField(blank=False, min=-10)
    Waste_inequality_autonomy = models.FloatField(blank=False, min=-10)
    Waste_inequality_coercion = models.FloatField(blank=False, min=-10)
    Waste_inequality_fairA = models.FloatField(blank=False, min=-10)
    Waste_inequality_fairB = models.FloatField(blank=False, min=-10)
    Waste_inequality_dignity = models.FloatField(blank=False, min=-10)
    Waste_inequality_ban = models.BooleanField(label='In your opinion, should such transactions be banned?',
                                            choices=[[True, 'Yes'], [False,'No']])
   
    Waste_equality_exploit = models.FloatField(blank=False, min=-10)
    Waste_equality_autonomy = models.FloatField(blank=False, min=-10)
    Waste_equality_coercion = models.FloatField(blank=False, min=-10)
    Waste_equality_fairA = models.FloatField(blank=False, min=-10)
    Waste_equality_fairB = models.FloatField(blank=False, min=-10)
    Waste_equality_dignity = models.FloatField(blank=False, min=-10)
    Waste_equality_ban = models.BooleanField(label='In your opinion, should such transactions be banned?',
                                            choices=[[True, 'Yes'], [False,'No']])
    ### Selling babie, min=-10s
    Baby_inequality_exploit = models.FloatField(blank=False, min=-10)
    Baby_inequality_autonomy = models.FloatField(blank=False, min=-10)
    Baby_inequality_coercion = models.FloatField(blank=False, min=-10)
    Baby_inequality_fairA = models.FloatField(blank=False, min=-10)
    Baby_inequality_fairB = models.FloatField(blank=False, min=-10)
    Baby_inequality_dignity = models.FloatField(blank=False, min=-10)
    Baby_inequality_ban = models.BooleanField(label='In your opinion, should such transactions be banned?',
                                            choices=[[True, 'Yes'], [False,'No']])
   
    Baby_equality_exploit = models.FloatField(blank=False, min=-10)
    Baby_equality_autonomy = models.FloatField(blank=False, min=-10)
    Baby_equality_coercion = models.FloatField(blank=False, min=-10)
    Baby_equality_fairA = models.FloatField(blank=False, min=-10)
    Baby_equality_fairB = models.FloatField(blank=False, min=-10)
    Baby_equality_dignity = models.FloatField(blank=False, min=-10)
    Baby_equality_ban = models.BooleanField(label='In your opinion, should such transactions be banned?',
                                            choices=[[True, 'Yes'], [False,'No']])

# Functions
def variables_for_template(player, Page_number, Attention_check=False):
    current_vignette = player.participant.Vignette_order[Page_number]
    labels_for_sliders = {
        'exploit': C.Slider_label_exploit, 
        'autonomy': C.Slider_label_autonomy,
        'coercion': C.Slider_label_coercion,
        'fairA': C.Slider_label_fairA,
        'fairB': C.Slider_label_fairB,
        'dignity': C.Slider_label_dignity,
        'ban': C.Slider_label_ban,
    }
        
    if current_vignette =='Waste_inequality' or current_vignette =='Waste_equality':
        labels_for_sliders = {
        'exploit': C.Slider_label_country_exploit,
        'autonomy': C.Slider_label_country_autonomy,
        'coercion': C.Slider_label_country_coercion,
        'fairA': C.Slider_label_country_fairA,
        'fairB': C.Slider_label_country_fairB,
        'dignity': C.Slider_label_country_dignity,
        'ban': C.Slider_label_country_ban,         
        }
    if not Attention_check:
        return {'Instructions': C.Instructions_path,
                'Vignette': current_vignette,
                'Vignette_text': f"{getattr(C, current_vignette)}",
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
            f"{current_vignette}_fairA", f"{current_vignette}_fairB", f"{current_vignette}_dignity", f"{current_vignette}_ban"]
  
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

class Page5(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        return get_form_fields(player, 4)
        
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        return variables_for_template(player, 4)
    
    @staticmethod
    def js_vars(player):
        return dict(vignette=player.participant.Vignette_order[4],)

class Page6(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        return get_form_fields(player, 5)
        
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        return variables_for_template(player, 5)
    
    @staticmethod
    def js_vars(player):
        return dict(vignette=player.participant.Vignette_order[5],)

class Page7(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        return get_form_fields(player, 6)
        
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        return variables_for_template(player, 6)
    
    @staticmethod
    def js_vars(player):
        return dict(vignette=player.participant.Vignette_order[6],)

class Page8(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        return get_form_fields(player, 7)
        
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        return variables_for_template(player, 7)
    
    @staticmethod
    def js_vars(player):
        return dict(vignette=player.participant.Vignette_order[7],)
        

page_sequence = [
    Page1, Page2, Page3, Page4, Page5, Page6, Page7, Page8,
    Attention_check_2,
    ]