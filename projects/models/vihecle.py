class Vehicle:
    def __init__(self, id: int, name: str, capacity: int, max_range: int) -> None:
        self.truck_id = id
        self.name = name
        self.capacity = capacity
        self.max_range = max_range
        self.truck_free = True
        
    def truck_buzy(self):
        self.truck_free = False
    
    def truck_no_buzy(self):
        self.truck_free = True    
