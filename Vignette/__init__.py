from otree.api import *
import random

doc = '''
This is the main survey app. It contains
1. Main survey 
2. One attention check.
- You can additionally calculate payoffs and save them at a participant field.
'''

class C(BaseConstants):
    NAME_IN_URL = 'Study_Name'
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
    She lives together with her husband in a household of 2 people. Their annual income is 75k USD.
    Due to a final-stage kidney disease, person A is in desperate need of a replacement kidney.
    Person A sells one of his kidneys to person B.'''
    Kidney_equality = '''
    Person A is a 40 year old man. He lives together with his wife and one kid in a household of 3 people.
    Their household's annual income is 31k USD.  Person B is a 40 year old man.
    She lives together with her husband in a household of 2 people. Their annual income is 31k USD.
    Due to a final-stage kidney disease, person A is in desperate need of a replacement kidney.
    Person A sells one of his kidneys to person B.'''
    
    Waste_inequality = '''
    Country A is a medium-sized nation with an average annual wage of $32,000.
    Country B, a medium-sized country with an average annual wage of $73,000, generates a substantial volume of consumer-products waste.
    Country B offers to sell 20 million tonnes (approximately 22 billion pounds) of this waste to Country A at the prevailing market price.
    '''
    Waste_equality = '''
    Country A is a medium-sized nation with an average annual wage of $30,000.
    Country B, a medium-sized country with an average annual wage of $32,000, generates a substantial volume of consumer-products waste.
    Country B offers to sell 20 million tonnes (approximately 22 billion pounds) of this waste to Country A at the prevailing market price.
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
    
    
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):   
    # Attention check 2, 1 was in introduction 
    Attention_2 = models.BooleanField(choices=[
            [True, 'I disagree.'],
            [False, 'I think both are possible.'],
            [False, 'I agree.'],], 
        label= 'A 20 year old man can eat 500kg meat and 2 tons of vegetables in one meal.', widget=widgets.RadioSelect)
            
    # Player answers
    ## Survey
    ### Child labor
    Child_inequality_exploit = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>benefit or exploit person A (the girl)</strong>')
    Child_inequality_autonomy = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>respect or limit individual autonomy (i.e. self-determination)</strong>?')
    Child_inequality_coercion = models.FloatField(blank=True, label = 'In your opinion, does this transaction allow the person A (the girl) <strong> to make fully informed choices or does it exert undue influence</strong>?')
    Child_inequality_fairA = models.FloatField(blank=True, label = 'In your opinion, is this transaction <strong>fair or unfair to person A (the girl)</strong>?')
    Child_inequality_fairB = models.FloatField(blank=True, label = 'In your opinion, is this transaction <strong>fair or unfair to person B (the woman)</strong>?')
    Child_inequality_dignity = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>promote or violate human dignity</strong>?')
    Child_inequality_ban = models.FloatField(blank=True, label = 'In your opinion, should this transaction be <strong>banned or allowed</strong>?')
    
    Child_equality_exploit = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>benefit or exploit person A (the girl)</strong>')
    Child_equality_autonomy = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>respect or limit individual autonomy (i.e. self-determination)</strong>?')
    Child_equality_coercion = models.FloatField(blank=True, label = 'In your opinion, does this transaction allow the person A (the girl) <strong> to make fully informed choices or does it exert undue influence</strong>?')
    Child_equality_fairA = models.FloatField(blank=True, label = 'In your opinion, is this transaction <strong>fair or unfair to person A (the girl)</strong>?')
    Child_equality_fairB = models.FloatField(blank=True, label = 'In your opinion, is this transaction <strong>fair or unfair to person B (the woman)</strong>?')
    Child_equality_dignity = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>promote or violate human dignity</strong>?')
    Child_equality_ban = models.FloatField(blank=True, label = 'In your opinion, should this transaction be <strong>banned or allowed</strong>?')
    ### Kidney markets
    Kidney_inequality_exploit = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>benefit or exploit person A (the seller)</strong>')
    Kidney_inequality_autonomy = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>respect or limit individual autonomy (i.e. self-determination)</strong>?')
    Kidney_inequality_coercion = models.FloatField(blank=True, label = 'In your opinion, does this transaction allow the person A (the seller) <strong> to make fully informed choices or does it exert undue influence</strong>?')
    Kidney_inequality_fairA = models.FloatField(blank=True, label = 'In your opinion, is this transaction <strong>fair or unfair to person A (the seller)</strong>?')
    Kidney_inequality_fairB = models.FloatField(blank=True, label = 'In your opinion, is this transaction <strong>fair or unfair to person B (the buyer)</strong>?')
    Kidney_inequality_dignity = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>promote or violate human dignity</strong>?')
    Kidney_inequality_ban = models.FloatField(blank=True, label = 'In your opinion, should this transaction be <strong>banned or allowed</strong>?')
     
    Kidney_equality_exploit = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>benefit or exploit person A (the seller)</strong>')
    Kidney_equality_autonomy = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>respect or limit individual autonomy (i.e. self-determination)</strong>?')
    Kidney_equality_coercion = models.FloatField(blank=True, label = 'In your opinion, does this transaction allow the person A (the seller) <strong> to make fully informed choices or does it exert undue influence</strong>?')
    Kidney_equality_fairA = models.FloatField(blank=True, label = 'In your opinion, is this transaction <strong>fair or unfair to person A (the seller)</strong>?')
    Kidney_equality_fairB = models.FloatField(blank=True, label = 'In your opinion, is this transaction <strong>fair or unfair to person B (the buyer)</strong>?')
    Kidney_equality_dignity = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>promote or violate human dignity</strong>?')
    Kidney_equality_ban = models.FloatField(blank=True, label = 'In your opinion, should this transaction be <strong>banned or allowed</strong>?')
    ### Waste trade
    Waste_inequality_exploit = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>benefit or exploit country A (the buyer)</strong>')
    Waste_inequality_autonomy = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>respect or limit individual autonomy (i.e. self-determination)</strong>?')
    Waste_inequality_coercion = models.FloatField(blank=True, label = 'In your opinion, does this transaction allow the person A (the buyer) <strong> to make fully informed choices or does it exert undue influence</strong>?')
    Waste_inequality_fairA = models.FloatField(blank=True, label = 'In your opinion, is this transaction <strong>fair or unfair to person A (the buyer)</strong>?')
    Waste_inequality_fairB = models.FloatField(blank=True, label = 'In your opinion, is this transaction <strong>fair or unfair to person B (the seller)</strong>?')
    Waste_inequality_dignity = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>promote or violate human dignity</strong>?')
    Waste_inequality_ban = models.FloatField(blank=True, label = 'In your opinion, should this transaction be <strong>banned or allowed</strong>?')
    
    Waste_equality_exploit = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>benefit or exploit country A (the buyer)</strong>')
    Waste_equality_autonomy = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>respect or limit individual autonomy (i.e. self-determination)</strong>?')
    Waste_equality_coercion = models.FloatField(blank=True, label = 'In your opinion, does this transaction allow the person A (the buyer) <strong> to make fully informed choices or does it exert undue influence</strong>?')
    Waste_equality_fairA = models.FloatField(blank=True, label = 'In your opinion, is this transaction <strong>fair or unfair to person A (the buyer)</strong>?')
    Waste_equality_fairB = models.FloatField(blank=True, label = 'In your opinion, is this transaction <strong>fair or unfair to person B (the seller)</strong>?')
    Waste_equality_dignity = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>promote or violate human dignity</strong>?')
    Waste_equality_ban = models.FloatField(blank=True, label = 'In your opinion, should this transaction be <strong>banned or allowed</strong>?')
    ### Selling babies
    Baby_inequality_exploit = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>benefit or exploit person A (the seller)</strong>')
    Baby_inequality_autonomy = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>respect or limit individual autonomy (i.e. self-determination)</strong>?')
    Baby_inequality_coercion = models.FloatField(blank=True, label = 'In your opinion, does this transaction allow the person A (the seller) <strong> to make fully informed choices or does it exert undue influence</strong>?')
    Baby_inequality_fairA = models.FloatField(blank=True, label = 'In your opinion, is this transaction <strong>fair or unfair to person A (the seller)</strong>?')
    Baby_inequality_fairB = models.FloatField(blank=True, label = 'In your opinion, is this transaction <strong>fair or unfair to person B (the buyer)</strong>?')
    Baby_inequality_dignity = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>promote or violate human dignity</strong>?')
    Baby_inequality_ban = models.FloatField(blank=True, label = 'In your opinion, should this transaction be <strong>banned or allowed</strong>?')
    
    Baby_equality_exploit = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>benefit or exploit person A (the seller)</strong>')
    Baby_equality_autonomy = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>respect or limit individual autonomy (i.e. self-determination)</strong>?')
    Baby_equality_coercion = models.FloatField(blank=True, label = 'In your opinion, does this transaction allow the person A (the seller) <strong> to make fully informed choices or does it exert undue influence</strong>?')
    Baby_equality_fairA = models.FloatField(blank=True, label = 'In your opinion, is this transaction <strong>fair or unfair to person A (the seller)</strong>?')
    Baby_equality_fairB = models.FloatField(blank=True,label = 'In your opinion, is this transaction <strong>fair or unfair to person B (the buyer)</strong>?')
    Baby_equality_dignity = models.FloatField(blank=True, label = 'In your opinion, does this transaction <strong>promote or violate human dignity</strong>?')
    Baby_equality_ban = models.FloatField(blank=True, label = 'In your opinion, should this transaction be <strong>banned or allowed</strong>?')
    
  
