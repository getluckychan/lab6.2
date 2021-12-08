from main import Fraction
from exeptions import Sign
from sys import exit
from copy import copy

def main():
    try:
        a = Fraction(None)
        a.read()
        a.display()
    except Sign:
        exit("Введіть + або - або нічого")
    except ValueError:
        exit("Введіть цілі числа")


main()
