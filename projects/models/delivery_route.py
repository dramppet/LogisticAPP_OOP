class DeliveryRoute:
    _next_id = 1
    def __init__(self,start_location:str, end_location: str, *location) -> None:
        self.route_id = DeliveryRoute._next_id
        DeliveryRoute._next_id +=1
        self.start_location = start_location
        self.end_location = end_location
        self.location = []
        