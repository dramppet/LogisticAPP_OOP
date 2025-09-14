import random
from typing import Dict, List, Optional
from models.truck import Truck
from manager.map import Map
from status.truck import TruckStatus

class VehicleManager:
    def __init__(self):
        self.vehicles = (
            [Truck(i, "Scania", 42000, 8000) for i in range(1001, 1011)] +
            [Truck(i, "Man",    37000, 10000) for i in range(1011, 1026)] +
            [Truck(i, "Actros", 26000, 13000) for i in range(1026, 1041)]
        )
        self.truckLocation: Dict[str, List[Truck]] = {}
        self.disperse_trucks()

    # Disperse trucks by city and set truck location
    def disperse_trucks(self) -> Dict[str, List[Truck]]:
        for location in Map._locations:
            selected = random.sample(self.vehicles, 6)
            # задаваме текущата локация на всеки избран камион
            for truck in selected:
                truck.location = location
            self.truckLocation[location] = selected
        return self.truckLocation

    def free_truck(self, city: str) -> List[Truck]:
        if Map._valid_location(city):
            return [
                truck for truck in self.truckLocation.get(city, [])
                if truck.status == TruckStatus.FREE  
            ]
        return []
    
    def bussy_truck(self, city: str) -> List[Truck]:
        if Map._valid_location(city):
            return [
                truck for truck in self.truckLocation.get(city, [])
                if truck.status == TruckStatus.BUSSY  
            ]
        return []

    def find_truck_by_id(self, vehicle_id: int) -> Optional[Truck]:
        return next(
            filter(lambda x: x.vehicle_id == vehicle_id, self.vehicles),
            None
        )
