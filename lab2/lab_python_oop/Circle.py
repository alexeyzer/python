from lab_python_oop.color import *
from lab_python_oop.figure import *
import math

class Circle(Figure):

    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self,color, radius):
        self.radius = radius
        self.clrcls = Color()
        self.clrcls.colorproperty = color

    def square(self):
        return math.pi * (self.radius**2)

    def __repr__(self):
        return '{} {} цвета с радиусом {} площадью {}.'.format(
            Circle.get_figure_type(),
            self.clrcls.colorproperty,
            self.radius,
            self.square()
        )
