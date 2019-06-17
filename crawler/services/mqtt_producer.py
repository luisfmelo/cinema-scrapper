import paho.mqtt.publish as publish

from config import MQTT, NEW_SESSION_TOPIC


def mqtt_publish(payload: str):
    publish.single(
        topic=NEW_SESSION_TOPIC,
        payload=payload,
        hostname=MQTT['HOST'],
        port=int(MQTT['PORT'])
    )
