from manager.map import Map
from exception.not_valid_location import NotValidLocationException

class DeliveryPackage:
    __unique_package_id = 1

    def __init__(self, start_location: str, end_location: str,
                 weight: float, contact_info: str) -> None:
        self._unique_package_id = DeliveryPackage.__unique_package_id
        DeliveryPackage.__unique_package_id += 1  
        
        self.start_location = start_location
        self.end_location = end_location
        self.weight = weight
        self.contact_info = contact_info
        
    @property
    def start_location(self):
        return self._start_location
    
    @start_location.setter
    def start_location(self,value):
        if not Map._valid_location(value):
            raise NotValidLocationException(f'Invalid start location {value}.')
        
        self._strat_location = value
        
    @property
    def end_location(self):
        return self._end_location
    
    @end_location.setter
    def end_location(self,value):
        if not Map._valid_location(value):
            raise NotValidLocationException(f'Invalid end location {value}.')
        
        self._end_location = value
        
    @property
    def weight (self):
        return self._weight
    
    @weight.setter
    def weight (self, value):
        if not isinstance(value, float):
            raise ValueError('Weight must be real number.')
        if value < 0:
            raise ValueError('Weight must be positive number.')

        self._weight = value
        
    def info(self):
        return (
            f'Package number {self.__unique_package_id}\n'
            f'Start location: {self.start_location} \n'
            f'End location: {self.end_location} \n'
            f'Weight: {self.weight} \n'
        )
        