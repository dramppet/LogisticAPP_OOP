from models.user import User

class Customer(User):
    def __init__(self,name,phone_number,email):
        super().__init__(name,phone_number,email)
    
    #TODO    
    def right_app(self):
        ...
        