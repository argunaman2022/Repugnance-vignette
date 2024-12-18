from otree.api import *
import random
import numpy as np
#import all functions from vignettes.py 

doc = '''
This is the main survey app. It contains
1. Main survey 
2. One attention check.
- You can additionally calculate payoffs and save them at a participant field.
'''

class C(BaseConstants):
    NAME_IN_URL = 'Scenarios'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Instructions_path = "_templates/global/Instructions.html"
    Quit_study_text_path = "_templates/global/Quit_study_text.html"
    Return_redirect = "https://www.wikipedia.org/" 
    
    all_vignettes = ['loan_shark', 'kidney', 'surrogate', 'queue_jump', 'prostitute', 'dwarf_tossing', 'waste_trade', 'coin_collector', 'apple_seller']
    
    # pictures
    loan_shark_picture = "https://raw.githubusercontent.com/argunaman2022/Repugnance-vignette/refs/heads/master/_static/pictures/loan_shark.jpg"
    kidney_picture = "https://raw.githubusercontent.com/argunaman2022/Repugnance-vignette/refs/heads/master/_static/pictures/kidney.png"
    surrogate_picture = "https://raw.githubusercontent.com/argunaman2022/Repugnance-vignette/refs/heads/master/_static/pictures/Surrogacy.png"
    queue_jump_picture = "https://raw.githubusercontent.com/argunaman2022/Repugnance-vignette/refs/heads/master/_static/pictures/queue_jump.jpg"
    prostitute_picture = ''#"https://raw.githubusercontent.com/argunaman2022/Repugnance-vignette/refs/heads/master/_static/pictures/Surrogacy.png?token=GHSAT0AAAAAAC3RHEJI55UNQG6IA3KK5O56Z3CUSXQ"
    dwarf_tossing_picture = ''#"https://raw.githubusercontent.com/argunaman2022/Repugnance-vignette/refs/heads/master/_static/pictures/Surrogacy.png?token=GHSAT0AAAAAAC3RHEJI55UNQG6IA3KK5O56Z3CUSXQ"
    waste_trade_picture = ''#"https://raw.githubusercontent.com/argunaman2022/Repugnance-vignette/refs/heads/master/_static/pictures/Surrogacy.png?token=GHSAT0AAAAAAC3RHEJI55UNQG6IA3KK5O56Z3CUSXQ"
    coin_collector_picture = "https://raw.githubusercontent.com/argunaman2022/Repugnance-vignette/refs/heads/master/_static/pictures/coin_seller.png"
    apple_seller_picture = "https://raw.githubusercontent.com/argunaman2022/Repugnance-vignette/refs/heads/master/_static/pictures/apple_seller.jpg"
    
    
    # slider labels    
    Slider_label_exploit = f'What do you think about the following statement: "<strong>this transaction exploits Bob</strong>"?'
    Slider_label_autonomy = 'In your opinion, does this transaction <strong>respect or limit individual autonomy (i.e. self-determination)</strong>?'
    Slider_label_coercion = 'In your opinion, does this transaction allow the person A <strong> to make fully informed choices or does it exert undue influence</strong>?'
    Slider_label_fairA = f'In your opinion, is this transaction <strong>fair or unfair to Sam</strong>?'
    Slider_label_dignity = 'In your opinion, does this transaction <strong>promote or violate human dignity</strong>?'
    Slider_label_harm = 'What do you think about the following statement: <strong>"allowing such transactions would harm society in the long run"</strong>?'

    # for imagined health
    Slider_label_health = 'In this scenario, how healthy do you imagine Sam (the seller of kidney) to be?'

    # for realism
    Slider_label_realism = 'In your opinion, how realistic is this scenario?'

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
    Attention_2 = models.BooleanField(label='What do you think: In which range is the proportion located?',
                                      choices=[[False, '0-20%'],
                                        [True,'21-40%'], 
                                        [False, '41-60%'],
                                        [False, '61-80%'],
                                        [False, '81-100%'],],
                                      widget=widgets.RadioSelectHorizontal)
                                        
    # Player answers
    ## ban and beliefs
    kidney_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    kidney_beliefs = models.FloatField(blank=True) #1 yes/ban 0 no/dont ban
    surrogate_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    surrogate_beliefs = models.FloatField(blank=True) #1 yes/ban 0 no/dont ban
    queue_jump_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    queue_jump_beliefs = models.FloatField(blank=True) #1 yes/ban 0 no/dont ban
    prostitute_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    prostitute_beliefs = models.FloatField(blank=True) #1 yes/ban 0 no/dont ban
    dwarf_tossing_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    dwarf_tossing_beliefs = models.FloatField(blank=True) #1 yes/ban 0 no/dont ban
    waste_trade_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    waste_trade_beliefs = models.FloatField(blank=True) #1 yes/ban 0 no/dont ban
    coin_collector_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    coin_collector_beliefs = models.FloatField(blank=True) #1 yes/ban 0 no/dont ban
    loan_shark_ban = models.IntegerField() #1 yes/ban 0 no/dont ban
    loan_shark_beliefs = models.FloatField(blank=True) #1 yes/ban 0 no/dont ban
    apple_seller_ban = models.IntegerField() #1 yes/ban 0 no/dont ban      
    apple_seller_beliefs = models.FloatField(blank=True) #1 yes/ban 0 no/dont ban     
    
    ## moral dims
    kidney_exploit = models.FloatField(blank=True, min=-10)
    kidney_autonomy = models.FloatField(blank=True, min=-10)
    kidney_coercion = models.FloatField(blank=True, min=-10)
    kidney_fairA = models.FloatField(blank=True, min=-10)
    kidney_dignity = models.FloatField(blank=True, min=-10)
    kidney_harm = models.FloatField(blank=True, min=-10) 
    
    ## Imagined
    kidney_imagined_price = models.FloatField(blank=False, min=0, label='In this scenario, what do you imagine the agreed-upon price to be (in dollars)?')
    kidney_imagined_health = models.FloatField(blank=True, min=-10) 
    
    
    ## Scenarios
    scenario_directionality_1_ban = models.StringField(label='',
                                                       choices=['Yes','No'], widget=widgets.RadioSelectHorizontal ) #1 yes/ban 0 no/dont ban
    scenario_directionality_2_ban = models.StringField(label='',
                                                       choices=['Yes','No'], widget=widgets.RadioSelectHorizontal ) #1 yes/ban 0 no/dont ban
    scenario_directionality_1_realism = models.FloatField( min=-10) 
    scenario_directionality_2_realism = models.FloatField( min=-10) 
    scenario_directionality_1_realism_free_text = models.LongStringField(label='(Please write 2 sentences)',) 
    scenario_directionality_2_realism_free_text = models.LongStringField(label='(Please write 2 sentences)',) 
    
    scenario_rich_1_ban = models.StringField(label='',
                                                       choices=['Yes','No'], widget=widgets.RadioSelectHorizontal ) #1 yes/ban 0 no/dont ban
    scenario_rich_2_ban = models.StringField(label='',
                                                       choices=['Yes','No'], widget=widgets.RadioSelectHorizontal ) #1 yes/ban 0 no/dont ban
    
    scenario_equality_1_ban = models.StringField(label='',
                                                       choices=['Yes','No'], widget=widgets.RadioSelectHorizontal ) #1 yes/ban 0 no/dont ban
    scenario_equality_2_ban = models.StringField(label='',
                                                       choices=['Yes','No'], widget=widgets.RadioSelectHorizontal ) #1 yes/ban 0 no/dont ban
    
    scenario_price_1_ban = models.StringField(label='',
                                                       choices=['Yes','No'], widget=widgets.RadioSelectHorizontal ) #1 yes/ban 0 no/dont ban
    scenario_price_2_ban = models.StringField(label='',
                                                       choices=['Yes','No'], widget=widgets.RadioSelectHorizontal ) #1 yes/ban 0 no/dont ban
    
    scenario_donation_1_ban = models.StringField(label='',
                                                       choices=['Yes','No'], widget=widgets.RadioSelectHorizontal ) #1 yes/ban 0 no/dont ban
    scenario_donation_2_ban = models.StringField(label='',
                                                       choices=['Yes','No'], widget=widgets.RadioSelectHorizontal ) #1 yes/ban 0 no/dont ban
    scenario_donation_1_realism = models.FloatField(min=-10)
    scenario_donation_2_realism = models.FloatField(min=-10)