# Pages
class Page1(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        current_vignette = player.participant.Vignette_order[0]
        return [f"{current_vignette}_exploit", f"{current_vignette}_autonomy", f"{current_vignette}_coercion",
                f"{current_vignette}_fairA", f"{current_vignette}_fairB", f"{current_vignette}_dignity", f"{current_vignette}_ban"]

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        current_vignette = player.participant.Vignette_order[0]
        return {'Instructions': C.Instructions_path,
                'Vignette': current_vignette,
                'Vignette_text': f"{getattr(C, current_vignette)}",
                }
class Page2(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        current_vignette = player.participant.Vignette_order[1]
        return [f"{current_vignette}_exploit", f"{current_vignette}_autonomy", f"{current_vignette}_coercion",
                f"{current_vignette}_fairA", f"{current_vignette}_fairB", f"{current_vignette}_dignity", f"{current_vignette}_ban"]

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        current_vignette = player.participant.Vignette_order[1]
        return {'Instructions': C.Instructions_path,
                'Vignette': current_vignette,
                'Vignette_text': f"{getattr(C, current_vignette)}",
                }
class Page3(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        current_vignette = player.participant.Vignette_order[2]
        return [f"{current_vignette}_exploit", f"{current_vignette}_autonomy", f"{current_vignette}_coercion",
                f"{current_vignette}_fairA", f"{current_vignette}_fairB", f"{current_vignette}_dignity", f"{current_vignette}_ban"]

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        current_vignette = player.participant.Vignette_order[2]
        return {'Instructions': C.Instructions_path,
                'Vignette': current_vignette,
                'Vignette_text': f"{getattr(C, current_vignette)}",
                }
class Page4(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        current_vignette = player.participant.Vignette_order[3]
        return [f"{current_vignette}_exploit", f"{current_vignette}_autonomy", f"{current_vignette}_coercion",
                f"{current_vignette}_fairA", f"{current_vignette}_fairB", f"{current_vignette}_dignity", f"{current_vignette}_ban"]

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        current_vignette = player.participant.Vignette_order[3]
        return {'Instructions': C.Instructions_path,
                'Vignette': current_vignette,
                'Vignette_text': f"{getattr(C, current_vignette)}",
                }
class Page5(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        current_vignette = player.participant.Vignette_order[4]
        return [f"{current_vignette}_exploit", f"{current_vignette}_autonomy", f"{current_vignette}_coercion",
                f"{current_vignette}_fairA", f"{current_vignette}_fairB", f"{current_vignette}_dignity", f"{current_vignette}_ban"]

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        current_vignette = player.participant.Vignette_order[4]
        return {'Instructions': C.Instructions_path,
                'Vignette': current_vignette,
                'Vignette_text': f"{getattr(C, current_vignette)}",
                }
class Page6(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        current_vignette = player.participant.Vignette_order[5]
        return [f"{current_vignette}_exploit", f"{current_vignette}_autonomy", f"{current_vignette}_coercion",
                f"{current_vignette}_fairA", f"{current_vignette}_fairB", f"{current_vignette}_dignity", f"{current_vignette}_ban"]

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        current_vignette = player.participant.Vignette_order[5]
        return {'Instructions': C.Instructions_path,
                'Vignette': current_vignette,
                'Vignette_text': f"{getattr(C, current_vignette)}",
                }
class Page7(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        current_vignette = player.participant.Vignette_order[6]
        return [f"{current_vignette}_exploit", f"{current_vignette}_autonomy", f"{current_vignette}_coercion",
                f"{current_vignette}_fairA", f"{current_vignette}_fairB", f"{current_vignette}_dignity", f"{current_vignette}_ban"]

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        current_vignette = player.participant.Vignette_order[6]
        return {'Instructions': C.Instructions_path,
                'Vignette': current_vignette,
                'Vignette_text': f"{getattr(C, current_vignette)}",
                }
class Page8(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        current_vignette = player.participant.Vignette_order[7]
        return [f"{current_vignette}_exploit", f"{current_vignette}_autonomy", f"{current_vignette}_coercion",
                f"{current_vignette}_fairA", f"{current_vignette}_fairB", f"{current_vignette}_dignity", f"{current_vignette}_ban"]

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        current_vignette = player.participant.Vignette_order[7]
        return {'Instructions': C.Instructions_path,
                'Vignette': current_vignette,
                'Vignette_text': f"{getattr(C, current_vignette)}",
                }


class Attention_check_2(Page):         
    form_model = 'player'
    form_fields = ['Attention_2']
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True

    @staticmethod
    def vars_for_template(player: Player):
        return {'Instructions': C.Instructions_path}
    
    def before_next_page(player: Player, timeout_happened=False):
        if (not player.Attention_2 and not player.participant.vars['Attention_1']):
            player.participant.vars['Allowed'] = False
            player.participant.vars['Attention_passed'] = False
  
page_sequence = [
    Page1, Page2, Page3, Page4, Page5, Page6, Page7, Page8,
    Attention_check_2,
    ]
