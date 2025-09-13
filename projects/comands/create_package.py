from comands.base_commands import BaseCommand
from helpers.validation_helpers import validate_params_count
#start location, end location, weight in kg and contact information
class CreatePackage(BaseCommand):
    def exsecut(self):
     validate_params_count(self._params,4):
         
    