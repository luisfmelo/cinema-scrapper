import os

NEW_SESSION_TOPIC = os.environ['NEW_SESSION_TOPIC']

MQTT = {
    'HOST': os.environ.get('MOSQUITTO_HOST', 'localhost'),
    'PORT': os.environ.get('MOSQUITTO_PORT', '1883')
}

REDIS = {
    'HOST': os.environ.get('REDIS_HOST', 'localhost'),
    'PORT': os.environ.get('REDIS_PORT', '6379')
}

