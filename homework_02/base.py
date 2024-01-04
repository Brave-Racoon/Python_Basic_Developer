from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    weight = 25000
    started = False
    fuel = 200
    fuel_consumption = 25

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    # добавьте метод `start`. При вызове этого метода необходимо проверить состояние `started`. И если не `started`,
    # то нужно проверить, что топлива больше нуля,
    # и обновить состояние `started`, иначе нужно выкинуть исключение `exceptions.LowFuelError`
    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    # добавьте метод `move`, который проверяет,
    # что топлива достаточно для преодоления переданной дистанции (вплоть до полного расхода),
    # и изменяет количество оставшегося топлива, иначе выкидывает исключение `exceptions.NotEnoughFuel`
    def move(self, mileage):
        remaining_fuel = self.fuel - mileage * self.fuel_consumption
        if remaining_fuel >= 0:
            self.fuel = remaining_fuel
        else:
            raise exceptions.NotEnoughFuel
