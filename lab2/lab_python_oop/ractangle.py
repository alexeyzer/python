from lab_python_oop.figure import *
from lab_python_oop.color import *

class Rectangle(Figure):

    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color, width, height):
        self.width = width
        self.heigth = height
        self.clcls = Color()
        self.clcls.colorproperty = color

    def square(self):
        return self.width * self.heigth

    def __repr__(self):
        return '{} {} цвета с шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.clcls.colorproperty,
            self.width,
            self.heigth,
            self.square()
        )