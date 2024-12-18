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
#TODO: make sure all the sliders work with darkening the text

class C(BaseConstants):
    NAME_IN_URL = 'Scenarios'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Instructions_path = "_templates/global/Instructions.html"
    Quit_study_text_path = "_templates/global/Quit_study_text.html"
    Return_redirect = "https://www.wikipedia.org/" 
    
    all_vignettes = ['loan_shark', 'kidney', 'surrogate', 'queue_jump', 'prostitute', 'dwarf_tossing', 'waste_trade', 'coin_collector', 'apple_seller']
    
    # pictures
    #TODO: make pics work by putting  them in GITHUB and putting here the permalinks
    loan_shark_picture = "_static/pictures/loan_shark.jpg"
    kidney_picture = "_static/pictures/kidney.png"
    surrogate_picture = "_static/pictures/loan_shark.jpg"
    queue_jump_picture = "_static/pictures/loan_shark.jpg"
    prostitute_picture = "_static/pictures/loan_shark.jpg"
    dwarf_tossing_picture = "_static/pictures/loan_shark.jpg"
    waste_trade_picture = "_static/pictures/loan_shark.jpg"
    coin_collector_picture = "_static/pictures/loan_shark.jpg"
    apple_seller_picture = "_static/pictures/loan_shark.jpg"
    
    
    # slider labels    
    Slider_label_exploit = f'What do you think about the following statement: "<strong>this transaction exploits Bob</strong>"?'
    Slider_label_autonomy = 'In your opinion, does this transaction <strong>respect or limit individual autonomy (i.e. self-determination)</strong>?'
    Slider_label_coercion = 'In your opinion, does this transaction allow the person A <strong> to make fully informed choices or does it exert undue influence</strong>?'
    Slider_label_fairA = f'In your opinion, is this transaction <strong>fair or unfair to Sam</strong>?'
    Slider_label_dignity = 'In your opinion, does this transaction <strong>promote or violate human dignity</strong>?'
    Slider_label_harm = 'What do you think about the following statement: <strong>"allowing such transactions would harm society in the long run"</strong>?'

    # for imagined health
    Slider_label_health = 'In this scenario, how healthy do you think is Sam (the seller of kidney)?'

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
    # Attention check 2, 1 was in introduction 
    Attention_2 = models.BooleanField()
            
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
    kidney_imagined_price = models.FloatField(blank=False, min=0, label='In this scenario, what do you think the agreed-upon price would be (in dollars)?')
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
    assert vignette in C.all_vignettes, 'vignette not found'

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
        A loan shark is an individual who lends money at high interest rates, often accompanied by aggressive collection methods.
        Loansharking is characterized by exorbitant weekly interest rates, typically around 20%.
        Unlike traditional banks, which may take several days or weeks to process loans and often require proof of stable residency,
        loan sharks offer quick access to funds making them particularly appealing to those facing urgent financial need.
        <br><br>
        <div style="text-align: center;">
        <h5>Scenario</h5>
        </div>
        Paul is a 45-year-old man. His annual income is  <strong>{income_seller}$</strong>.
        Peter is a 30-year-old man. His income is <strong>{income_buyer}$</strong>.
        Paul's son is diagnosed with a life-threatening tumor. 
        While surgery offers a chance to save his life, it must be performed immediately.
        The only available surgeon capable of performing the procedure on short notice requires an upfront payment.
        After selling all the assets he can liquidate Paul still falls $100,000 short.
        Traditional banks, which offer weekly interest rates of 5%, are not an option due to their lengthy processing times.
        Paul and Peter come to the following agreement: 
        Peter will lend Paul the remaining amount for one month at an interest rate of 25%.
        '''  
    elif vignette == 'kidney':
        name = 'Kidney transplant'
        vignette_picture = C.kidney_picture

        text = f''' 
        Advances in surgery and medication make living kidney donation a successful treatment for end-stage kidney disease.
        In this process, an individual with two healthy kidneys undergoes surgical removal of one kidney.
        This kidney is then transplanted into the recipient, restoring kidney function.
        Individuals can live healthy and fulfilling lives with a single kidney.
        In the USA more than 90.000 people are on the waiting list for a kidney donation.
        <img src="{vignette_picture}" alt="Kidney transplant" style="max-width: 100%; height: auto; margin-bottom: 20px;">
        <br><br>
        <div style="text-align: center;">
        <h5>Scenario</h5>
        </div>
        Sam is a 40 year old man. He lives in a medium sized city and has a desk-job at a logistics company. He earns <strong>{income_seller}$</strong> annually.
        Bob is a 40 year old man. He also lives in a medium sized, but different city.
        He is employed at a small firm where he earns <strong>{income_buyer}$</strong> annually.
        Due to final-stage kidney disease, <strong>Bob urgently needs a replacement kidney</strong>.
        Although he is on the waiting list for a kidney donation, his doctors tell him that he is not high enough on the list to receive a donation in time.
        Sam hears about Bob's situation through word of mouth. They come to the agreement that Sam will sell one of his kidneys to Bob at an agreed price. 
        '''
    elif vignette == 'surrogate':
        name = 'Gestational Surrogacy'

        text = f''' 
        <strong>Gestational surrogacy</strong> is a medical solution for certain types of infertility.
        It enables a woman to have a biological child through another woman's pregnancy.
        In this process, doctors fertilize the intended mother's egg in a laboratory and implant the resulting embryo into a surrogate. 
        The surrogate carries the baby under a legal agreement, ensuring the child is handed over to the intended mother after birth.
        <br><br>
        <div style="text-align: center;">
        <h5>Scenario</h5>
        </div>
        Samantha is a 29 year old single woman. She is employed at a firm close to where she lives. Her annual income is <strong>{income_seller}$</strong>. 
        Beth is a 42 year old single woman and she lives in a city 500 miles away from Samantha. Her annual income is <strong>{income_buyer}$</strong>.
        Beth wants to have a baby but she is infertile. She does not want to adopt because she wants to be the genetic mother of her child. 
        She has already acquired donor sperm and is looking for a surrogate mother.
        Samantha and Beth meet on an online platform where they come to the following agreement: 
        Beth will pay Samantha to be a surrogate mother for her child. 
        This means Samantha will be pregnant with Beth's baby and upon delivery the baby will be given to Beth with all legal rights. 
        '''
        vignette_picture = C.surrogate_picture
    elif vignette == 'queue_jump':
        name = 'Line stander'

        text = f''' 
        <strong>Line standing.</strong>Congressional hearings are usually open to the public. Any U.S. citizen is welcomed to observe the sessions. Seating, however, is limited and operates on a first-come-first-serve basis. As a result, attendees may need to queue to secure entry to the hearings. This has led to the business of line-standing. Individuals are paid to wait in the queue and exchange their positions with the buyer before the scheduled event. 
        <br><br>
        <div style="text-align: center;">
        <h5>Scenario</h5>
        </div>
        Philip is a 35-year-old man. His annual income from working at a start-up is <strong>{income_seller}$</strong>.
        Bruce is a 42-year-old man. His annual income is <strong>{income_buyer}$</strong>.
        Bruce wants to attend an important congressional hearing that has garnered significant public interest. With limited seating available, a large crowd is expected to queue for hours. To secure a spot, Bruce and Philip reach an agreement: Bruce will pay Philip to stand in line for 20 hours. Just before Philip’s turn to enter, Bruce will take his place in the queue.
        '''
        vignette_picture = C.queue_jump_picture
    elif vignette == 'prostitute':
        name = 'Prostitution'
        text = f''' 
        <strong>Prostitution.</strong>is the exchange of sexual services for money, goods, or other forms of compensation. It is a profession practiced worldwide, though its legality, regulation, and social perception vary greatly by country and culture.
        <br><br>
        <div style="text-align: center;">
        <h5>Scenario</h5>
        </div>
        Sarah is a 31-year-old woman. She lives on the countryside and works at a company in a large city close by. She commutes to her job with her private car. Her annual income is <strong>{income_seller}$</strong>.
        
        Benjamin is a 45-year-old man. He lives and works in the city in which Sarah works. He is employed at a different, rather small company. From this job he makes <strong>{income_buyer}$</strong> annually.
        Although Benjamin and Sarah have never met, he has noticed her on several occasions in public spaces. While Benjamin is not interested in dating, he finds the idea of a one-time, no-strings-attached sexual encounter appealing. By chance, the two cross paths in a park and strike up a conversation. During their talk, they come to an agreement: Benjamin will pay Sarah to have sex with him in a safe, pre-arranged location of her choosing.
        '''
        vignette_picture = C.prostitute_picture
    elif vignette == 'dwarf_tossing':
        name = 'Drawf tossing'
        text = f''' 
        <strong>Dwarf tossing</strong>. Dwarf tossing is an activity in which people with dwarfism (people of around 4ft height) are thrown onto mattresses or at Velcro-coated walls. 
        They are wearing special padded clothing or Velcro costumes. 
        Participants compete to throw the person with dwarfism the farthest.
        <br><br>
        <div style="text-align: center;">
        <h5>Scenario</h5>
        </div>
        Casey is a 28-year-old man with dwarfism. His annual income from working a desk-job is <strong>{income_seller}$</strong>.
        Jonathan is a 45-year-old man. His annual income at a large company is <strong>{income_buyer}$</strong>.
        On the internet, Jonathan reads about the concept of "dwarf tossing" and decides to organize such a competition for a friend's birthday party.
        Jonathan and Casey come to the following agreement:
        Jonathan will pay Casey to be the dwarf that will be tossed in the competition.
        '''
        vignette_picture = C.dwarf_tossing_picture
    elif vignette == 'waste_trade':
        name = 'Waste trade'
        text = f''' 
        <strong>Global waste trade</strong> refers to the cross-border exchange of waste between countries, with the aim of additional treatment, disposal, or recycling. Developing nations frequently import toxic or hazardous wastes from more economically developed countries. 
        The United States, for example, ranks as the sixth-largest exporter of plastic waste, with an export volume totaling 437,480 metric tons.
        <br><br>
        <div style="text-align: center;">
        <h5>Scenario</h5>
        </div>
        Country A is a medium-sized nation with an average annual income of <strong>{income_seller}$</strong> per person.
        Country B, a medium-sized country with an average annual income of <strong>{income_buyer}$</strong> per person,
        generates a substantial volume of consumer-products waste. 
        Country B and A come to the following agreement: B will pay Country A to dispose of 20 million tonnes (approximately 22 billion pounds) of this waste. This waste will be buried in Country A's landfills.
        '''
        vignette_picture = C.waste_trade_picture
    elif vignette == 'coin_collector':
        name = 'Coin collector'
        text = f''' 
        <strong>Coin collecting</strong>.Collecting items like coins is a popular hobby enjoyed by people worldwide.
        Some of these items, though not initially valuable, can increase in worth over time due to collector interest. 
        Online forums provide platforms for coin collectors to buy and sell coins and connect with others who share their passion.
        <br><br>
        <div style="text-align: center;">
        <h5>Scenario</h5>
        </div>
        Samuel is a 40-year-old man who works at a regional company, earning an annual income of <strong>{income_seller}$</strong>.
        In addition to his job, he enjoys collecting coins as a hobby. One day, he decides to sell part of his coin collection and posts it on an online forum for coin enthusiasts.
        Brian is a 32-year-old man. He lives and works at a nearby city. His annual income is <strong>{income_buyer}$</strong>and Brian also collects coins. 
        When Brian comes across Samuel's offer on the online platform, he finds it particularly interesting. 
        After a brief exchange of messages, they agree that Samuel will sell his collection to Brian at the listed price.
        '''
        vignette_picture = C.coin_collector_picture
    elif vignette == 'apple_seller':
        name = 'Apple seller'
        text = f''' 
        <strong>The market for apples</strong> is a global industry that involves the production, distribution, and consumption of apples.
        Among the best-known apple types are Fuji, Gala, and Granny Smith, each catering to different consumer preferences. 
        Apples are sold through various channels, including supermarkets, farmers' markets, and export trade. 
        <br><br>
        <div style="text-align: center;">
        <h5>Scenario</h5>
        </div>
        Hilary is a 35-year-old woman who earns an annual income of <strong>{income_seller}$</strong> from her self-employed business.
        She also owns a small orchard with five apple trees.
        Barbara is a 40-year-old woman who works at a large company, earning <strong>{income_buyer}$</strong> annually.
        Hilary and Barbara meet at a party, where Hilary mentions her orchard. Barbara expresses interest in buying some of Hilary's apples to make juice. 
        They agree that Hilary will sell 100kg of apples to Barbara at an agreed price. Hilary pays taxes on the transaction.
        '''
        vignette_picture = C.apple_seller_picture
                 
    else: 
        text = 'Vignette not found'
        name = 'Vignette not found'
        
    
    return text, name, vignette_picture 


def variables_for_template(player, Page_number, Attention_check=False, moral=False):
    current_vignette = player.participant.Vignette_order[Page_number]
        
        
    label = current_vignette+'_'+player.participant.Treatment
    vignette_text, vignette_name, vignette_pic = return_vignette(current_vignette, player.participant.Treatment)
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
        print(list(values.values())[0])
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
        vignette_text, vignette_name, vignette_pic = return_vignette(current_vignette, player.participant.Treatment)
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
        vignette_text, vignette_name, vignette_pic = return_vignette(current_vignette, player.participant.Treatment)
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
        
class Part_III(BasePage_Table):
    extra_fields = ['kidney_imagined_health','kidney_imagined_price'] 
    form_fields = BasePage_Table.form_fields + extra_fields

class Part_IV_table_1(BasePage_Table):
    extra_fields = ['scenario_directionality_1_ban', 'scenario_directionality_2_ban',
                    'scenario_directionality_1_realism','scenario_directionality_2_realism',
                    'scenario_directionality_1_realism_free_text', 'scenario_directionality_2_realism_free_text']
    form_fields = BasePage_Table.form_fields + extra_fields
        
class Part_IV_table_2(BasePage_Table):
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

        
page_sequence = generated_pages + [Page_moral, Part_III, Part_IV_table_1, Part_IV_table_2, Part_IV_table_3, Part_IV_table_4, Part_IV_table_5]
