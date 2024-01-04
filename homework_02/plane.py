"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02 import exceptions
# в модуле `plane` создайте класс `Plane`
# класс `Plane` должен быть наследником `Vehicle`


class Plane(Vehicle):
    # добавьте атрибуты `cargo` и `max_cargo` классу `Plane`
    cargo = 0
    max_cargo = 0

    # добавьте `max_cargo` в инициализатор (переопределите родительский)
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    # объявите метод `load_cargo`, который принимает число, проверяет, что в сумме с текущим `cargo`
    # не будет перегруза, и обновляет значение, в ином случае выкидывает исключение `exceptions.CargoOverload`
    def load_cargo(self, curr_cargo):
        res = self.cargo + curr_cargo
        if res <= self.max_cargo:
            self.cargo = res
        else:
            raise exceptions.CargoOverload

    # объявите метод `remove_all_cargo`, который обнуляет значение `cargo` и возвращает значение `cargo`,
    # которое было до обнуления
    def remove_all_cargo(self):
        res = self.cargo
        self.cargo = 0
        return res
