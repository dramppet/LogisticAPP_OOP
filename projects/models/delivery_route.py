from typing import Optional, List,Tuple
from datetime import datetime, timedelta
from functools import reduce

from models.delivery_package import DeliveryPackage
from exception.not_valid_route_location import NotValidRouteLocationExseption
from models.truck import Truck
from map.map import Map

class DeliveryRoute:
    _next_id = 1
    
    def __init__(self, *location: str, deperture_time: Optional[datetime] = None) -> None:
        self.route_id = DeliveryRoute._next_id
        DeliveryRoute._next_id +=1
                       
        self.location = tuple(location)
        self.departure_time = deperture_time or deperture_time.now()
        
        self.truck: Optional[Truck]  = None
        self.packacges: List[DeliveryPackage]  = []
        
    @property
    def locations(self) -> Tuple[str,...]: 
        return Tuple(self._locations)   

    @location.setter
    def location(self, value: Tuple[str,...]):
        if len(value) < 2:
            raise NotValidRouteLocationExseption('Location must be more 1 distination')
        
        normalized = tuple(v.upper() for v in value)
        
        for el in normalized:
            if not Map._valid_location(el):
                raise NotValidRouteLocationExseption(f'Invalid location {el}')
        
        self._location = normalized
        
    @property
    def total_distance(self):
        segments = zip(self._location,self._location[1:])
        return reduce(lambda total,second : total + Map.calculate_distance(*second),
                      segments,0)
        
    @property
    def finish_route(self):
        len_distance = self.total_distance / Truck._MAX_SPEED
        return self.departure_time + timedelta(len_distance)
        
    def info(self)->str:
        return {
            f'Delivery Route {self._next_id}',
            f'Start location {self._location[0]}'
            f'End location {self._location[-1]}'
            f'Create route {self.departure_time}'
            f'End route {self.finish_route}'
            f'Truck {Truck.name}'
            f'Total distance: {self.total_distance}'
        }

    