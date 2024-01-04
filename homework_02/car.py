"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


# в модуле `car` создайте класс `Car`
# класс `Car` должен быть наследником `Vehicle`
class Car(Vehicle):
    # добавьте атрибут `engine` классу `Car`
    engine = 0

    # объявите метод `set_engine`, который принимает в себя экземпляр объекта `Engine` и
    # устанавливает на текущий экземпляр `Car`
    def set_engine(self, engine):
        self.engine = engine
