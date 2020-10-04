from lab_python_oop.ractangle import *
from lab_python_oop.Circle import *
from lab_python_oop.square import *
from more_itertools import *

def main():
    rect = Rectangle("Синего", 6, 5)
    circ = Circle("Красного", 5)
    sqr = Square("квадрат", 6)
    print(rect)
    print(circ)
    print(sqr)
    a = list(chunked([1, 2, 3, 4, 5, 6], 2))
    print(a)

if __name__ == '__main__':
    main()
