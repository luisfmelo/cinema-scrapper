import requests


class Api:
    def __init__(self, base_url):
        self.url = base_url

    def new_session(self, payload):
        url = f"{self.url}/api/sessions"
        return requests.post(url=url, json=payload)
