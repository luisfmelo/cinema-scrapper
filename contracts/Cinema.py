from dataclasses import dataclass


@dataclass
class Cinema:
    name: str
    city: str
    company: str
    longitude: float
    latitude: float

    def to_json(self):
        return {
            "name": self.name,
            "city": self.city,
            "company": self.company,
            "longitude": self.longitude,
            "latitude": self.latitude,
        }

    @staticmethod
    def from_json(j: dict):
        return Cinema(
            name=j["name"],
            city=j["city"],
            company=j["company"],
            longitude=j["longitude"],
            latitude=j["latitude"],
        )
