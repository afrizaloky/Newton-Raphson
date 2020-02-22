#!/usr/bin/env python3
from sympy import *
from math import *
from prettytable import PrettyTable


# Definition Function
x = var('x')
user_input = input("Enter the function (x**2 + 2*x + 2) = ")
expr = sympify(user_input)
x_old = float(input("Enter the value of X0 = "))
RAE = float(input("Enter the value of tollerance (0.0001) = "))
RAE_now = 100
t = PrettyTable()
t.field_names = ["i", "xi", "Aproximation Error"]
counter = 0


def f(value):

    res = expr.subs(x, value)
    return res


def derive(value):
    x = Symbol('x')
    derive = diff(expr, x)
    return derive.subs(x, value)


def newton(x_old):
    x_new = x_old - f(x_old)/derive(x_old)
    return x_new


while RAE < RAE_now:
    x_new = newton(x_old)
    selisih = abs(x_new-x_old)
    RAE_now = abs(selisih/x_new)
    x_old = x_new
    t.add_row([counter, x_new, RAE_now])
    counter = counter+1

print(t)
