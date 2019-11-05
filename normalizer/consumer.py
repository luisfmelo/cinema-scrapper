import json
import logging
from datetime import timedelta

import paho.mqtt.client as paho
import redis as redis

from config import MQTT, NEW_SESSION_TOPIC, REDIS, OMDB_API_KEY, CINEMA_API, HERE_PLACES

# Set up redis client
from couch import CouchDB
from data.Session import Session
from services import cinema_api, omdb_api, here_api
from utils import b64

REDIS_EXPIRATION = timedelta(days=7)

r = redis.Redis(host=REDIS["HOST"], port=REDIS["PORT"])
couch = CouchDB()
c_api = cinema_api.Api(CINEMA_API["URL"])
omdb = omdb_api.Api(OMDB_API_KEY, r)
here_places_api = here_api.Api(HERE_PLACES["APP_ID"], HERE_PLACES["APP_CODE"], r)

logger = logging.getLogger(__name__)


def on_message(client, userdata, msg):
    try:
        print("%-20s %d %s" % (msg.topic, msg.qos, msg.payload))

        body = json.loads(b64.decode_string(msg.payload))

        # Log Message
        couch.new_session(body)

        session = Session.from_json(body)

        # Check cinema
        # TODO: delete this when company starts to work
        session.cinema = here_places_api.search_cinema(session.cinema)

        # Check if movie was not processed before

        # Call API to create a new session record. Expected response 201 oe 409
        res = c_api.new_session(session.to_json())

        if res.status_code != 201 and res.status_code != 409:
            raise Exception("ERROR posting to API.")

        client.publish('pong', 'ack', 0)
        return msg

    except Exception as e:
        logger.error(str(e))


def main():
    print("Starting Consumer...")

    # set up MQTT client
    client = paho.Client()
    client.on_message = on_message
    client.connect(MQTT['HOST'], int(MQTT['PORT']))
    client.subscribe(NEW_SESSION_TOPIC, qos=2)

    # Forever loop
    client.loop_forever()


if __name__ == '__main__':
    main()
