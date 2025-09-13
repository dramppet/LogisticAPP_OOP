from status.truck import TruckStatus

class Truck:
    _MAX_SPEED  = 87
    def __init__(self,vehicle_id: int, name: str, capacity: int, max_range: int) -> None:
        self.vehicle_id = vehicle_id
        self.name = name
        self.capacity = capacity
        self.max_range = max_range
        self.status  = TruckStatus.FREE
        self.route = None
        self.location = None
        
        
    def info(self) -> str:
       return (
            f"Vehicle_id: {self.vehicle_id}\n"
            f"Name: {self.name}\n"
            f"Capacity: {self.capacity}\n"
            f"Max range: {self.max_range}\n"
            f"Status: {self.status}\n"
            f"Location: {self.current_location or 'Unknown'}"
        )
        
        
        
    