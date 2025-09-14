from base_commands import BaseCommand
from helpers.validation_helpers import validate_params_count
from projects.exception.invalid_length import InvalidLengthParamsExseption
from core.application_data import AplicationData

class CreateRoute(BaseCommand):
    def execute(self):
        if validate_params_count(self._params,2):
            raise InvalidLengthParamsExseption("Invalid params: need at least 2 locations.")
        
        route = self
        
        return(f"Route #{route.route_id} created: {' -> '.join(route.location)}")
