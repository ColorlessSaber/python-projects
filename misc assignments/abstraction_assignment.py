"""
An example of using abstractmethod in a class and defining it in another class
"""
from abc import ABC, abstractmethod
class Vehicle(ABC):
    """
    Class for generic vehicle
    """
    @abstractmethod
    def engine_type(self):
        pass

class ElectricCar(Vehicle):
    """
    Class for electric cars
    """
    def engine_type(self):
        return 'electric motor'

if __name__ == '__main__':
    electric_spot_car = ElectricCar()
    print(electric_spot_car.engine_type())