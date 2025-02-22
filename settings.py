from os import environ
#TODO: add the prolific completion link here
SESSION_CONFIGS = [
    dict(name='Study',
         #TODO: AFTER PILOT, REMOVE THE PILOT FROM THE APPSEQUENCE
         app_sequence=['Introduction', 'Main_Part','Exit', 'Pilot','Results'], 
         num_demo_participants=10,
         completionlink='https://app.prolific.com/submissions/complete?cc=CCNA4C97'),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

ROOMS = [
    dict( name = 'Survey', display_name = 'Survey'),
]


SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [
    'Allowed',
    'Attention_1', 'Attention_2', 'Attention_3',
    'Attention_passed',
    'Treatment', 'Vignette_order',
]
SESSION_FIELDS = {
                    'Treatment_quotas':{} 
                 }

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '9007113971546'
