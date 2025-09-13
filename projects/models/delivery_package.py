
class DeliveryPackage:
    __unique_package_id = 1

    def __init__(self, start_location: str, end_location: str,
                 weight: float, info):
        self._unique_package_id = DeliveryPackage.__unique_package_id
        DeliveryPackage.__unique_package_id += 1  
        self.start_location = start_location
        self.end_location = end_location
        self.weight = weight
        self.info= info

    @property
    def unique_package_id(self):
        return self._unique_package_id

        