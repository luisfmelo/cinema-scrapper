import requests
from config import SLACK_WEBHOOK_URL


def notify_slack_message(msg):
    res = requests.post(SLACK_WEBHOOK_URL, json={"text": msg})
    if res.status_code != 200:
        raise SlackException()


class SlackException(Exception):
    pass
