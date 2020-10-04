import math
import cmath
import sys

def inpf(coef):
    try:
        a = float(input("Введите коэффициент {0}\n".format(coef)))
    except:
        a = inpf(coef)
    return a

def basic(a, b, c):
    d = pow(b,2) - (4 * a * c)
    if d > 0:
        x = ((-b + math.sqrt(d)) / (2 * a))
        if x <= 0:
            x1 = cmath.sqrt(x)
        else:
            x1 = math.sqrt(x)
        print("x1 = {0}".format(x1))
        print("x2 = -{0}".format(x1))
        x = ((-b - math.sqrt(d)) / (2 * a))
        if x <= 0:
            x2 = cmath.sqrt(x)
        else:
            x2 = math.sqrt(x)
        print("x3 = {0}".format(x2))
        print("x4 = -{0}".format(x2))
    else:
        print("Корней нет")

def twoab(a, b):
    print("x1 = 0")
    print("x2 = 0")
    x1 = (-b / a)
    if  x1 >= 0:
        x1 = math.sqrt(x1)
    else:
        x1 = cmath.sqrt(x1)
    print("x3 = {0}".format(x1))
    print("x4 = -{0}".format(x1))
def twoac(a, c):
    x1 = (-c / a)
    if x1 >= 0:
        x1 = math.sqrt(x1)
        if x1 >= 0:
            x1 = math.sqrt(x1)
            x2 = cmath.sqrt(-x1)
        else:
            x1 = cmath.sqrt(x1)
            x2 = math.sqrt(-x1)
    else:
        x1 = cmath.sqrt(x1)
        x2 = cmath.sqrt(-x1)
    print("x1 = {0}".format(x1))
    print("x2 = -{0}".format(x1))
    print("x3 = {0}".format(x2))
    print("x4 = -{0}".format(x2))

print("Зудин Алексей Максимович  ИУ5-43Б")
a = 0
b = 0
c = 0
if len(sys.argv) == 4:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
if a == 0 and b == 0 and c == 0:
    a = inpf("A")
    b = inpf("B")
    c = inpf("C")
if a != 0 and b != 0 and c != 0:
    basic(a, b, c)
if a != 0 and b != 0 and c == 0:
    twoab(a,b)
if a != 0 and b == 0 and c != 0:
    twoac(a, c)
if a == 0 and b == 0 and c != 0:
    print("Нет решений")
if a != 0 and b == 0 and c == 0:
    print("Решений нет")
if a == 0 and b != 0 and c == 0:
    print("X = 0")
if a == 0 and b == 0 and c == 0:
    print("Бесконечное количество решений")