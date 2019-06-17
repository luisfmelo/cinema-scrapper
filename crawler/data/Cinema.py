from dataclasses import dataclass


@dataclass
class Cinema:
    name: str
    city: [None, str]
    cinema: str

    def to_json(self):
        return {
            'name': self.name,
            'city': self.city,
            'cinema': self.cinema
        }
