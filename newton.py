#!/usr/bin/env python3
from sympy import var
from sympy import sympify
from math import *
#from tabulate import tabulate

#Definition Function
x = var('x')  # the possible variable names must be known beforehand...
user_input = input("Enter the function (X**2 + 2*x + 2) = ")
expr = sympify(user_input)
x_old = float(input("Enter the value of X0 = "))
RAE = float(input("Enter the value of tollerance (0.0001) = "))
RAE_now = 100

def f(value):
	
	res = expr.subs(x, value)
	return res

def derive(f, value):
	
	h= 0.00000000001
	top = f(value + h) - f(value)
	bottom = h
	slope = top/bottom
	return float("%.3f" % slope)

def newton(x_old):
	x_new = x_old - f(x_old)/derive(f, x_old)
	return x_new


print(" \tX\t\tRAE")
while RAE<RAE_now:
	x_new = newton(x_old)
	selisih = abs(x_new-x_old)
	RAE_now = abs(selisih/x_new)
	print
	print("", x_new, RAE_now)
	
	x_old = x_new
