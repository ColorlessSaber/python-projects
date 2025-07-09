"""
Below shows how one class can inherit attributes and methods from another class
"""

class GasEngine:
    """
    A class for a gas powered engine. Has attributes for: number of cylinders, number of turbos or superchargers,
    max horsepower, and engine name.
    """
    number_of_cylinders = 0
    number_of_turbos = 0
    number_of_supercharger = 0
    max_horse_power = 0
    engine_description = ''

class SportCar(GasEngine):
    """
    A class for holding a sport car. Inherits the GasEngine
    """
    price = "$1000000"
    quality = "high"
    car_name = "Bugatti Veyron"
    def __init__(self):
        self.number_of_cylinders = 16
        self.number_of_turbos = 4
        self.max_horse_power = 1000
        self.engine_description = "Two V8 with four turbo chargers"

class VanCar(GasEngine):
    """
    A class for holding a van car. Inherits the GasEngine
    """
    price = "$51000"
    quality = "mid"
    car_name = "Toyota Van"

    def __init__(self):
        self.number_of_cylinders = 8
        self.max_horse_power = 502
        self.engine_description = "Eco-Friendly V8"