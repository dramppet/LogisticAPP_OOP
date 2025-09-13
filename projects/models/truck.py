from status.truck import TruckStatus

class Truck:
    def __init__(self,vehicle_id: int, name: str, capacity: int, max_range: int) -> None:
        self.vehicle_id = vehicle_id
        self.name = name
        self.capacity = capacity
        self.max_range = max_range
        self.status  = TruckStatus.FREE
        self.route = None
        self.location = None
        
        
        
    