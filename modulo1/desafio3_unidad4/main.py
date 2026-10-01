'''
Desafío 3: Demostrar Herencia
Objetivo: Crea una clase Vehicle y dos subclases Car y Bike. 
Añade un método vehicle_type() en Vehicle que devuelva "Unknown",
 pero sobrescríbelo en Car y Bike para que devuelva "Car" y "Bike" respectivamente.

Resultado Esperado:

scss
my_vehicle = Vehicle()
my_car = Car()
my_bike = Bike()
print(my_vehicle.vehicle_type())  # "Unknown"
print(my_car.vehicle_type())      # "Car"
print(my_bike.vehicle_type())     # "Bike"
'''

'''
class Vehicle:

    def __init__(self, vehicle_type="Unknown", wheels_num=2):
        self.vehicle_type = vehicle_type
        self.wheels_num = wheels_num

    def __str__(self):
        return f'Vehicle Object: {self.vehicle_type}, {self.wheels_num}'

    def get_vehicle_type(self):
        return self.vehicle_type


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
'''

'''
Desafío 3: Demostrar Composición
Objetivo: Crea dos clases, Engine y Car. La clase Car debería usar una instancia de Engine. Implementa un método en Car para arrancar el motor.
Salida Esperada:
Cuando crees una instancia de Car y llames al método para arrancar, debería devolver un mensaje indicando que el motor ha arrancado
'''

