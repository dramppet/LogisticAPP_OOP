from abc import ABC, abstractmethod
class BaseCommand(ABC):
    def __init__(self, params, app_data):
        self._params = params
        self._app_data = app_data
    @abstractmethod
    def execute(self):
        raise NotImplementedError
