from otree.api import *
import random
#import all functions from vignettes.py 

doc = '''
This is the main survey app. It contains
1. Main survey 
2. One attention check.
- You can additionally calculate payoffs and save them at a participant field.
'''
# names
def generate_name():
    #TODO for now only Sam and Bob
    return 'Sam', 'Bob'

#TODO: make sure all the sliders work with darkening the text
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
    
    all_vignettes = ['loan_shark', 'kidney', 'surrogate', 'queue_jump', 'prostitute', 'dwarf_tossing', 'waste_trade', 'coin_collector']
    
    #TODO: i have changed the exploit question, check if it is ok.
    #Slider_label_exploit = 'In your opinion, does this transaction <strong>benefit or exploit person A</strong>?'
    #TODO: make sure names are consistent
    Slider_label_exploit = f'What do you think about the following statement: "<strong>this transaction exploits {generate_name()[0]}</strong>"?'
    Slider_label_autonomy = 'In your opinion, does this transaction <strong>respect or limit individual autonomy (i.e. self-determination)</strong>?'
    Slider_label_coercion = 'In your opinion, does this transaction allow the person A <strong> to make fully informed choices or does it exert undue influence</strong>?'
    Slider_label_fairA = f'In your opinion, is this transaction <strong>fair or unfair to {generate_name()[0]}</strong>?'
    # Slider_label_fairB = 'In your opinion, is this transaction <strong>fair or unfair to person B </strong>?'
    Slider_label_dignity = 'In your opinion, does this transaction <strong>promote or violate human dignity</strong>?'
    Slider_label_ban = 'To what extend do you agree with the following statement: <strong>"this transaction should be prevented"</strong>?'
    Slider_label_disapprove = 'To what extend do you disapprove of this transaction?'
    
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
        
    Attention_check = '''
    There are no seller or buyer in this situation. It is important to us that you are reading these vignettes carefully. We use what are called "attention checks" to measure whether are paying attention. 
    This is one such attention check. To complete this attention check all you need to do is to move all the sliders all the way to the right and click "Next" to continue.
    Please move all the sliders below all the way to the right and continue.
    '''
    
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):   
    # Attention check 2, 1 was in introduction 
    Attention_2 = models.BooleanField()
            
    # Player answers
    ## Survey
    ## Loan shark
    loan_shark_exploit = models.FloatField(blank=False, min=-10)
    loan_shark_autonomy = models.FloatField(blank=False, min=-10)
    loan_shark_coercion = models.FloatField(blank=False, min=-10)
    loan_shark_fairA = models.FloatField(blank=False, min=-10)
    loan_shark_dignity = models.FloatField(blank=False, min=-10)
    loan_shark_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    
    ### Kidney market
    kidney_exploit = models.FloatField(blank=False, min=-10)
    kidney_autonomy = models.FloatField(blank=False, min=-10)
    kidney_coercion = models.FloatField(blank=False, min=-10)
    kidney_fairA = models.FloatField(blank=False, min=-10)
    kidney_dignity = models.FloatField(blank=False, min=-10)
    kidney_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    
    ### surrogate
    surrogate_exploit = models.FloatField(blank=False, min=-10)
    surrogate_autonomy = models.FloatField(blank=False, min=-10)
    surrogate_coercion = models.FloatField(blank=False, min=-10)
    surrogate_fairA = models.FloatField(blank=False, min=-10)
    surrogate_dignity = models.FloatField(blank=False, min=-10)
    surrogate_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    
    ### Queue jump
    queue_jump_exploit = models.FloatField(blank=False, min=-10)
    queue_jump_autonomy = models.FloatField(blank=False, min=-10)
    queue_jump_coercion = models.FloatField(blank=False, min=-10)
    queue_jump_fairA = models.FloatField(blank=False, min=-10)
    queue_jump_dignity = models.FloatField(blank=False, min=-10)
    queue_jump_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    
    ### Prostitute
    prostitute_exploit = models.FloatField(blank=False, min=-10)
    prostitute_autonomy = models.FloatField(blank=False, min=-10)
    prostitute_coercion = models.FloatField(blank=False, min=-10)
    prostitute_fairA = models.FloatField(blank=False, min=-10)
    prostitute_dignity = models.FloatField(blank=False, min=-10)
    prostitute_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    
    ### Dwarf tossing
    dwarf_tossing_exploit = models.FloatField(blank=False, min=-10)
    dwarf_tossing_autonomy = models.FloatField(blank=False, min=-10)
    dwarf_tossing_coercion = models.FloatField(blank=False, min=-10)
    dwarf_tossing_fairA = models.FloatField(blank=False, min=-10)
    dwarf_tossing_dignity = models.FloatField(blank=False, min=-10)
    dwarf_tossing_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    
    
    ### Waste trade
    waste_trade_exploit = models.FloatField(blank=False, min=-10)
    waste_trade_autonomy = models.FloatField(blank=False, min=-10)
    waste_trade_coercion = models.FloatField(blank=False, min=-10)
    waste_trade_fairA = models.FloatField(blank=False, min=-10)
    waste_trade_dignity = models.FloatField(blank=False, min=-10)
    waste_trade_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    
    ### Coin collector
    coin_collector_exploit = models.FloatField(blank=False, min=-10)
    coin_collector_autonomy = models.FloatField(blank=False, min=-10)
    coin_collector_coercion = models.FloatField(blank=False, min=-10)
    coin_collector_fairA = models.FloatField(blank=False, min=-10)
    coin_collector_dignity = models.FloatField(blank=False, min=-10)
    coin_collector_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    
    
    
    
    
    
    
