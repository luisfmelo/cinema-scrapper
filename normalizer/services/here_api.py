import json
import re

import requests
from redis import Redis

from data.Cinema import Cinema
from utils.utils import str_similarity, hardcoded_city


class Api:
    CACHE_TTL = 30 * 24 * 60 * 60  # 30 days

    def __init__(self, app_id: str, app_code: str, r: Redis):
        self.url = "https://places.cit.api.here.com"
        self.app_id = app_id
        self.app_code = app_code
        self.cache = r
        self.headers = {
            "Accept-Encoding": "gzip",
            "Accept-Language": "en-US,en;q=0.9,pt-PT;q=0.8,pt;q=0.7,es;q=0.6"
        }

    def search_cinema(self, cinema: Cinema) -> Cinema:
        cinema_name = cinema.name
        cinema_company = cinema.company
        if cinema_name == "":  # TODO: delete this?
            raise Exception("Cinema invalid")
        key = self.get_cache_key(cinema_name, cinema_company)

        # Check in cache. If it is not there, request Here API and save in cache
        c = self.cache.get(key)
        if c is not None:
            return Cinema.from_json(json.loads(c))

        # Request Here API
        target = "36.9545,-16.9697;r=1057434"
        q = cinema_name + " cinema"
        url = f"{self.url}/places/v1/discover/search?q={q}&in={target}&app_id={self.app_id}&app_code={self.app_code}"
        r = self.__request(url)

        results = r["results"]["items"]
        if len(results) < 1:
            raise Exception("ERROR: no results found at Here Places.")

        if len(results) > 1:
            results = [r for r in results if r["category"]["id"] in ["mall", "service", "cinema"]]

            if len(results) != 1:
                max_points = 0
                winner = None
                for result in results:
                    points = str_similarity(key, result["title"].lower())
                    if points > max_points:
                        max_points = points
                        winner = result

                if winner is not None:
                    results = [winner]
                else:
                    raise Exception("ERROR: more than 1 result found in Here Places and str similarity didn't work.")

        info = self.__request(results[0]["href"])

        # Store in cache
        cinema.city = info["location"]["address"].get("city", hardcoded_city(key))
        cinema.longitude = info["location"]["position"][0]
        cinema.latitude = info["location"]["position"][1]

        success = self.cache.setex(key, self.CACHE_TTL, json.dumps(cinema.to_json()))
        if not success:
            raise Exception("ERROR saving on REDIS.")

        return cinema

    def get_cache_key(self, cinema_name, company):
        return re.sub("([a-z])([A-Z])", "\g<1> \g<2>", f"{cinema_name} {company}").lower()

    def __request(self, url):
        return requests.request(method="GET", url=url, headers=self.headers).json()
