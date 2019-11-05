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

COUCHDB = {
    'HOST': os.environ.get('COUCHDB_HOST', 'http://localhost'),
    'PORT': os.environ.get('COUCHDB_PORT', '5984')
}

OMDB_API_KEY = os.environ.get('OMDB_API_KEY', '')

HERE_PLACES = {
    "APP_ID": os.environ.get('HERE_APP_ID', ''),
    "APP_CODE": os.environ.get('HERE_APP_CODE', '')
}

CINEMA_API = {
    "URL": os.environ.get('CINEMA_API_URL', "http://localhost:8000")
}
