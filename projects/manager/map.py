from typing import Tuple
from exception.not_valid_location import NotValidLocationException

class Map:
    _locations = ['PER','DAR','ASP','BRI','SYD','MEL','ADL']

    _distances = {
        "SYD": {"MEL": 877, "ADL": 1376, "ASP": 2762, "BRI": 909, "DAR": 3935, "PER": 4016},
        "MEL": {"SYD": 877, "ADL": 725, "ASP": 2255, "BRI": 1765, "DAR": 3752, "PER": 3509},
        "ADL": {"SYD": 1376, "MEL": 725, "ASP": 1530, "BRI": 1927, "DAR": 3027, "PER": 2785},
        "ASP": {"SYD": 2762, "MEL": 2255, "ADL": 1530, "BRI": 2993, "DAR": 1497, "PER": 2481},
        "BRI": {"SYD": 909, "MEL": 1765, "ADL": 1927, "ASP": 2993, "DAR": 3426, "PER": 4311},
        "DAR": {"SYD": 3935, "MEL": 3752, "ADL": 3027, "ASP": 1497, "BRI": 3426, "PER": 4025},
        "PER": {"SYD": 4016, "MEL": 3509, "ADL": 2785, "ASP": 2481, "BRI": 4311, "DAR": 4025},
    }

    @classmethod
    def get_location(cls) -> Tuple[str, ...]:
        return tuple(cls._locations)

    @classmethod
    def _valid_location(cls, city: str) -> bool:
        return city in cls._locations

    @classmethod
    def calculate_distance(cls, city1: str, city2: str) -> int:
        city1, city2 = city1.upper(), city2.upper()

        if not cls._valid_location(city1):
            raise NotValidLocationException(f"{city1} is not a valid location")
        if not cls._valid_location(city2):
            raise NotValidLocationException(f"{city2} is not a valid location")

        if city1 == city2:
            return 0

        return cls._distances.get(city1, {}).get(city2) or cls._distances[city2][city1]
