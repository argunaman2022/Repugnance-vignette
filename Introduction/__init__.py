from otree.api import *
import random

doc = '''
This is the first app - the Introduction app. It contains
1. Demgraphics page
2. Instructions that participants can always access
3. Comprehension checks 
4. and the first attention checks
Following are saved to the participant level
- Allowed: if they didnt fail the comprehension checks
- Comprehension_passed: whether they passed the comprehension checks
- Attention_1: whether they passed the first attention check
- Treatment: which treatment they are assigned to
'''

class C(BaseConstants):
    NAME_IN_URL = 'Introduction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Instructions_path = "_templates/global/Instructions.html"
    
    # Treatment quotas
    quotas = {
    'inequality_first': 0,
    'equality_first' : 0,
    }
    
    # there are 4 vignettes with 2 versions each vignette_inequality and vignette_equality
    Vignette_labels = ['Child', 'Kidney', 'Waste','Baby']
    
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
    age = models.IntegerField(label="Age", min=18, max=100)
    gender = models.StringField(label='Gender',
                                choices=['Male', 'Female', 'Transgender male','Transgender female', 'Other/Prefer not to say'], widget=widgets.RadioSelect)
    education = models.StringField(label = 'Education level',
                                   choices=['High school or lower','Bachelors degree','Masters degree','PhD','Other'], widget=widgets.RadioSelect) 
    income = models.StringField(label='Gross annual income',
                            choices=['0 - 25.000 USD', '25.000 - 50.000 USD', '50.000 - 75.000 USD', '75.000 - 100.000 USD','> 100.000 USD'], widget=widgets.RadioSelect)

    'Comprehension and attention checks'
    #whether the player got the comprehension questions rigt at the first try
    Comprehension_1 = models.BooleanField(initial=True) 
    #In the first comprehension check, the questions the player has answered wrong are stored as a string below.
    Comprehension_wrong_answers = models.StringField(initial='') 
    Comprehension_2 = models.BooleanField(initial=True) 
    
    Comprehension_question_1 = models.BooleanField(choices=[
            [True,'Correct answer'], # Correct answer here
            [False, 'False answer'],
            [False, 'False answer'],],
        label = 'Comprehension question 1',
        widget=widgets.RadioSelect)
    Comprehension_question_2 = models.BooleanField(choices=[
            [True,'Correct answer'], 
            [False, 'False answer'],
            [False, 'False answer'],],
        label = 'Comprehension question 1',
        widget=widgets.RadioSelect)
    Comprehension_question_3 = models.BooleanField(choices=[
            [True,'Correct answer'], 
            [False, 'False answer'],
            [False, 'False answer'],],
        label = 'Comprehension question 1',
        widget=widgets.RadioSelect)
    
    Attention_1 = models.BooleanField(choices=[
            [False, 'Austria'],
            [False, 'Germany'],
            [False, 'Switzerland'],
            [True, 'Russia'], 
            [False, 'India'] ],
        label='<strong>Choose the country that was described in the instructions.</strong>',
        widget=widgets.RadioSelect)
    
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
    5. depending on the treatment i.e. (inequality_first or equality_first) add the suffix _treatment to the vignette names
    6. save the vignette order to the participant level
    '''
    treatment = random.choice([key for key, value in Quotas.items() if value in sorted(Quotas.values())[:1]])
    player.participant.Treatment = treatment
    Quotas.update({treatment: Quotas[treatment]+1})
    
    vignette_labels_order = C.Vignette_labels.copy() 
    # player.participant.vars['Vignette_order'] = [
    #         vignette_labels_order[0]+'_inequality', vignette_labels_order[1]+'_inequality', vignette_labels_order[2]+'_inequality',vignette_labels_order[3]+'_inequality',
    #         vignette_labels_order[0]+'_equality',vignette_labels_order[1]+'_equality', vignette_labels_order[2]+'_equality', vignette_labels_order[3]+'_equality']
    
    random.shuffle(vignette_labels_order)
    if treatment == 'inequality_first':
        player.participant.vars['Vignette_order'] = [
            vignette_labels_order[0]+'_inequality', vignette_labels_order[1]+'_inequality', vignette_labels_order[2]+'_inequality',vignette_labels_order[3]+'_inequality',
            vignette_labels_order[0]+'_equality',vignette_labels_order[1]+'_equality', vignette_labels_order[2]+'_equality', vignette_labels_order[3]+'_equality']
    elif treatment == 'equality_first':
            player.participant.vars['Vignette_order'] = [
                vignette_labels_order[0]+'_equality',vignette_labels_order[1]+'_equality', vignette_labels_order[2]+'_equality', vignette_labels_order[3]+'_equality',
                vignette_labels_order[0]+'_inequality', vignette_labels_order[1]+'_inequality', vignette_labels_order[2]+'_inequality',vignette_labels_order[3]+'_inequality',]
    print(f"Player {player.id_in_group} is assigned to {treatment} treatment, his vignette order is {player.participant.vars['Vignette_order']}")

            
#%% PAGES
# Demographics, Introduction, Comprehension checks and attention check 1
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'income']
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened=False):
        player.prolific_id = player.participant.label #save prolific id
        treatment_assignment(player) #assign treatment and update quotas 
    
class Instructions(Page):
    @staticmethod
    def vars_for_template(self):
        return {'Instructions': C.Instructions_path}
    
class Comprehension_check_1(Page):
    form_model = 'player'
    form_fields = ['Comprehension_question_1', 'Comprehension_question_2', 'Comprehension_question_3']
    
    @staticmethod
    def vars_for_template(player: Player):
        return {'Instructions': C.Instructions_path}

    @staticmethod   
    def before_next_page(player: Player, timeout_happened=False):
        player_passed_comprehension = player.Comprehension_question_1 and player.Comprehension_question_2 and player.Comprehension_question_3
        # if player has answered a question wrong then I save it in a string
        wrong_answers = ''
        if not player.Comprehension_question_1:
            player.Comprehension_question_1 = None #reset player answer so it doesnt show up in the next page
            wrong_answers+= 'first question'
        if not player.Comprehension_question_2:
            if not wrong_answers =='': wrong_answers += ', '
            player.Comprehension_question_2 = None
            wrong_answers+= 'second question'
        if not player.Comprehension_question_3:
            if not wrong_answers =='': wrong_answers += ', '
            player.Comprehension_question_3 = None
            wrong_answers+= 'third question'
        
        player.Comprehension_wrong_answers = wrong_answers
        player.Comprehension_1 = player_passed_comprehension
        # save at the participant level
        if player_passed_comprehension:
            player.participant.vars['Comprehension_passed'] = True
            player.participant.vars['Allowed']=True
        else: 
            player.participant.vars['Allowed']=False
        
class Comprehension_check_2(Page):
    form_model = 'player'
    form_fields = ['Comprehension_question_1', 'Comprehension_question_2', 'Comprehension_question_3']
    
    @staticmethod
    def vars_for_template(player: Player):
        return {'Instructions': C.Instructions_path}
    
    @staticmethod
    def is_displayed(player: Player):
        return not player.Comprehension_1  #display only if player failed on first try
    
    @staticmethod
    def vars_for_template(player: Player):
        return {'Comprehension_wrong_answers':  player.Comprehension_wrong_answers,
                'Instructions': C.Instructions_path}

    @staticmethod   
    def before_next_page(player: Player, timeout_happened=False):
        player_passed_comprehension = (player.Comprehension_question_1 and
                                       player.Comprehension_question_2 and player.Comprehension_question_3)
        #failing two compr. checks player is not allowed to continue
        player.participant.Allowed = player_passed_comprehension
        player.Comprehension_2 = player_passed_comprehension
        # save at the participant level if they passed
        if player_passed_comprehension:
            player.participant.vars['Comprehension_passed'] = True
            player.participant.vars['Allowed']=True
        else:
            player.participant.vars['Allowed']=False
            player.participant.vars['Comprehension_passed'] = False

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


page_sequence = [Demographics, Instructions,
                 Comprehension_check_1, Comprehension_check_2,
                 Attention_check_1]