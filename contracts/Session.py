from dataclasses import dataclass
import datetime

from .Cinema import Cinema
from .Movie import Movie


@dataclass
class Session:
    movie: Movie
    cinema: Cinema
    room: str
    start_date: datetime

    @staticmethod
    def from_json(j: dict):
        try:
            return Session(
                movie=Movie.from_json(j["movie"]),
                cinema=Cinema.from_json(j["cinema"]),
                room=j["room"].strip(),
                start_date=datetime.datetime.strptime(j["start_date"].strip(), '%Y-%m-%d %H:%M:%S.%f'),
            )
        except Exception:
            raise Exception("ERROR: decoding Movie")

    def to_json(self):
        return {
            'movie': self.movie.to_json(),
            'cinema': self.cinema.to_json(),
            'room': self.room,
            'start_date': self.start_date,
        }