#%%      Functions


# vignettes
def return_vignette(vignette, treatment, income_seller=False, income_buyer=False, name_seller=generate_name()[0], name_buyer=generate_name()[1]):
    assert treatment in ['poor_poor', 'poor_rich', 'rich_rich'], 'treatment not found'
    assert vignette in ['loan_shark', 'kidney', 'surrogate', 'queue_jump', 'prostitute', 'dwarf_tossing', 'waste_trade', 'coin_collector'], 'vignette not found'

    vignette = vignette.lower()
    treatment = treatment.lower()
    #TODO: change names
    if treatment == 'poor_poor':
        income_seller = '15.000'
        income_buyer = '15.000'
    elif treatment == 'poor_rich':
        income_seller = '15.000'
        income_buyer = '120.000'
    elif treatment == 'rich_rich':
        income_seller = '120.000'
        income_buyer = '120.000'  
        
    
    
    if vignette == 'loan_shark':
        text = f''' 
        <strong>Loansharking</strong>. A loan shark is an individual who provides loans with exorbitant interest rates and harsh collection tactics.
        Loansharking is characterized by high weekly interest rates around 20%.
        While traditional banks may have processing times of several days to weeks, loan sharks can provide fund within a day, appealing to those in urgent need of funds.
        <br><br>
        {name_seller} is a 30-year-old man. His annual income is  <strong>{income_seller}$</strong>.
        {name_buyer} is a 45 year old man. His income is <strong>{income_buyer}$</strong>. {name_seller}'s teenager son is diagnosed with <strong>a rare life threatening tumor</strong>.
        If the tumor is removed he has a chance to live but it needs to be done immediately. 
        The only capable surgeon who is available in such a short-notice requires an upfront payment.
        {name_seller} sells all assets that can be sold quickly in a week but he is short of $100,000 to cover the payment.
        Although traditional banks offer a weekly interest rates of 5%, due to long processing times they are not an option.
        {name_seller} and {name_seller} come to the following agreement: {name_seller} will lend {name_seller} the missing sum for one month with an interest rate of 50%.
        '''           
    elif vignette == 'kidney':
        text = f''' 
        <strong>Kidney transplant</strong>. Advances in surgery and medication make living kidney donation a successful treatment for end-stage kidney disease.
        In this process, an individual with two healthy kidneys undergoes surgical removal of one kidney.
        This kidney is then transplanted into the recipient, restoring kidney function.
        Individuals can live healthy and fulfilling lives with a single kidney.
        In the USA more than 90.000 people are on the waiting list for a kidney donation.
        Although there are a lot of donors, roughly 13 people die waiting for a transplant every day.
        A controversial idea is allowing people to sell/buy kidneys to reduce this number.
        <br><br>
        
        {name_seller} is a 40-year-old man. His annual income is <strong>{income_seller}$</strong>$.
        {name_buyer} is a 40-year-old man, his annual income is <strong>{income_buyer}$</strong>$. Due to final-stage kidney disease, {name_buyer} urgently needs a replacement kidney.
        {name_seller} and {name_buyer} come to the following agreement: {name_seller} will sell one of his kidneys to {name_buyer}.
        '''
    elif vignette == 'surrogate':
        text = f''' 
        <strong>Gestational Surrogacy</strong>. Gestational surrogacy is a useful medical technique for certain infertilities.
        It allows a woman to have a child through another woman's pregnancy. Doctors fertilize her egg in a lab and implant it in a surrogate mother. 
        The surrogate carries the baby with a legal agreement ensuring the genetic mother receives the child after birth.
        <br><br>
        
        {name_seller} is a 29 year old single woman. Her annual income is <strong>{income_seller}$</strong>$. {name_seller} is a 42 year old single woman.
        Her annual income is <strong>{income_buyer}$</strong>$. {name_seller} wants to have a baby but is infertile. Since she wants to be the genetic mother of the child,
        adopting a baby is not an option for her. {name_seller} and B come to the following agreement: {name_seller} will pay {name_seller} to be a surrogate mother for her child.
        This means {name_seller} will be pregnant with {name_seller}'s baby and upon delivery the baby will be given to {name_seller}. 
        '''
    elif vignette == 'queue_jump':
        text = f''' 
        <strong>Line stander</strong>. Congressional hearings are usually open to the public. Any U.S. citizen is welcomed to observe the sessions.
        Seating, however, is limited and operates on a first-come-first-serve basis. As a result, attendees may need to queue to secure entry to the hearings. 
        This has led to the business of line-standing. Individuals are paid to stand in the queue and exchange their positions with the buyer before the scheduled event. 
        <br><br>
        
        {name_seller} is a 42 year old man. His annual income is <strong>{income_seller}$</strong>$. {name_buyer} is a 35 year old man. His annual income is <strong>{income_buyer}$</strong>$.
        An important congressional hearing is planned that {name_buyer} wants to attend.
        This hearing is drawing a lot of public interest and so lots of people will be queuing for the limited seats. {name_buyer} and A come to the following agreement:
        {name_buyer} will pay {name_seller} to stand in queue for him for 20 hours. Right before it is {name_seller}'s turn to go in {name_buyer} will come and take his place.
        '''
    elif vignette == 'prostitute':
        text = f''' 
        {name_seller} is a 27 year old woman. Her annual income is <strong>{income_seller}$</strong>$.
        {name_buyer} is a 45 year old man. His annual income is <strong>{income_buyer}$</strong>$.
        One day he notices her and wants to have a one time no-strings-attached sexual encounter with her.
        {name_buyer} and A come to the following agreement: B will pay {name_seller} to have sex with him in a safe, pre-arranged place of her choosing. 
        '''
    elif vignette == 'dwarf_tossing':
        text = f''' 
        <strong>Dwarf tossing</strong>. Dwarf tossing is an activity in which people with dwarfism (little people of around 4ft height)
        are thrown onto mattresses or at Velcro-coated walls.
        They are wearing special padded clothing or Velcro costumes. Participants compete to throw the person with dwarfism the farthest.
        <br><br>
        
        {name_seller} is a 28 year old man with dwarfism. His annual income is <strong>{income_seller}$</strong>$. {name_buyer} is a 45 year old man.
        His annual income is <strong>{income_buyer}$</strong>$.
        On the internet, {name_buyer} reads about the concept of "dwarf tossing" and decides to organize such a competition for a friend's birthday party as a gift.
        {name_buyer} and A come to the following agreement: B will pay A to be the dwarf that will be tossed in the competition.
        '''
    elif vignette == 'waste_trade':
        text = f''' 
        <strong>Waste trade</strong>. Global waste trade refers to the cross-border exchange of waste between countries,
        with the aim of additional treatment, disposal, or recycling. Developing nations frequently import toxic or hazardous wastes from more economically developed countries.
        The United States, for example, ranks as the sixth-largest exporter of plastic waste, with an export volume totaling 437,480 metric tons.
        <br><br>
        
        Country A is a medium-sized nation with an average annual income of <strong>{income_seller}$</strong>$ per person.
        Country B, a medium-sized country with an average annual income of <strong>{income_buyer}$</strong>$ per person,
        generates a substantial volume of consumer-products waste. Country B and A come to the following agreement: B will pay Country A to dispose of 20 million tonnes (approximately 22 billion pounds) of this waste.
        This waste will be buried in Country A's landfills.
        '''
    elif vignette == 'coin_collector':
        text = f''' 
        <strong>Unburied treasures</strong>. In some U.S states items found while digging in private property belongs to the owner.
        Some such items, while not initially valuable, can gain worth over time due to the interest of collectors, such as those specializing in coins.
        <br><br>
        
        {name_seller} is a 40 year old man. His annual income is <strong>{income_seller}$</strong>$.
        {name_buyer} is a 40 year old man. His annual income is <strong>{income_buyer}$</strong>$. One of his hobbies is coin collecting.
        While digging in his backyard {name_seller} finds an old U.S quarter. {name_seller} and B come to the following agreement: {name_seller} will sell the coin to {name_buyer}. 
        '''

                 
    else: text = 'Vignette not found'
        
    return text


def variables_for_template(player, Page_number, Attention_check=False):
    current_vignette = player.participant.Vignette_order[Page_number]
    labels_for_sliders = {
        'exploit': C.Slider_label_exploit, 
        'autonomy': C.Slider_label_autonomy,
        'coercion': C.Slider_label_coercion,
        'fairA': C.Slider_label_fairA,
        'dignity': C.Slider_label_dignity,
        'disapproval': C.Slider_label_disapprove,
        'ban': C.Slider_label_ban,
    }
        
    if current_vignette =='waste_trade':
        labels_for_sliders = {
        'exploit': C.Slider_label_country_exploit,
        'autonomy': C.Slider_label_country_autonomy,
        'coercion': C.Slider_label_country_coercion,
        'fairA': C.Slider_label_country_fairA,
        'dignity': C.Slider_label_country_dignity,
        'ban': C.Slider_label_country_ban,         
        }
        
    label = current_vignette+'_'+player.participant.Treatment
    vignette_text = return_vignette(current_vignette, player.participant.Treatment)
    
    if not Attention_check:
        return {'Instructions': C.Instructions_path,
                'Vignette': current_vignette,
                # 'Vignette_text': vignette_text,
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
  
#%% 
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
