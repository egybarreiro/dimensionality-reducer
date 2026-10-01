"""
Description: Define Car class
etc.....
"""


class Car:
    def __init__(self, color, brand, model, vin):
        self.color = color
        self.brand = brand
        self.model = model
        self.vin = vin

    def accelerate(self):
        return f"A {self.color}, {self.brand}, {self.model} is accelerating"

    def brake(self):
        return "The car is braking"