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
    version: [None, str]
    format: [None, str]
    synopsis: [None, str]
    trailer_url: [None, str]
    imdb_url: [None, str]
    rating: [None, float]
    poster: [None, str]

    def to_json(self):
        return {
            'title': self.title,
            'original_title': self.original_title,
            'year': self.year,
            'age_rating': self.age_rating,
            'duration': self.duration,
            'genre': self.genre,
            'country': self.country,
            'version': self.version,
            'format': self.format,
            'synopsis': self.synopsis,
            'trailer_url': self.trailer_url,
            'imdb_url': self.imdb_url,
            'rating': self.rating
        }

    @staticmethod
    def from_json(j: dict):
        try:
            return Movie(
                title=j["title"].strip(),
                original_title=j["original_title"].strip(),
                year=j["year"].strip(),
                age_rating=j["age_rating"].strip(),
                duration=j["duration"].strip(),
                genre=j["genre"].strip(),
                country=j["country"].strip(),
                version=j.get("version", None),
                format=j.get("format", None),
                synopsis=j.get("synopsis", None),
                trailer_url=j.get("trailer_url", None),
                imdb_url=j.get("imdb_url", None),
                rating=j.get("rating", None),
                poster=j.get("poster", None),
            )
        except Exception:
            raise Exception("ERROR: decoding Movie")
