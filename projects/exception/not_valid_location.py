class NotValidLocationException(Exception):
    def __init__(self, msg: str = 'Invalid location' ):
        super().__init__(msg)
        self._msg = msg
        