#%%      Functions
def draw_and_round(lower, upper):
    number = random.uniform(lower, upper)
    number = str(round(number, 1))
    return f'{number}00'

# vignettes
def return_vignette(vignette, treatment, income_seller=False, income_buyer=False,):
    assert treatment in ['poor_poor', 'poor_rich', 'rich_rich'], 'treatment not found'

    vignette = vignette.lower()
    treatment = treatment.lower()
    if treatment == 'poor_poor':
        income_seller = draw_and_round(32,34)
        income_buyer = draw_and_round(32,34)
    elif treatment == 'poor_rich':
        income_seller = draw_and_round(32,34)
        income_buyer = draw_and_round(100,102)
    elif treatment == 'rich_rich':
        income_seller = draw_and_round(100,102)
        income_buyer = draw_and_round(100,102)
        
        

    if vignette == 'loan_shark':
        name = 'Loansharking'
        vignette_picture = C.loan_shark_picture

        text = f''' 
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <div style="flex: 1; padding-right: 20px; text-align: justify;">
                A loan shark is an individual who lends money at high interest rates, often accompanied by aggressive collection methods.
                Loansharking is characterized by exorbitant weekly interest rates, typically around 20%.
                Unlike traditional banks, which may take several days or weeks to process loans and often require proof of stable residency,
                loan sharks offer quick access to funds, making them particularly appealing to those facing urgent financial need.
            </div>
            <div style="flex: 0 0 40%; text-align: center;">
                <img src="{vignette_picture}" alt="Loansharking" style="max-width: 100%; height: 300px; margin-left: 0px;">
            </div>
        </div>

        <div style="text-align: justify; margin-top: 20px;">
            <div style="text-align: center;">
                <h5>Scenario</h5>
            </div>
            Paul is a 45-year-old man. His annual income is <strong>{income_seller}$</strong>.
            Peter is a 30-year-old man. His income is <strong>{income_buyer}$</strong>.
            Paul's son is diagnosed with a life-threatening tumor. 
            While surgery offers a chance to save his life, it must be performed immediately.
            The only available surgeon capable of performing the procedure on short notice requires an upfront payment.
            After selling all the assets he can liquidate, Paul still falls $100,000 short.
            Traditional banks, which offer weekly interest rates of 5%, are not an option due to their lengthy processing times.
            Paul and Peter come to the following agreement: 
            Peter will lend Paul the remaining amount for one month at an interest rate of 25%.
        </div>
        '''

    elif vignette == 'kidney_2':
        name = 'Kidney transplant'
        vignette_picture = C.kidney_picture

        text = f''' 
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <div style="flex: 1; padding-right: 20px; text-align: justify;">
                Advances in surgery and medication make living kidney donation a successful treatment for end-stage kidney disease.
                In this process, an individual with two healthy kidneys undergoes surgical removal of one kidney.
                This kidney is then transplanted into the recipient, restoring kidney function.
                Individuals can live healthy and fulfilling lives with a single kidney.
                In the USA, more than 90,000 people are on the waiting list for a kidney donation.
            </div>
            <div style="flex: 0 0 40%; text-align: center;">
                <img src="{vignette_picture}" alt="Kidney transplant" style="max-width: 100%; height: 300px; margin-left: 0px;">
            </div>
        </div>

        <div style="text-align: justify; margin-top: 20px;">
            <div style="text-align: center;">
                <h5>Scenario</h5>
            </div>
            Sam is a 40-year-old man. He lives in a medium-sized city and has a desk job at a logistics company. 
            Bob is a 40-year-old man. He also lives in a medium-sized but different city. He is employed at a small firm.
            Due to final-stage kidney disease, <strong>Bob urgently needs a replacement kidney</strong>. 
            Although he is on the waiting list for a kidney donation, his doctors tell him that he is not high enough 
            on the list to receive a donation in time. Sam hears about Bob's situation through word of mouth. They come to 
            the agreement that Sam will sell one of his kidneys to Bob at an agreed price.
        </div>
        '''
    elif vignette == 'kidney':
        name = 'Kidney transplant'
        vignette_picture = C.kidney_picture

        text = f''' 
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <div style="flex: 1; padding-right: 20px; text-align: justify;">
                Advances in surgery and medication make living kidney donation a successful treatment for end-stage kidney disease.
                In this process, an individual with two healthy kidneys undergoes surgical removal of one kidney.
                This kidney is then transplanted into the recipient, restoring kidney function.
                Individuals can live healthy and fulfilling lives with a single kidney.
                In the USA, more than 90,000 people are on the waiting list for a kidney donation.
            </div>
            <div style="flex: 0 0 40%; text-align: center;">
                <img src="{vignette_picture}" alt="Kidney transplant" style="max-width: 100%; height: 300px; margin-left: 0px;">
            </div>
        </div>

        <div style="text-align: justify; margin-top: 20px;">
            <div style="text-align: center;">
                <h5>Scenario</h5>
            </div>
            Sam is a 40-year-old man. He lives in a medium-sized city and has a desk job at a logistics company. He earns 
            <strong>{income_seller}$</strong> annually. 
            Bob is a 40-year-old man. He also lives in a medium-sized but different city. He is employed at a small firm 
            where he earns <strong>{income_buyer}$</strong> annually.
            Due to final-stage kidney disease, <strong>Bob urgently needs a replacement kidney</strong>. 
            Although he is on the waiting list for a kidney donation, his doctors tell him that he is not high enough 
            on the list to receive a donation in time. Sam hears about Bob's situation through word of mouth. They come to 
            the agreement that Sam will sell one of his kidneys to Bob at an agreed price.
        </div>
        '''

    elif vignette == 'surrogate':
        name = 'Gestational Surrogacy'
        vignette_picture = C.surrogate_picture

        text = f''' 
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <div style="flex: 1; padding-right: 20px; text-align: justify;">
                <strong>Gestational surrogacy</strong> is a medical solution for certain types of infertility.
                It enables a woman to have a biological child through another woman's pregnancy.
                In this process, doctors fertilize the intended mother's egg in a laboratory and implant the resulting embryo into a surrogate. 
                The surrogate carries the baby under a legal agreement, ensuring the child is handed over to the intended mother after birth.
            </div>
            <div style="flex: 0 0 40%; text-align: center;">
                <img src="{vignette_picture}" alt="Gestational surrogacy" style="max-width: 100%; height: 300px; margin-left: 0px;">
            </div>
        </div>

        <div style="text-align: justify; margin-top: 20px;">
            <div style="text-align: center;">
                <h5>Scenario</h5>
            </div>
            Samantha is a 29-year-old single woman. She is employed at a firm close to where she lives. Her annual income is <strong>{income_seller}$</strong>. 
            Beth is a 42-year-old single woman, and she lives in a city 500 miles away from Samantha. Her annual income is <strong>{income_buyer}$</strong>.
            Beth wants to have a baby but she is infertile. She does not want to adopt because she wants to be the genetic mother of her child. 
            She has already acquired donor sperm and is looking for a surrogate mother.
            Samantha and Beth meet on an online platform where they come to the following agreement: 
            Beth will pay Samantha to be a surrogate mother for her child. 
            This means Samantha will be pregnant with Beth's baby, and upon delivery, the baby will be given to Beth with all legal rights.
        </div>
        '''
    elif vignette == 'queue_jump':
        name = 'Line Stander'
        vignette_picture = C.queue_jump_picture

        text = f'''
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <div style="flex: 1; padding-right: 20px; text-align: justify;">
                Congressional hearings are usually open to the public. Any U.S. citizen is welcome to observe the sessions.
                Seating, however, is limited and operates on a first-come-first-serve basis. 
                As a result, attendees may need to queue for hours to secure entry. 
                This has led to the business of line-standing, where individuals are paid to wait in line and exchange their positions with the buyer.
            </div>

            <div style="flex: 0 0 40%; text-align: center;">
                <img src="{vignette_picture}" alt="Line Stander" style="max-width: 100%; height: 300px; margin-left: 0px;">
            </div>
        </div>

        <div style="text-align: justify; margin-top: 20px;">
            <div style="text-align: center;">
                <h5>Scenario</h5>
            </div>
            Philip is a 35-year-old man. His annual income from working at a start-up is <strong>{income_seller}$</strong>.
            Bruce is a 42-year-old man. His annual income is <strong>{income_buyer}$</strong>.
            Bruce wants to attend an important congressional hearing that has garnered significant public interest. 
            With limited seating available, a large crowd is expected to queue for hours. 
            To secure a spot, Bruce and Philip reach an agreement: Bruce will pay Philip to stand in line for 20 hours. 
            Just before Philip’s turn to enter, Bruce will take his place in the queue.
        </div>
        '''
    elif vignette == 'prostitute':
        name = 'Prostitution'
        vignette_picture = C.prostitute_picture

        text = f'''
                Prostitution is the exchange of sexual services for money, goods, or other forms of compensation. 
                It is a profession practiced worldwide, though its legality, regulation, and social perception vary greatly by country and culture.

        <div style="text-align: justify; margin-top: 20px;">
            <div style="text-align: center;">
                <h5>Scenario</h5>
            </div>
            Sarah is a 31-year-old woman. She lives in the countryside and works at a company in a nearby large city. 
            She commutes to her job with her private car. Her annual income is <strong>{income_seller}$</strong>.
            Benjamin is a 45-year-old man. He lives and works in the city where Sarah works. His annual income is <strong>{income_buyer}$</strong>.
            Although Benjamin and Sarah have never met, he has noticed her on several occasions in public spaces.
            While Benjamin is not interested in dating, he finds the idea of a one-time, no-strings-attached sexual encounter appealing. 
            By chance, the two cross paths in a park and strike up a conversation. 
            During their talk, they come to an agreement: Benjamin will pay Sarah to have sex with him in a safe, pre-arranged location of her choosing.
        </div>
        '''
    elif vignette == 'dwarf_tossing':
        name = 'Dwarf Tossing'
        vignette_picture = C.dwarf_tossing_picture

        text = f'''
                Dwarf tossing is an activity in which individuals with dwarfism are thrown onto mattresses or at Velcro-coated walls. 
                They wear special padded clothing or Velcro costumes, and participants compete to throw them the farthest. 
                This practice has sparked significant ethical debate due to its exploitative nature.


        <div style="text-align: justify; margin-top: 20px;">
            <div style="text-align: center;">
                <h5>Scenario</h5>
            </div>
            Casey is a 28-year-old man with dwarfism. His annual income from working a desk job is <strong>{income_seller}$</strong>.
            Jonathan is a 45-year-old man. His annual income at a large company is <strong>{income_buyer}$</strong>.
            On the internet, Jonathan reads about the concept of "dwarf tossing" and decides to organize such a competition for a friend's birthday party.
            Jonathan and Casey come to the following agreement: Jonathan will pay Casey to be the dwarf who will be tossed in the competition.
        </div>
        '''
    elif vignette == 'waste_trade':
        name = 'Waste Trade'
        vignette_picture = C.waste_trade_picture

        text = f'''
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <div style="flex: 1; padding-right: 20px; text-align: justify;">
                The global waste trade involves the cross-border exchange of waste between nations for treatment, disposal, or recycling. 
                Developing countries frequently import hazardous waste from more economically developed nations, raising ethical and environmental concerns.
                The United States ranks as one of the largest exporters of plastic waste globally.
            </div>

            <div style="flex: 0 0 40%; text-align: center;">
                <img src="{vignette_picture}" alt="Waste Trade" style="max-width: 100%; height: 300px; margin-left: 0px;">
            </div>
        </div>

        <div style="text-align: justify; margin-top: 20px;">
            <div style="text-align: center;">
                <h5>Scenario</h5>
            </div>
            Country A is a medium-sized nation with an average annual income of <strong>{income_seller}$</strong> per person.
            Country B is a medium-sized country with an average annual income of <strong>{income_buyer}$</strong> per person.
            Country B generates a substantial volume of consumer-product waste. 
            Country B and Country A come to the following agreement: Country A will pay Country B to take some of its hazardous waste for disposal and recycling.
        </div>
        '''

    elif vignette == 'coin_collector':
        name = 'Coin Collecting'
        vignette_picture = C.coin_collector_picture

        text = f'''
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <div style="flex: 1; padding-right: 20px; text-align: justify;">
                Coin collecting involves the search and acquisition of coins, often for numismatic value. 
                The value of a coin is determined by rarity, condition, and demand. 
                Coins are collected from different regions, time periods, and countries, with some collectors focusing on a specific theme.
            </div>

            <div style="flex: 0 0 40%; text-align: center;">
                <img src="{vignette_picture}" alt="Coin Collector" style="max-width: 100%; height: 300px; margin-left: 0px;">
            </div>
        </div>

        <div style="text-align: justify; margin-top: 20px;">
            <div style="text-align: center;">
                <h5>Scenario</h5>
            </div>
            Alice is a 30-year-old woman. She collects rare, valuable coins and has made her passion her profession. 
            Her annual income is <strong>{income_seller}$</strong>.
            Oscar is a 40-year-old man who also has a keen interest in coin collecting. His annual income is <strong>{income_buyer}$</strong>.
            Alice possesses a rare, highly sought-after coin that Oscar is willing to purchase. 
            They agree to a fair price, and Alice sells the coin to Oscar as part of their mutual interest in the hobby.
        </div>
        '''

    elif vignette == 'apple_seller':
        name = 'Apple Selling'
        vignette_picture = C.apple_seller_picture

        text = f'''
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <div style="flex: 1; padding-right: 20px; text-align: justify;">
                Apple selling is a trade practice where sellers offer apples at markets or online. 
                Sellers may focus on rare varieties or those grown in specific conditions, increasing the appeal to collectors and enthusiasts.
            </div>

            <div style="flex: 0 0 40%; text-align: center;">
                <img src="{vignette_picture}" alt="Apple Seller" style="max-width: 100%; height: 300px; margin-left: 0px;">
            </div>
        </div>

        <div style="text-align: justify; margin-top: 20px;">
            <div style="text-align: center;">
                <h5>Scenario</h5>
            </div>
            Heather is a 33-year-old woman. She runs a small, organic apple farm. Her annual income from selling apples is <strong>{income_seller}$</strong>.
            Susan is a 40-year-old woman who runs a bakery. She uses apples for her signature pies. Her annual income is <strong>{income_buyer}$</strong>.
            Heather offers a rare variety of apples that are particularly prized for their flavor and texture. 
            Susan, seeking to use these special apples in her pies, purchases a large order from Heather, negotiating a price based on the volume she buys.
        </div>
        '''





    else: 
        text = 'Vignette not found'
        name = 'Vignette not found'
        
    
    return text, name 


