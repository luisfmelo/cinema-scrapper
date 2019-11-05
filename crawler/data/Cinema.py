from dataclasses import dataclass


@dataclass
class Cinema:
    name: str
    city: [None, str]
    company: str

    def to_json(self):
        return {
            'name': self.name,
            'city': self.city,
            'company': self.company
        }
