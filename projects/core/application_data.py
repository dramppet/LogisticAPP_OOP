from typing import List,Tuple,Optional
from datetime import datetime

from manager.map import Map
from models.delivery_route import DeliveryRoute
from exception.invalid_length import InvalidLengthExseption
from exception.not_valid_location import NotValidLocationException

class AplicationData:
    MIN_LOCATION = 2
    
    def __init__(self):
        self._routes:List[DeliveryRoute] = []
        
    @property
    def routes(self) -> Tuple[DeliveryRoute,...]:
        return tuple(self._routes)
        
    
    def create_route(self, *locations: str, departure_time: Optional[datetime] = None) -> DeliveryRoute:
        if len(locations) < AplicationData.MIN_LOCATION:
            raise InvalidLengthExseption(f"Route must have at least {self.MIN_LOCATIONS} locations.")
        normalized = tuple(loc.upper() for loc in locations)
        for loc in locations:
            if not Map._valid_location(loc):
                raise NotValidLocationException(f"{loc} is not a valid location.")
        route = DeliveryRoute(*normalized,deperture_time=departure_time)
        self._routes.append(route)
        return route