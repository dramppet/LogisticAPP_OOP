import random  
from typing import Dict,List 
from models.truck import Truck 
from manager.map import Map 
from status.truck import TruckStatus
 
class VehicleManager: 
    def __init__(self): 
        self.vehicles = (
            [Truck(vehicle_id, "Scania", 42000, 8000) for vehicle_id in range(1001, 1011)] 
            + [Truck(vehicle_id, "Man", 37000, 10000) for vehicle_id in range(1011, 1026)] 
            + [Truck(vehicle_id, "Actros", 26000, 13000) for vehicle_id in range(1026, 1041)]) 
        self.disperse_trucks() 
        self.truckLocation: Dict[str,List[Truck]] = {} 
        
    def disperse_trucks(self):
        
        for location in Map._locations:
            selected = random.sample(self.vehicles, 6)
   
        for truck in selected:
            truck.location = location
        self.truckLocation[location] = selected
        
        return self.truckLocation
    
    def free_truck(self, city: str) -> List[Truck]:
        
        if Map._valid_location(city):
            return [truck for truck in self.truckLocation.get(city, []) if truck.status == TruckStatus.Free] 
            return [] 
        
    def find_truck_by_id(self, vehicle_id: int) -> int: 
        return next(filter(lambda x: x.vehicle_id == vehicle_id ,self.vehicles),None) 
