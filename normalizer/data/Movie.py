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

    VERSIONS = ["dob", "leg"]
    FORMATS = ["3D", "4DX", "ATMOS", "IMAX"]

    def to_json(self):
        return {
            'title': self.title,
            'original_title': self.original_title,
            'year': int(self.year),
            'age_rating': self.age_rating,
            'duration': int(self.duration),
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
            title = j["title"]

            # Get Version
            versions = []
            for v in Movie.VERSIONS:
                title, found = Movie.search_keyword(title, v)
                if found:
                    versions.append(v)

            # Get Formats
            formats = []
            for f in Movie.FORMATS:
                title, found = Movie.search_keyword(title, f)
                if found:
                    formats.append(f)

            return Movie(
                title=title.strip(),
                original_title=j["original_title"].strip(),
                year=j["year"].strip(),
                age_rating=j["age_rating"].strip(),
                duration=j["duration"].strip(),
                genre=j["genre"].strip(),
                country=j["country"].strip(),
                version=",".join(versions),
                format=",".join(formats),
                synopsis=j.get("synopsis", None),
                trailer_url=j.get("trailer_url", None),
                imdb_url=j.get("imdb_url", None),
                rating=j.get("rating", None),
                poster=j.get("poster", None),
            )
        except Exception:
            raise Exception("ERROR: decoding Movie")

    @staticmethod
    def search_keyword(movie_title: str, keyword: str) -> (str, bool):
        idx = movie_title.lower().find(keyword.lower())
        # Found
        if idx != -1:
            # Search for parenthesis before '(' and after ')' -> to remove them
            with_parenthesis = not (movie_title[idx - 1] == '(' and movie_title[idx + len(keyword)] == ')')

            start_idx = idx - 1 if with_parenthesis else idx
            end_idx = idx + len(keyword) + 1 if with_parenthesis else idx + len(keyword)

            title = movie_title[:start_idx] + movie_title[end_idx:]
            return title.strip(), True

        return movie_title, False
