import json

import requests
from redis import Redis

from data.Movie import Movie


class Api:
    CACHE_TTL = 30 * 24 * 60 * 60  # 30 days

    def __init__(self, api_key: str, r: Redis):
        self.base_url = "https://www.omdbapi.com"  # /?t=Maleficent+-+Mistress+of+Evil&apikey=153a972a
        self.api_key = api_key
        self.cache = r

    def search_movie(self, movie: Movie):
        key = movie.original_title if movie.original_title != "" else movie.title
        c = self.cache.get(key)
        if c is None:
            # Cal OMDB api to get original movie title
            url = f"{self.base_url}/?t={key}&y={movie.year}&apikey={self.api_key}"
            res = requests.request(method="GET", url=url)
            if res.status_code != 200:
                raise Exception("Error fetching from OMDB")
            # update movie data
            data = res.json()
            if "Title" in data and data["Title"] != "":
                movie.original_title = data["Title"]
            if "Poster" in data and data["Poster"] != "":
                movie.poster = data["Poster"]
            if "imdbID" in data and data["imdbID"] != "":
                movie.poster = f"https://www.imdb.com/title/{data['imdbID']}/"
            if "Rating" in data and data["Rating"] != "":
                movie.rating = data["Rating"]
            if len(data["Ratings"]) > 0:
                pass

            success = self.cache.setex(key, self.CACHE_TTL, json.dumps(movie.to_json()))
            if not success:
                raise Exception("ERROR saving on REDIS.")

        return movie
