from engine.engine import Engine


class CapuletEngine(Engine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = int(current_mileage)
        self.last_service_mileage = int(last_service_mileage)

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000