def variables_for_template(player, Page_number, Attention_check=False, moral=False):
    current_vignette = player.participant.Vignette_order[Page_number]
        
        
    label = current_vignette+'_'+player.participant.Treatment
    vignette_text, vignette_name= return_vignette(current_vignette, player.participant.Treatment)
    labels_for_sliders = {
    'exploit': C.Slider_label_exploit, 
    'autonomy': C.Slider_label_autonomy,
    'coercion': C.Slider_label_coercion,
    'fairA': C.Slider_label_fairA,
    'dignity': C.Slider_label_dignity,
    'harm': C.Slider_label_harm,
    }
    
    if Attention_check:
        return {'Instructions': C.Instructions_path,
                'Vignette_text': C.Attention_check,
                }
    elif moral:
        return {'Instructions': C.Instructions_path,
                'Vignette': current_vignette,
                'Vignette_text': vignette_text,
                'vignette_name': vignette_name,
                'label': label,
                'labels_for_sliders': labels_for_sliders,
                }
    else:
        return {'Instructions': C.Instructions_path,
                'Vignette': current_vignette,
                'Vignette_text': vignette_text,
                'vignette_name': vignette_name,
                }
    
    

def get_form_fields_userdef(player, Page_number, sob=False):
    current_vignette = player.participant.Vignette_order[Page_number]
    if sob:
        return [f"{current_vignette}_beliefs"]
    else:
        return [f"{current_vignette}_ban"]

  
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
  
