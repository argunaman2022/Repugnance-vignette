# vignette texts
def return_vignette(vignette, treatment, income_seller=False, income_buyer=False, name_seller='Sam', name_buyer='Bob'):
    assert treatment in ['poor_poor', 'poor_rich', 'rich_rich'], 'treatment not found'
    
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
        {name_seller} is a 30-year-old man. His annual income is  <strong>{income_seller}</strong>.
        {name_buyer} is a 45 year old man. His income is <strong>{income_buyer}</strong>. {name_seller}'s teenager son is diagnosed with <strong>a rare life threatening tumor<\strong>.
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
        
        {name_seller} is a 40-year-old man. His annual income is <strong>{income_seller}</strong>$.
        {name_buyer} is a 40-year-old man, his annual income is <strong>{income_buyer}</strong>$. Due to final-stage kidney disease, {name_buyer} urgently needs a replacement kidney.
        {name_seller} and {name_buyer} come to the following agreement: {name_seller} will sell one of his kidneys to {name_buyer}.
        '''
    elif vignette == 'surrogate':
        text = f''' 
        <strong>Gestational Surrogacy</strong>. Gestational surrogacy is a useful medical technique for certain infertilities.
        It allows a woman to have a child through another woman's pregnancy. Doctors fertilize her egg in a lab and implant it in a surrogate mother. 
        The surrogate carries the baby with a legal agreement ensuring the genetic mother receives the child after birth.
        <br><br>
        
        {name_seller} is a 29 year old single woman. Her annual income is <strong>{income_seller}</strong>$. {name_seller} is a 42 year old single woman.
        Her annual income is <strong>{income_buyer}</strong>$. {name_seller} wants to have a baby but is infertile. Since she wants to be the genetic mother of the child,
        adopting a baby is not an option for her. {name_seller} and B come to the following agreement: {name_seller} will pay {name_seller} to be a surrogate mother for her child.
        This means {name_seller} will be pregnant with {name_seller}'s baby and upon delivery the baby will be given to {name_seller}. 
        '''
    elif vignette == 'queue_jump':
        text = f''' 
        <strong>Line stander</strong>. Congressional hearings are usually open to the public. Any U.S. citizen is welcomed to observe the sessions.
        Seating, however, is limited and operates on a first-come-first-serve basis. As a result, attendees may need to queue to secure entry to the hearings. 
        This has led to the business of line-standing. Individuals are paid to stand in the queue and exchange their positions with the buyer before the scheduled event. 
        <br><br>
        
        {name_seller} is a 42 year old man. His annual income is <strong>{income_seller}</strong>$. {name_buyer} is a 35 year old man. His annual income is <strong>{income_buyer}</strong>$.
        An important congressional hearing is planned that {name_buyer} wants to attend.
        This hearing is drawing a lot of public interest and so lots of people will be queuing for the limited seats. {name_buyer} and A come to the following agreement:
        {name_buyer} will pay {name_seller} to stand in queue for him for 20 hours. Right before it is {name_seller}'s turn to go in {name_buyer} will come and take his place.
        '''
    elif vignette == 'prostitute':
        text = f''' 
        {name_seller} is a 27 year old woman. Her annual income is <strong>{income_seller}</strong>$.
        {name_buyer} is a 45 year old man. His annual income is <strong>{income_buyer}</strong>$.
        One day he notices her and wants to have a one time no-strings-attached sexual encounter with her.
        {name_buyer} and A come to the following agreement: B will pay {name_seller} to have sex with him in a safe, pre-arranged place of her choosing. 
        '''
    elif vignette == 'dwarf_tossing':
        text = f''' 
        <strong>Dwarf tossing</strong>. Dwarf tossing is an activity in which people with dwarfism (little people of around 4ft height)
        are thrown onto mattresses or at Velcro-coated walls.
        They are wearing special padded clothing or Velcro costumes. Participants compete to throw the person with dwarfism the farthest.
        <br><br>
        
        {name_seller} is a 28 year old man with dwarfism. His annual income is <strong>{income_seller}</strong>$. {name_buyer} is a 45 year old man.
        His annual income is <strong>{income_buyer}</strong>$.
        On the internet, {name_buyer} reads about the concept of "dwarf tossing" and decides to organize such a competition for a friend's birthday party as a gift.
        {name_buyer} and A come to the following agreement: B will pay A to be the dwarf that will be tossed in the competition.
        '''
    elif vignette == 'waste_trade':
        text = f''' 
        <strong>Waste trade</strong>. Global waste trade refers to the cross-border exchange of waste between countries,
        with the aim of additional treatment, disposal, or recycling. Developing nations frequently import toxic or hazardous wastes from more economically developed countries.
        The United States, for example, ranks as the sixth-largest exporter of plastic waste, with an export volume totaling 437,480 metric tons.
        <br><br>
        
        Country A is a medium-sized nation with an average annual income of <strong>{income_seller}</strong>$ per person.
        Country B, a medium-sized country with an average annual income of <strong>{income_buyer}</strong>$ per person,
        generates a substantial volume of consumer-products waste. Country B and A come to the following agreement: B will pay Country A to dispose of 20 million tonnes (approximately 22 billion pounds) of this waste.
        This waste will be buried in Country A's landfills.
        '''
    elif vignette == 'coin_collector':
        text = f''' 
        <strong>Unburied treasures</strong>. In some U.S states items found while digging in private property belongs to the owner.
        Some such items, while not initially valuable, can gain worth over time due to the interest of collectors, such as those specializing in coins.
        <br><br>
        
        {name_seller} is a 40 year old man. His annual income is <strong>{income_seller}</strong>$.
        {name_buyer} is a 40 year old man. His annual income is <strong>{income_buyer}</strong>$. One of his hobbies is coin collecting.
        While digging in his backyard {name_seller} finds an old U.S quarter. {name_seller} and B come to the following agreement: {name_seller} will sell the coin to {name_buyer}. 
        '''

                 
    else: text = 'Vignette not found'
    #TODO: finish all texts
        
    return text



# delete below

Child_inequality = '''
    {name_seller} is a 13 year old girl. She lives together with her parents in a household of 3 people. Their household's annual income is <strong>31k USD</strong>.
    {name_seller} is a 50 year old woman. She lives together with her husband and mother in a household of 3 people.
    Their annual income is <strong>75k USD</strong>. {name_seller} will work for 5 hours every Saturday cleaning {name_seller}'s 2 story-house2 story-house for an hourly wage of 15 USD/hour.'''
    Child_equality = '''
    {name_seller} is a 13 year old girl. She lives together with her parents in a household of 3 people. Their household's annual income is <strong>31k USD</strong>.
    {name_seller} is a 50 year old woman. She lives together with her husband and mother in a household of 3 people.
    Their annual income is <strong>31k USD</strong>. {name_seller} will work for 5 hours every Saturday cleaning {name_seller}'s 2 story-house2 story-house for an hourly wage of 15 USD/hour.'''
    
    #TODO: both of these are hardcoded for presentation purposes.
    Kidney_inequality = '''
    Samuel is a 40-year-old man, living with his wife and one kid in a household of 3 people, with an annual income of 31k$.
    Benjamin is a 40-year-old man, residing with his wife and one kid in a similar household with an annual income of 75k$.
    Due to final-stage kidney disease, Benjamin urgently needs a replacement kidney. Samuel will sell one of his kidneys to Benjamin.'''
    Kidney_equality = '''
Samuel is a 40-year-old man, living with his wife and one kid in a household of 3 people, with an annual income of 31k\$.
    Benjamin is a 40-year-old man, residing with his wife and one kid in a similar household with an annual income of 75k\$.
    Due to final-stage kidney disease, Benjamin urgently needs a replacement kidney. Samuel will sell one of his kidneys to Benjamin..'''
    
    Waste_inequality = '''
    Country A is a medium-sized nation with an average annual wage of <strong>31k USD</strong>.
    Country B, a medium-sized country with an average annual wage of <strong>75k USD</strong>, generates a substantial volume of consumer-products waste.
    Country B will sell 20 million tons (approximately 22 billion pounds) of this waste to Country A at the prevailing market price.
    This waste is non-recyclable and will be burnt in Country A's incinerators.
    '''
    Waste_equality = '''
    Country A is a medium-sized nation with an average annual wage of <strong>31k USD</strong>.
    Country B, a medium-sized country with an average annual wage of <strong>31k USD</strong>, generates a substantial volume of consumer-products waste.
    Country B will sell 20 million tons (approximately 22 billion pounds) of this waste to Country A at the prevailing market price. 
    This waste is non-recyclable and will be burnt in Country A's incinerators.
    '''
    Baby_inequality = '''
    {name_seller} is a 25 year old single, pregnant woman. She lives alone and works at a retail shop. 
    Her annual net income is <strong>31k USD</strong>. {name_seller} is a 40 year old single woman. 
    She lives alone and her household's annual net income is <strong>75k USD</strong>. {name_seller} wants to have a baby but is infertile.
    Adopting a baby in their country is extremely difficult. {name_seller} will sell her baby to {name_seller} once she is born.
    '''
    Baby_equality = '''
    {name_seller} is a 25 year old single, pregnant woman. She lives alone and works at a retail shop. 
    Her annual net income is <strong>31k USD</strong>. {name_seller} is a 40 year old single woman. 
    She lives alone and her household's annual net income is <strong>31k USD</strong>. {name_seller} wants to have a baby but is infertile.
    Adopting a baby in their country is extremely difficult. {name_seller} will sell her baby to {name_seller} once she is born.
    '''
    Collector_inequality = '''
    {name_seller} is a 40 year old man. He lives together with his wife and one kid in a household of 3 people.
    Their household's annual income is <strong>31k USD</strong>. {name_seller} is a 40 year old man. 
    He lives together with her wife and one kid in a household of 3 people. Their annual income is <strong>75k USD</strong>.
    {name_seller} has a coin collection he has been collecting since his teenages.
    {name_seller} will sell this collection to {name_seller} at the prevailing market price.
    '''
    Collector_equality = '''
    {name_seller} is a 40 year old man. He lives together with his wife and one kid in a household of 3 people.
    Their household's annual income is <strong>31k USD</strong>. {name_seller} is a 40 year old man. 
    He lives together with her wife and one kid in a household of 3 people. Their annual income is <strong>31k USD</strong>.
    {name_seller} has a coin collection he has been collecting since his teenages.
    {name_seller} will sell this collection to {name_seller} at the prevailing market price.
    '''
