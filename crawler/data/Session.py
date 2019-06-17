from dataclasses import dataclass

from data import Cinema
from data import Movie


@dataclass
class Session:
    movie: Movie
    cinema: Cinema
    room: str
    date: str
    hour: str

    def to_json(self):
        return {
            'movie': self.movie.to_json(),
            'cinema': self.cinema.to_json(),
            'room': self.room,
            'date': self.date,
            'hour': self.hour
        }