class BasePage(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True

    @staticmethod
    def get_form_fields(player, number, sob):
        return get_form_fields_userdef(player, number, sob)

    @staticmethod
    def vars_for_template(player: Player, number):
        return variables_for_template(player, number)

    @staticmethod
    def js_vars(player: Player, number):
        return dict(vignette=player.participant.Vignette_order[number])

    @staticmethod    
    def error_message(player, values):
        if (list(values.values())[0]==None):
            return 'Please answer the question by moving the slider'




# Dynamically create main and `_sob` pages
def create_pages():
    pages = []
    for i in range(9):  # Adjust the range as needed
        # Main page
        main_page_attrs = {
            'number': i,
            'sob': False,
            'get_form_fields': lambda player, i=i: BasePage.get_form_fields(player, i, False),
            'vars_for_template': lambda player, i=i: BasePage.vars_for_template(player, i),
            'js_vars': lambda player, i=i: BasePage.js_vars(player, i),
        }
        main_page_class = type(f"Page{i + 1}", (BasePage,), main_page_attrs)
        pages.append(main_page_class)

        # _sob page
        sob_page_attrs = {
            'number': i,
            'sob': True,
            'get_form_fields': lambda player, i=i: BasePage.get_form_fields(player, i, True),
            'vars_for_template': lambda player, i=i: BasePage.vars_for_template(player, i),
            'js_vars': lambda player, i=i: BasePage.js_vars(player, i),
        }
        sob_page_class = type(f"Page{i + 1}_sob", (BasePage,), sob_page_attrs)
        pages.append(sob_page_class)
    return pages


# Generate the pages
generated_pages = create_pages()


class PartII_instructions(Page):
    pass

class Page_moral(Page):
    form_model = 'player'
    form_fields = ['kidney_exploit', 'kidney_autonomy', 'kidney_coercion', 'kidney_fairA', 'kidney_dignity', 'kidney_harm']
   
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True


    @staticmethod
    def vars_for_template(player: Player):
        current_vignette = 'kidney'
        
        label = current_vignette+'_'+player.participant.Treatment
        vignette_text, vignette_name= return_vignette(current_vignette, player.participant.Treatment)
        labels_for_sliders = {
        'exploit': C.Slider_label_exploit, 
        'autonomy': C.Slider_label_autonomy,
        'coercion': C.Slider_label_coercion,
        'fairA': C.Slider_label_fairA,
        'dignity': C.Slider_label_dignity,
        'harm': C.Slider_label_harm,
        }
      
        return {'Instructions': C.Instructions_path,
                'Vignette': current_vignette,
                'Vignette_text': vignette_text,
                'vignette_name': vignette_name,
                'label': label,
                'Slider_labels': labels_for_sliders,
                }


    @staticmethod
    def js_vars(player: Player):
        return dict(vignette='kidney')


#%%  Table parts

'base page'
class BasePage_Table(Page):
    form_model = 'player'
    form_fields = []
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True

    @staticmethod
    def js_vars(player: Player):
        return dict(vignette='kidney')

    @staticmethod
    def vars_for_template(player: Player):
        current_vignette = 'kidney'
        
        label = current_vignette+'_'+player.participant.Treatment
        vignette_text, vignette_name= return_vignette(current_vignette, player.participant.Treatment)
        labels_for_sliders = {
        'health': C.Slider_label_health, 
        }
      
        return {'Instructions': C.Instructions_path,
                'Vignette': current_vignette,
                'Vignette_text': vignette_text,
                'vignette_name': vignette_name,
                'label': label,
                'Slider_labels': labels_for_sliders,
                }
class BasePage_Table_2(Page):
    form_model = 'player'
    form_fields = []
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed == True

    @staticmethod
    def js_vars(player: Player):
        return dict(vignette='kidney')

    @staticmethod
    def vars_for_template(player: Player):
        current_vignette = 'kidney_2'
        
        label = current_vignette+'_'+player.participant.Treatment
        vignette_text, vignette_name= return_vignette(current_vignette, player.participant.Treatment)
        labels_for_sliders = {
        'health': C.Slider_label_health, 
        }
      
        return {'Instructions': C.Instructions_path,
                'Vignette': current_vignette,
                'Vignette_text': vignette_text,
                'vignette_name': vignette_name,
                'label': label,
                'Slider_labels': labels_for_sliders,
                }
        
class Page11_imagined(BasePage_Table):
    extra_fields = ['kidney_imagined_health','kidney_imagined_price'] 
    form_fields = BasePage_Table.form_fields + extra_fields


class Part_IV_table_1(BasePage_Table_2):
    extra_fields = ['scenario_directionality_1_ban', 'scenario_directionality_2_ban',
                    'scenario_directionality_1_realism','scenario_directionality_2_realism',
                    'scenario_directionality_1_realism_free_text', 'scenario_directionality_2_realism_free_text']
    form_fields = BasePage_Table.form_fields + extra_fields
    
    
class Part_IV_table_2(BasePage_Table_2):
    extra_fields = ['scenario_rich_1_ban', 'scenario_rich_2_ban']
    form_fields = BasePage_Table.form_fields + extra_fields
    
class Part_IV_table_3(BasePage_Table):
    extra_fields = ['scenario_equality_1_ban', 'scenario_equality_2_ban']
    form_fields = BasePage_Table.form_fields + extra_fields

class Part_IV_table_4(BasePage_Table):
    extra_fields = ['scenario_price_1_ban', 'scenario_price_2_ban']
    form_fields = BasePage_Table.form_fields + extra_fields
class Part_IV_table_5(BasePage_Table):
    extra_fields = ['scenario_donation_1_ban', 'scenario_donation_2_ban', 
                    'scenario_donation_1_realism', 'scenario_donation_2_realism']
    form_fields = BasePage_Table.form_fields + extra_fields

        
page_sequence = generated_pages + [Attention_check_2,PartII_instructions, Page_moral, 
                                   Page11_imagined, Part_IV_table_1, Part_IV_table_2, Part_IV_table_3, Part_IV_table_4, Part_IV_table_5]
