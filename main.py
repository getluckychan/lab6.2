from random import randint
from exeptions import Sign


class Fraction:
    def __init__(self, x):
        self.x = x
        self.y = None
        self.sign = None

    def set_y(self, y):
        numbers = [randint(0, 9) for i in range(y)]
        self.y = int(''.join(map(str, numbers)))

    def get_y(self):
        return self.y

    def set_sign(self, sign):
        if sign == '-' or sign == '+' or sign == '':
            self.sign = sign
        else:
            raise Sign

    def get_sign(self):
        return self.sign

    def to_float(self):
        return float(str(self.sign) + str(self.x) + "." + str(self.y))

    def display(self):
        print(self.to_float())

    def read(self):
        self.__init__(int(input("Введіть цілу частину: ")))
        self.set_y(int(input("введіть кількість цифр після коми: ")))
        self.set_sign(input("Введіть знак: "))

    def __copy__(self):
        print('copying ...')
        my_copy = type(self)(1)
        my_copy.__dict__.update(self.__dict__)
        return my_copy

    def __del__(self):
        print("Видалення всіх значень")
        del self.sign, self.x, self.y




