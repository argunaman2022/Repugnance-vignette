from otree.api import *
import random
import pandas as pd

doc = '''
This is the main survey app. It contains
1. Main survey 
2. One attention check.
- You can additionally calculate payoffs and save them at a participant field.
'''
#TODO: add an exit button for players to be able to quit and return the prolific assignment (add this to template as well)
class C(BaseConstants):
    NAME_IN_URL = 'BeliefsOfOthers'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Instructions_path = "_templates/global/Instructions.html"
    Instructions_SOB_path = "_templates/global/Instructions.html"
    
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
    Adopting a baby in person B's country is extremely difficult. Person A offers to sell her baby to person B once she is born.
    '''
    Baby_equality = '''
    Person A is a 25 year old single, pregnant woman. She lives alone and works at a retail shop. 
    Her annual net income is 30k USD. Person B is a 40 year old single woman. 
    She lives alone and her household's annual net income is 30k USD. Person B wants to have a baby but is infertile.
    Adopting a baby in person B's country is extremely difficult. Person A offers to sell her baby to person B once she is born.
    '''
    Attention_check = '''
    There is no person A or person B in this situation. It is important to us that you are reading these vignettes carefully. We use what are called "attention checks" to measure whether are paying attention. 
    This is one such attention check. To complete this attention check all you need to do is to move all the sliders all the way to the right and click "Next" to continue.
    Please move all the sliders below all the way to the right and continue.
    '''
    
    
    Slider_label_exploit = 'What do you think your partner\'s answer was to the following question: <br> <i>"does this transaction benefit or exploit person A?"</i>'
    Slider_label_autonomy = 'What do you think your partner\'s answer was to the following question: <br> <i>"does this transaction respect or limit individual autonomy (i.e. self-determination)?"</i>'
    Slider_label_coercion = 'What do you think your partner\'s answer was to the following question: <br> <i>"does this transaction allow the person A to make fully informed choices or does it exert undue influence?"</i>'
    Slider_label_fairA = 'What do you think your partner\'s answer was to the following question: <br> <i>"is this transaction fair or unfair to person A ?"</i>'
    Slider_label_fairB = 'What do you think your partner\'s answer was to the following question: <br> <i>"is this transaction fair or unfair to person B ?"</i>'
    Slider_label_dignity = 'What do you think your partner\'s answer was to the following question: <br> <i>"does this transaction promote or violate human dignity?"</i>'
    
    
    Slider_label_country_exploit = 'What do you think your partner\'s answer was to the following question: <br><i>"does this transaction <i>benefit or exploit country A?"</i>'
    Slider_label_country_autonomy = 'What do you think your partner\'s answer was to the following question: <br><i>"does this transaction respect or limit individual autonomy (i.e. self-determination)?"</i>'
    Slider_label_country_coercion = 'What do you think your partner\'s answer was to the following question: <br><i>"does this transaction allow the country A  to make fully informed choices or does it exert undue influence?"</i>'
    Slider_label_country_fairA = 'What do you think your partner\'s answer was to the following question: <br><i>"is this transaction fair or unfair to country A ?"</i>'
    Slider_label_country_fairB = 'What do you think your partner\'s answer was to the following question: <br><i>"is this transaction fair or unfair to country B ?"</i>'
    Slider_label_country_dignity = 'What do you think your partner\'s answer was to the following question: <br><i>"does this transaction promote or violate human dignity?"</i>'
    
    
    
    
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
    SOB_Child_inequality_exploit = models.FloatField(blank=False, min=-10)
    SOB_Child_inequality_autonomy = models.FloatField(blank=False, min=-10)
    SOB_Child_inequality_coercion = models.FloatField(blank=False, min=-10)
    SOB_Child_inequality_fairA = models.FloatField(blank=False, min=-10)
    SOB_Child_inequality_fairB = models.FloatField(blank=False, min=-10)
    SOB_Child_inequality_dignity = models.FloatField(blank=False, min=-10)
    SOB_Child_inequality_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    
    SOB_Child_equality_exploit = models.FloatField(blank=False, min=-10)
    SOB_Child_equality_autonomy = models.FloatField(blank=False, min=-10)
    SOB_Child_equality_coercion = models.FloatField(blank=False, min=-10)
    SOB_Child_equality_fairA = models.FloatField(blank=False, min=-10)
    SOB_Child_equality_fairB = models.FloatField(blank=False, min=-10)
    SOB_Child_equality_dignity = models.FloatField(blank=False, min=-10)
    SOB_Child_equality_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    ### Kidney market, min=-10s
    SOB_Kidney_inequality_exploit = models.FloatField(blank=False, min=-10)
    SOB_Kidney_inequality_autonomy = models.FloatField(blank=False, min=-10)
    SOB_Kidney_inequality_coercion = models.FloatField(blank=False, min=-10)
    SOB_Kidney_inequality_fairA = models.FloatField(blank=False, min=-10)
    SOB_Kidney_inequality_fairB = models.FloatField(blank=False, min=-10)
    SOB_Kidney_inequality_dignity = models.FloatField(blank=False, min=-10)
    SOB_Kidney_inequality_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    
    SOB_Kidney_equality_exploit = models.FloatField(blank=False, min=-10)
    SOB_Kidney_equality_autonomy = models.FloatField(blank=False, min=-10)
    SOB_Kidney_equality_coercion = models.FloatField(blank=False, min=-10)
    SOB_Kidney_equality_fairA = models.FloatField(blank=False, min=-10)
    SOB_Kidney_equality_fairB = models.FloatField(blank=False, min=-10)
    SOB_Kidney_equality_dignity = models.FloatField(blank=False, min=-10)
    SOB_Kidney_equality_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    ### Waste trad, min=-10e
    SOB_Waste_inequality_exploit = models.FloatField(blank=False, min=-10)
    SOB_Waste_inequality_autonomy = models.FloatField(blank=False, min=-10)
    SOB_Waste_inequality_coercion = models.FloatField(blank=False, min=-10)
    SOB_Waste_inequality_fairA = models.FloatField(blank=False, min=-10)
    SOB_Waste_inequality_fairB = models.FloatField(blank=False, min=-10)
    SOB_Waste_inequality_dignity = models.FloatField(blank=False, min=-10)
    SOB_Waste_inequality_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
   
    SOB_Waste_equality_exploit = models.FloatField(blank=False, min=-10)
    SOB_Waste_equality_autonomy = models.FloatField(blank=False, min=-10)
    SOB_Waste_equality_coercion = models.FloatField(blank=False, min=-10)
    SOB_Waste_equality_fairA = models.FloatField(blank=False, min=-10)
    SOB_Waste_equality_fairB = models.FloatField(blank=False, min=-10)
    SOB_Waste_equality_dignity = models.FloatField(blank=False, min=-10)
    SOB_Waste_equality_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    ### Selling babie, min=-10s
    SOB_Baby_inequality_exploit = models.FloatField(blank=False, min=-10)
    SOB_Baby_inequality_autonomy = models.FloatField(blank=False, min=-10)
    SOB_Baby_inequality_coercion = models.FloatField(blank=False, min=-10)
    SOB_Baby_inequality_fairA = models.FloatField(blank=False, min=-10)
    SOB_Baby_inequality_fairB = models.FloatField(blank=False, min=-10)
    SOB_Baby_inequality_dignity = models.FloatField(blank=False, min=-10)
    SOB_Baby_inequality_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
   
    SOB_Baby_equality_exploit = models.FloatField(blank=False, min=-10)
    SOB_Baby_equality_autonomy = models.FloatField(blank=False, min=-10)
    SOB_Baby_equality_coercion = models.FloatField(blank=False, min=-10)
    SOB_Baby_equality_fairA = models.FloatField(blank=False, min=-10)
    SOB_Baby_equality_fairB = models.FloatField(blank=False, min=-10)
    SOB_Baby_equality_dignity = models.FloatField(blank=False, min=-10)
    SOB_Baby_equality_ban = models.IntegerField() #1 yes/ban 0 no/dont ban

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
    }
        
    if current_vignette =='Waste_inequality' or current_vignette =='Waste_equality':
        labels_for_sliders = {
        'exploit': C.Slider_label_country_exploit,
        'autonomy': C.Slider_label_country_autonomy,
        'coercion': C.Slider_label_country_coercion,
        'fairA': C.Slider_label_country_fairA,
        'fairB': C.Slider_label_country_fairB,
        'dignity': C.Slider_label_country_dignity,
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
    return [f"SOB_{current_vignette}_exploit", f"SOB_{current_vignette}_autonomy", f"SOB_{current_vignette}_coercion",
            f"SOB_{current_vignette}_fairA", f"SOB_{current_vignette}_fairB", f"SOB_{current_vignette}_dignity", f"SOB_{current_vignette}_ban"]
  
# Pages
class Introduction_SOB(Page):            
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(self):
        return {'Instructions': C.Instructions_SOB_path}


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
        vignette=player.participant.Vignette_order[0]
        current_vignette = vignette.split('_')[0]
        return dict(vignette=vignette,
                    current_vignette=current_vignette,)

   
page_sequence = [
    Introduction_SOB,
    Page1, 
    ]
