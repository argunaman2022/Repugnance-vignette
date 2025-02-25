from otree.api import *
import random


#TODO: make sure there are no quotas. We'll create two experiments in prolific
#TODO: Pilot: check treatment balance

class C(BaseConstants):
    NAME_IN_URL = 'Introduction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Max_bonus = 2 
    Base_payment = 3.4 
    Bonus = 'Placeholder' #TODO: adjust
    
    #TODO: do bonus calculation codes.
    
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

def creating_session(subsession):
    '''
    1. create the quotas for each treatment to be saved to the session variable
        - make sure that in the settings.py file the SESSION_FIELDS has initialized the session variables
    2. These quotas are initially zero but as participants are assigned they are incremented. 
    - It is important to note that although prolific ensures gender balanced sample,
        we need this balancing to be within treatment level also
    '''
        # people in v_1_first see the first version of the vignettes first.

    subsession.session.Treatment_quotas = C.quotas.copy()

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Demographics
    prolific_id = models.StringField(default=str("None")) #prolific id, will be fetched automatically.
   

    'Comprehension and attention checks'
    #whether the player got the comprehension questions rigt at the first try
    Comprehension_1 = models.BooleanField(initial=True) 
    #In the first comprehension check, the questions the player has answered wrong are stored as a string below.
    Comprehension_wrong_answers = models.StringField(initial='') 
    Comprehension_2 = models.BooleanField(initial=True) 
    
    Comprehension_question_1 = models.BooleanField(choices=[
            [True,f'I will receive a fixed payment of {C.Base_payment} and a bonus payment that will be determined only by my answers in Part II.'], # Correct answer here
            [False, f'I will receive a fixed payment of {C.Base_payment} and a bonus payment that will be determined by my answers in Part I and Part II.'],
            [False, f'I will receive a fixed payment of {C.Base_payment} only. '],],
        label = 'How is your <strong>Payment</strong> determined?',
        widget=widgets.RadioSelect,)
        
    Comprehension_question_2 = models.BooleanField(choices=[
            [False, 'In Part I, there are correct and incorrect answers. My bonus in this part depends on the correctness of my answer.'],
            [True,'In Part I, there is no right or wrong answer. I need to answer with my honest opinions. '], 
            [False, 'In Part I, there are correct and incorrect answers. My bonus in this part does not depend on correctness of my answer.'],],
        label = f'Which of the following is true for <strong>Part I</strong>?',
        widget=widgets.RadioSelect,)

    Comprehension_question_3 = models.BooleanField(choices=[
            [True,'In Part II, I will see the same situations as in Part I. Here my bonus is determined by the correctness  of my answer.'], 
            [False, 'In Part II, there is no right or wrong answer. I need to answer with my honest opinions. '],
            [False, 'In Part II, I will see situations I have not seen in Part I. My bonus in this part depends on the correctness of my answers.'],],
        label = f'Which of the following is true for <strong>Part II</strong>?',
        widget=widgets.RadioSelect,)
    
    Honesty = models.StringField(choices=['Yes', 'No', 'I cannot promise'],
        label = f'Do you <strong>agree</strong> to be careful and provide your best answers? <br>Please be honest. Your answer will not affect your payment. ',
        widget=widgets.RadioSelect,)
    
    Payment_button = models.IntegerField(initial=0)
    
    Attention_1 = models.BooleanField(choices=[
            [False, 'USA'],
            [False, 'Canada'],
            [False, 'Mexico'],
            [False, 'Austria'],
            [False, 'Germany'],
            [False, 'Switzerland'],
            [True, 'Russia'], 
            [False, 'India'], ],
        label='Choose the country that was described in the instructions.',
        widget=widgets.RadioSelect,)
    
#%% Functions
def treatment_assignment(player):
    session=player.subsession.session
    Quotas = session.Treatment_quotas
    
    '''
    Quota/Treatment assignment works as follows:
    1. get the current quotas
    2. assign a random treatment from the bottom half of the quotas (i.e. the treatment with the lowest quota)
    3. update quotas accordingly.
    Then 
    4. shuffle the vignettes.
    5. depending on the treatment i.e. (inequality or equality) add the suffix _treatment to the vignette names
    6. save the vignette order to the participant level
    '''
    treatment = random.choice([key for key, value in Quotas.items() if value in sorted(Quotas.values())[:1]])
    player.participant.Treatment = treatment
    Quotas.update({treatment: Quotas[treatment]+1})
    
    vignette_labels_order = C.Vignette_labels.copy()  #i.e. ['Child', 'Kidney', 'Waste','Baby']

    random.shuffle(vignette_labels_order)
    player.participant.vars['Vignette_order'] = ['kidney'] + vignette_labels_order
    
    print(f"Player {player.id_in_group} is assigned to {treatment} treatment, his vignette order is {player.participant.vars['Vignette_order']}")

            
