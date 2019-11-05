from dataclasses import dataclass


@dataclass
class Movie:
    title: str
    original_title: str
    year: int
    age_rating: str
    duration: int
    genre: str
    country: str
    version: str
    format: [None, str]
    synopsis: [None, str]
    trailer_url: [None, str]
    imdb_url: [None, str]
    rating: [None, float]

    def to_json(self):
        return {
            'title': self.title,
            'original_title': self.original_title,
            'year': self.year,
            'age_rating': self.age_rating,
            'duration': self.duration,
            'genre': self.genre,
            'country': self.country,
            'synopsis': self.synopsis,
            'trailer_url': self.trailer_url,
            'imdb_url': self.imdb_url,
            'rating': self.rating
        }



