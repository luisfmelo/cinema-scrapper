from dataclasses import dataclass
import datetime

from data.Cinema import Cinema
from data.Movie import Movie


@dataclass
class Session:
    movie: Movie
    cinema: Cinema
    room: str
    start_time: datetime

    @staticmethod
    def from_json(j: dict):
        try:
            return Session(
                movie=Movie.from_json(j["movie"]),
                cinema=Cinema.from_json(j["cinema"]),
                room=j["room"].strip(),
                start_time=datetime.datetime.strptime(j["date"] + " " + j["hour"], '%Y-%m-%d %Hh%M'),
            )
        except Exception:
            raise Exception("ERROR: decoding Movie")

    def to_json(self):
        return {
            'movie': self.movie.to_json(),
            'cinema': self.cinema.to_json(),
            'room': self.room,
            'start_time': self.start_time.isoformat() + 'Z',
        }
