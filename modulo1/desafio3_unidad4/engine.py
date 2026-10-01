class Vehicle:

    def __init__(self, vehicle_type="Unknown", wheels_num=2):
        self.vehicle_type = vehicle_type
        self.wheels_num = wheels_num

    def __str__(self):
        return f'Vehicle Object: {self.vehicle_type}, {self.wheels_num}'

    def get_vehicle_type(self):
        return self.vehicle_type

class Engine:
    def __init__(self, is_running = True):
        self.is_running = is_running

    def __str__(self):
        if self.is_running:
            return 'The engine is running'
        return 'The engine is not running'

class Car(Vehicle):

    def __init__(self):
        super().__init__(wheels_num=4, vehicle_type='Car')

    def __str__(self):
        return f'Car Object: {self.vehicle_type}, {self.wheels_num}'


class Bike(Vehicle):

    def __init__(self):
        super().__init__(wheels_num=2, vehicle_type='Bike')

    def __str__(self):
        return f'Bike Object: {self.vehicle_type}, {self.wheels_num}'