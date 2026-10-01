class Service:

    services_list = ['tire_rotation', 'oil_change']

    def __init__(self, name, service_type, price, service_time):
        self.name = name
        self.service_type = service_type
        self.price = price
        self.service_time = service_time

    def charge_service(self):
        return f'Your total is {self.price}.'

    def notify_start_service(self):
        return f'Your service {self.name}, has started'

    def notify_end_service(self):
        return f'Your service {self.name}, has ended'


class Invoice:

    def __init__(self, car, service, phone_number):
        self.car = car
        self.service = service
        self.phone_number = phone_number

    def print_invoice(self):
        return f'Service invoice: {self.car.vin}, {self.service.price}.'
