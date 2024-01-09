"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class MyExceptions(BaseException):
    pass


class LowFuelError(MyExceptions):
    pass


class NotEnoughFuel(MyExceptions):
    pass


class CargoOverload(MyExceptions):
    pass
