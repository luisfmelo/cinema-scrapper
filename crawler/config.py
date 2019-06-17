import logging.config
import os

CINEMAS = [
    {
        "name": "Nos Lusomundo Cinemas",
        "url": "http://cinemas.nos.pt/pages/cartaz.aspx",
        "class": "cinemas-nos"
    }
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


CHROME_DRIVER = './chromedriver'

SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']

MQTT = {
    'HOST': os.environ.get('MOSQUITTO_HOST', 'localhost'),
    'PORT': os.environ.get('MOSQUITTO_PORT', '1883')
}

NEW_SESSION_TOPIC = 'new_session_topic'
