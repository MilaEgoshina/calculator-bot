from fractions import Fraction
import re
from math import gcd

def calculate_float_rational_numbers(x,y,operation):#для вычисления чисел с плавающей запятой 
    match operation:
        case '+' : return str(x + y)
        case '-': return str(x - y)
        case '*': return str(x * y)
        case '/': 
            if float(y) == 0.0:
                return 'На ноль делить нельзя'
            else:
                return str(x/y)


def calculate_drob_rational_numbers(x,y,operation):#для вычисления дробей простого вида x/y ,x - числитель, y - знаменатель 
    match operation:
        case '+': return f'{Fraction(x).numerator * Fraction(y).denominator + Fraction(y).numerator * Fraction(x).denominator}/{Fraction(x).denominator * Fraction(y).denominator}'
        case '-': return f'{Fraction(x).numerator * Fraction(y).denominator - Fraction(y).numerator * Fraction(x).denominator}/{Fraction(x).denominator * Fraction(y).denominator}'
        case '*': return f'{Fraction(x).numerator * Fraction(y).numerator}/{Fraction(x).denominator * Fraction(y).denominator}'
        case '/': return f'{Fraction(x).numerator * Fraction(y).denominator}/{Fraction(x).denominator * Fraction(y).numerator}'

def parsing_of_rational_number(num):#приводит число к виду простой дробви х/у для дальнейшего вычисления
    res = re.split(' |/',num)
    zhak = ''
    if len(res) > 2:
        if int(res[0]) < 0:
            zhak = '-'
            res[0] = f'{abs(int(res[0]))}'
        return f'{zhak}{int(res[0]) * int(res[2]) + int(res[1])}/{res[2]}'
    else:
        return num


    
