from abc import ABC,abstractmethod

class User(ABC):
    NAME_MIN = 3
    NAME_MAX = 15
    def __init__(self, name: str, phone_number: str, email: str) ->None:
        self.name = name
        self.phone_number = phone_number
        self.email = email
        
    @property
    def name (self) -> None:
        return self._name 
    
    @name.setter
    def name(self, value:str) -> str:
        if not isinstance(value,str):
            raise ValueError('Name must be string.')
        if len(value) < self.NAME_MIN or len(value) > self.NAME_MAX:
            raise ValueError(f'Name must be {self.NAME_MIN} and {self.NAME_MAX} symbols')
        self._name = value
        
    @property
    def phone_number(self) -> None:
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self,value:str) ->str:
        if not value.startswith('04'):
            raise ValueError('Phone number start swith 04.')
        if len(value) != 10:
            raise ValueError('Phone number mustu be 10 digit long')
        self._phone_number = value
        
    @property
    def email(self) -> None:
        return self.email
    
    @email.setter
    def email(self,value:str) -> str:
        username, domain = value.split("@", 1)
        
        if not isinstance(value,str):
            raise ValueError('Email must be str')
        if '@' not in value:
            raise ValueError("Email must contain '@'.")
        if "." not in domain:
            raise ValueError("Email domain must contain a dot (e.g. 'gmail.com').")
        if not domain.endswith(".com"):
            raise ValueError("Email must end with '.com'.")
        self._email = value
        
    @abstractmethod
    def right_app(self):
        ...
    