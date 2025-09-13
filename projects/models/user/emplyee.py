from models.user import User


class Employee(User):
    def __init__(sefl, name, phone_number, email):
        super().__init__(name, phone_number, email)

    # TODO
    def right_app(self): ...
