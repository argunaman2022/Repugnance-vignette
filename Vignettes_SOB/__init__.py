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
    NAME_IN_URL = 'others_beliefs'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Instructions_path = "_templates/global/Instructions.html"
    Instructions_SOB_path = "_templates/global/Instructions.html" #TODO: add instructions for SOB
    
    # vignette characteristics
    vignette_characteristics = pd.read_excel('_templates/global/Vignette_characteristics.xlsx',
                                             index_col=0, sheet_name='Persons')
    #country_vignette_characteristics = pd.read_excel('_templates/global/Vignette_characteristics.xlsx', sheet_name='Country')
  
    
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):              
    # Player answers
    ## Survey
    ### Child labor
    Child_equality_SOB = models.FloatField(
        label='What percentage of people chose to ban the transaction in <strong>Version 1?</strong>',
        min=0, max=100)
    Child_inequality_SOB = models.FloatField(
        label='What percentage of people chose to ban the transaction in <strong>Version 2?</strong>',
        min=0, max=100)
    Kidney_equality_SOB = models.FloatField(
        label='What percentage of people chose to ban the transaction in <strong>Version 1?</strong>',
        min=0, max=100)
    Kidney_inequality_SOB = models.FloatField(
        label='What percentage of people chose to ban the transaction in <strong>Version 2?</strong>',
        min=0, max=100)
    Waste_equality_SOB = models.FloatField(
        label='What percentage of people chose to ban the transaction in <strong>Version 1?</strong>',
        min=0, max=100)
    Waste_inequality_SOB = models.FloatField(
        label='What percentage of people chose to ban the transaction in <strong>Version 2?</strong>',
        min=0, max=100)
    Baby_equality_SOB = models.FloatField(
        label='What percentage of people chose to ban the transaction in <strong>Version 1?</strong>',
        min=0, max=100)
    Baby_inequality_SOB = models.FloatField(
        label='What percentage of people chose to ban the transaction in <strong>Version 2?</strong>',
        min=0, max=100)
    
# Functions
def variables_for_template(player, Page_number, Attention_check=False):
    current_vignette_full_name = player.participant.Vignette_order[Page_number] #e.g. Baby_inequality
    current_vignette = current_vignette_full_name.split("_")[0] #e.g. Baby
    current_vignette_inequality = current_vignette + '_inequality' #e.g. Baby_inequality
    current_vignette_equality = current_vignette + '_equality' #e.g. Baby_equality
    
    vignette_characteristics = C.vignette_characteristics.copy().transpose()
    vignette_characteristics = vignette_characteristics[vignette_characteristics.iloc[:,0] == current_vignette]

    labels_for_table = {
        'transaction': vignette_characteristics.loc[current_vignette_full_name,'Transaction'], 
        'transaction_price': vignette_characteristics.loc[current_vignette_full_name,'Transaction price'], 
        'seller': vignette_characteristics.loc[current_vignette_full_name,'Seller'], 
        'seller_incomev1': vignette_characteristics.loc[current_vignette_full_name,'Sellers household income'], 
        'seller_incomev2': vignette_characteristics.loc[current_vignette_full_name,'Sellers household income'], 
        'buyer': vignette_characteristics.loc[current_vignette_full_name,'Buyer'], 
        'buyer_incomev1': vignette_characteristics.loc[current_vignette_equality,'Buyers household income'],  
        'buyer_incomev2': vignette_characteristics.loc[current_vignette_inequality,'Buyers household income'],  
    }
    print(vignette_characteristics)
        
    return {'Instructions': C.Instructions_path,
            'Vignette': current_vignette,
            'labels_for_table': labels_for_table,
            }
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
    form_fields = ['Waste_inequality_SOB', 'Waste_equality_SOB'] #TODO: make this dynamic and randomize. currently doesnt work
        
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True
    
    @staticmethod
    def vars_for_template(player: Player):
        return variables_for_template(player, 0)
    
    @staticmethod
    def js_vars(player):
        vignette=player.participant.Vignette_order[0] #e.g. Baby_inequality
        current_vignette = vignette.split("_")[0] #e.g. Baby
        return dict(vignette=vignette,current_vignette=current_vignette)
   
page_sequence = [
    Introduction_SOB,
    Page1, 
    ]