#%% PAGES
# Consent, Demographics, Introduction, Comprehension checks and attention check 1
class Consent(Page):   
    @staticmethod
    def before_next_page(player: Player, timeout_happened=False):
        player.prolific_id = player.participant.label #save prolific id
        treatment_assignment(player) #assign treatment and update quotas 
    

class Instructions(Page):
    form_model = 'player'
    form_fields = ['Payment_button']
    @staticmethod
    def vars_for_template(self):
        return {'Instructions': C.Instructions_path}
    
    @staticmethod   
    def before_next_page(player: Player, timeout_happened=False):
        player.participant.vars['Allowed']=True
        
class Honesty(Page):
    form_model = 'player'
    form_fields = ['Honesty']
    @staticmethod
    def vars_for_template(self):
        return {'Instructions': C.Instructions_path}

        
class Attention_1(Page):
    form_model = 'player'
    form_fields = ['Attention_1']
    
    @staticmethod
    def vars_for_template(player: Player):
        return {'Instructions': C.Instructions_path}
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened=False):
        if not player.Attention_1:
            player.participant.vars['Attention_1'] = False
        else:
            player.participant.vars['Attention_1'] = True
    

    
# class Comprehension_check_1(Page):
#     form_model = 'player'
#     form_fields = ['Comprehension_question_1', 'Comprehension_question_2', 'Comprehension_question_3']
    
#     @staticmethod
#     def vars_for_template(player: Player):
#         return {'Instructions': C.Instructions_path}

#     @staticmethod   
#     def before_next_page(player: Player, timeout_happened=False):
#         player_passed_comprehension = player.Comprehension_question_1 and player.Comprehension_question_2 and player.Comprehension_question_3
#         # if player has answered a question wrong then I save it in a string
#         wrong_answers = ''
#         if not player.Comprehension_question_1:
#             player.Comprehension_question_1 = None #reset player answer so it doesnt show up in the next page
#             wrong_answers+= 'first question'
#         if not player.Comprehension_question_2:
#             if not wrong_answers =='': wrong_answers += ', '
#             player.Comprehension_question_2 = None
#             wrong_answers+= 'second question'
#         if not player.Comprehension_question_3:
#             if not wrong_answers =='': wrong_answers += ', '
#             player.Comprehension_question_3 = None
#             wrong_answers+= 'third question'
        
#         player.Comprehension_wrong_answers = wrong_answers
#         player.Comprehension_1 = player_passed_comprehension
#         # save at the participant level
#         if player_passed_comprehension:
#             player.participant.vars['Comprehension_passed'] = True
#             player.participant.vars['Allowed']=True
#         else: 
#             player.participant.vars['Allowed']=False
        
# class Comprehension_check_2(Page):
#     form_model = 'player'
#     form_fields = ['Comprehension_question_1', 'Comprehension_question_2', 'Comprehension_question_3']
    
#     @staticmethod
#     def vars_for_template(player: Player):
#         return {'Instructions': C.Instructions_path}
    
#     @staticmethod
#     def is_displayed(player: Player):
#         return not player.Comprehension_1  #display only if player failed on first try
    
#     @staticmethod
#     def vars_for_template(player: Player):
#         return {'Comprehension_wrong_answers':  player.Comprehension_wrong_answers,
#                 'Instructions': C.Instructions_path}

#     @staticmethod   
#     def before_next_page(player: Player, timeout_happened=False):
#         player_passed_comprehension = (player.Comprehension_question_1 and
#                                        player.Comprehension_question_2 and player.Comprehension_question_3)
#         #failing two compr. checks player is not allowed to continue
#         player.participant.Allowed = player_passed_comprehension
#         player.Comprehension_2 = player_passed_comprehension
#         # save at the participant level if they passed
#         if player_passed_comprehension:
#             player.participant.vars['Comprehension_passed'] = True
#             player.participant.vars['Allowed']=True
#         else:
#             player.participant.vars['Allowed']=False
#             player.participant.vars['Comprehension_passed'] = False



page_sequence = [Consent, Instructions, Honesty, Attention_1,
                 ]