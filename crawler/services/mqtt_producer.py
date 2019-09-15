import paho.mqtt.publish as publish

from config import MQTT, NEW_SESSION_TOPIC
from services import b64


def mqtt_publish(payload: str):
    publish.single(
        topic=NEW_SESSION_TOPIC,
        payload=b64.encode_string(payload),
        hostname=MQTT['HOST'],
        port=int(MQTT['PORT'])
    )
