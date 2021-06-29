"""
Usados para que las funciones acepten cualquier cantidad
de parametros
"""


# *args devuelve una tupla
def total_elements(*args):
    _sum = 0
    for element in args:
        _sum += element
    return _sum


# *kwargs devuelve un dict
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand


class Tesla(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.brand = "Tesla"


if __name__ == '__main__':
    print(total_elements(1, 2, 3, 4, 5, 6))
    tesla_car = Tesla(
        color="black",
        brand="Tesla"
    )
    print(tesla_car.color)


