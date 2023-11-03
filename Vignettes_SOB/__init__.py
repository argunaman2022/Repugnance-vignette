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
    Child_inequality_SOB = models.IntegerField(
        label='What percentage of people chose to ban the transaction in Version 1?',
        min=0, max=100)
    Child_equality_SOB = models.IntegerField(
        label='What percentage of people chose to ban the transaction in Version 2?',
        min=0, max=100)
# Functions
def variables_for_template(player, Page_number, Attention_check=False):
    current_vignette_full_name = player.participant.Vignette_order[Page_number] #e.g. Baby_inequality
    current_vignette = current_vignette_full_name.split("_")[0] #e.g. Baby
    
    vignette_characteristics = C.vignette_characteristics.copy().transpose()
    vignette_characteristics = vignette_characteristics[vignette_characteristics.iloc[:,0] == current_vignette]

    labels_for_table = {
        'transaction': vignette_characteristics.loc[current_vignette_full_name,'Transaction'], 
        'transaction_price': vignette_characteristics.loc[current_vignette_full_name,'Transaction price'], 
        'seller': vignette_characteristics.loc[current_vignette_full_name,'Seller'], 
        'seller_incomev1': vignette_characteristics.loc[current_vignette_full_name,'Sellers household income'], 
        'seller_incomev2': vignette_characteristics.loc[current_vignette_full_name,'Sellers household income'], 
        'buyer': vignette_characteristics.loc[current_vignette_full_name,'Buyer'], 
        'buyer_incomev1': vignette_characteristics.loc[current_vignette_full_name,'Buyers household income'],  
        'buyer_incomev2': vignette_characteristics.loc[current_vignette_full_name,'Buyers household income'],  
    }
        
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
    form_fields = ['Child_inequality_SOB', 'Child_equality_SOB'] #TODO: make this dynamic and randomize.
        
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
    Introduction_SOB,
    Page1, Page2, Page3, Page4, Page5, Page6, Page7, Page8,
    ]
