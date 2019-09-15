import requests


class Api:
    def __init__(self):
        self.url = "https://enup4er791vps.x.pipedream.net"

    def new_session(self, payload):
        url = f"{self.url}/session"
        r = requests.request(method="POST", url=url, json=payload)
        return r
