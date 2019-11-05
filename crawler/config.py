import logging.config
import os

CINEMAS = [
    {
        "name": "Nos Lusomundo Cinemas",
        "url": "http://cinemas.nos.pt/pages/cartaz.aspx",
        "class": "cinemas-nos"
    },
    # {
    #     "name": "Castello Lopes Cinemas",
    #     "url": "https://castellolopescinemas.pt/exibicao/",
    #     "class": "cinemas-castello-lopes"
    # },
    # {
    #     "name": "Castello Lopes Cinemas",
    #     "url": "https://castellolopescinemas.pt/brevemente/",
    #     "class": "cinemas-castello-lopes"
    # }
    # {
    #     "name": "Cineplace Nova Arcada - Braga",
    #     "url": "https://filmspot.pt/cinema/cineplace-nova-arcada-braga-111/",
    #     "class": "cinemas-filmspot-cineplace-nova-arcada"
    # },
]

LOGGING_CONFIG = None
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'colored_console': {
            '()': 'colorlog.ColoredFormatter',
            # 'format': "%(log_color)s%(levelname)-8s%(red)s%(module)-30s%(reset)s %(blue)s%(message)s"
            'format': "%(asctime)-20s %(log_color)s%(levelname)-10s%(reset)s %(blue)s%(message)s"
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'colored_console',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        # root logger
        '': {
            'level': 'INFO',
            'handlers': ['console'],
        },
    },
})

chrome_driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver')
CHROME_DRIVER = os.environ.get('CHROME_DRIVER', chrome_driver_path)

SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']

MQTT = {
    'HOST': os.environ.get('MOSQUITTO_HOST', 'localhost'),
    'PORT': os.environ.get('MOSQUITTO_PORT', '1883')
}

NEW_SESSION_TOPIC = os.environ['NEW_SESSION_TOPIC']
