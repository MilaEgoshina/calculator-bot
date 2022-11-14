from fractions import Fraction
import re
from math import gcd

def calculate_float_rational_numbers(x,y,operation):# функция для вычисления чисел типа float
    match operation:
        case '+' : return str(x + y)
        case '-': return str(x - y)
        case '*': return str(x * y)
        case '/': 
            if float(y) == 0.0:
                return 'На ноль делить нельзя'
            else:
                return str(x / y)


def calculate_drob_rational_numbers(x,y,operation):#функция для вычисления дробей только простого вида x/y ,где x - числитель, y - знаменатель 
    match operation:
        case '+': return f'{Fraction(x).numerator * Fraction(y).denominator + Fraction(y).numerator * Fraction(x).denominator}/{Fraction(x).denominator * Fraction(y).denominator}'
        case '-': return f'{Fraction(x).numerator * Fraction(y).denominator - Fraction(y).numerator * Fraction(x).denominator}/{Fraction(x).denominator * Fraction(y).denominator}'
        case '*': return f'{Fraction(x).numerator * Fraction(y).numerator}/{Fraction(x).denominator * Fraction(y).denominator}'
        case '/': return f'{Fraction(x).numerator * Fraction(y).denominator}/{Fraction(x).denominator * Fraction(y).numerator}'

def parsing_of_rational_number(num):#функция, которая приводит число к виду простой дробви х/у, если в дроби есть целое число
    res = re.split(' |/',num)
    # print(res)
    zhak = ''
    if len(res) > 2:# в этом условии и определяем есть ли целочисленная часть у дроби, или же нет
        if int(res[0]) < 0:
            zhak = '-'
            res[0] = f'{abs(int(res[0]))}'
        return f'{zhak}{int(res[0]) * int(res[2]) + int(res[1])}/{res[2]}'#целое число умножаем на знаменатель и плюсуем  числитель, в знаменателе остается изначальный знаменатель
    else:
        return num


def parsing_to_integer_part(num):#функция для выделения целочисленной части в дроби и сокращения числителя с знаменателем для красивого вывода пользователю
    res = (list(map(int,num.split('/'))))
    # print(res)
    znak = ''
    if res[0] < 0:
        znak = '-'
        res[0] = int(res[0]) * (-1)
    if (len(res)) < 2:#если число целое, то просто возвращаем это число
        return f'{num}'
    elif res[1] == 1:# если знаменатель равен 1, то возвращаем просто числитель
        return f'{res[0]}'
    elif res[0] == 0:# если числитель равен 0, то возвращаем этот ноль
        return f'{res[0]}'
    elif res[1] == 0:#если знаменатель равен 0, то на ноль делить нельзя
        return 'На ноль делить нельзя'
    elif res[0] == res[1]:#если числитель и знаменатель равны , то возвращаем 1 с соответствующим знаком
        return f'{znak}1'
    elif res[0] > res[1]:#если же числитель больше чем знаменатель, то выделяем целую часть и сокращаем дробь 
        integer_part = int(res[0] / res[1])
        nod = gcd(res[0],res[1])
        res[0] = int(res[0] / nod)#сокращаем оставшуюся дробь 
        res[1] = int(res[1] / nod)#сокращаем оставшуюся дробь 
        if (res[0] - integer_part * res[1]) == 0: #делиться целочисленно, возвращаем целое число с соответствующим знаком
            return f'{znak}{integer_part}'
        else:#если не делиться целочисленно, то возвращаем целую часть вместе с дробной частью
            return f'{znak}{integer_part} {res[0] - integer_part * res[1]}/{res[1]}'
    else:#в остальных случаях мы просто сокращаем дробь с помощью НОД и возвращаем ее
        nod = gcd(res[0],res[1])
        return f'{res[0] / nod} / {res[1] / nod}'

def calculation(x,y,operation):
    if type(x) == str and type(y) == str:
        if x.find('/') < 0 and y.find('/') < 0:
            x1 = float(x)
            y1 = float(y)
            return calculate_float_rational_numbers(x1,y1,operation)
        else:
            if x[x.find('/') + 1] == '0' or y[y.find('/') + 1] == '0':
                return 'На ноль делить нельзя '
            else:
                return parsing_to_integer_part(calculate_drob_rational_numbers(parsing_of_rational_number(x),parsing_of_rational_number(y),operation))


     
print(calculation('4/5','5/4','+'))


    
    

    
