import json
import os
from datetime import timedelta

import redis

import paho.mqtt.client as paho

from config import MQTT, NEW_SESSION_TOPIC, REDIS

# Set up redis client
from services import b64, cinema_api

REDIS_EXPIRATION = timedelta(days=7)
r = redis.Redis(host=REDIS["HOST"], port=REDIS["PORT"])
api = cinema_api.Api()


def on_message(client, userdata, msg):
    print("%-20s %d %s" % (msg.topic, msg.qos, msg.payload))

    # check cache -> if not present, send POST request and add to the cache
    if not r.get(msg.payload):
        # decode msg
        body = json.loads(b64.decode_string(msg.payload.decode('utf-8')))

        # send post request
        res = api.new_session(body)

        if res.status_code == 200:
            # add to the cache
            success = r.setex(msg.payload, REDIS_EXPIRATION, "")
            if not success:
                print("ERROR saving on REDIS.")
        else:
            print("ERROR posting to API.")

    client.publish('pong', 'ack', 0)
    return msg


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
