from utils import gdc

class Fraction:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self):
        return f"{self.__numerator} / {self.__denominator}"

    def __add__(self, other):
        lower_num = (self.__denominator * other.__denominator) / gdc(self.__denominator, other.__denominator)
        higher_num = self.__numerator * (lower_num / self.__denominator) + other.__numerator * (lower_num / other.__denominator)

        if gdc(higher_num, lower_num) != 1:
            local_gdc = gdc(higher_num, lower_num)
            higher_num /= local_gdc
            lower_num /= local_gdc

        return Fraction(higher_num, lower_num)

    def __sub__(self, other):
        lower_num = (self.__denominator * other.__denominator) / gdc(self.__denominator, other.__denominator)
        higher_num = self.__numerator * (lower_num / self.__denominator) - other.__numerator * (lower_num / other.__denominator)

        if gdc(higher_num, lower_num) != 1:
            local_gdc = gdc(higher_num, lower_num)
            higher_num /= local_gdc
            lower_num /= local_gdc

        return Fraction(higher_num, lower_num)

    def inverse(self):
        return Fraction(self.__denominator, self.__numerator)

