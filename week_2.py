#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:02:18 2020

@author: smoneta
"""
# Week 2: Simple programs / Functions

# Excercise: square

def square(x):
    '''
    x: int or float.
    '''
    return x**2

# Excercise: evaluate quadratic
    
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return (a*(x**2))+(b*x)+c

# Exercise: Fouth power
    
def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    return square(x) * square(x)

# Excercise: Odd
    
def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    return x%2 != 0

# Excercise: Power iteration
    
def iterPower(base, exp):
        prod = base
        if exp == 1:
            return base
        elif exp == 0:
            return float(1)
        else:
            for i in range (1,exp):
                prod *=base
        
        return prod
    
# Excercise: Power recurtion
        
def recurPower(base,exp):     
     if exp == 1:
         return base
     elif exp == 0:
         return float(1)
     else:
         return base * (recurPower(base, exp-1))
     
# Excercise: Greatest common denomication (GDC) iteration
         
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    value = min(a,b)
    
    while a % value !=0 or b % value != 0:
        value -= 1
        
    return value 

# Excercise: Greatest common denomication (GDC) recursion
    
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur (b, a % b)
    
# Excersice: Is in
        
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1 and char != aStr:
        return False
    elif len(aStr) == 1 and char == aStr:
        return True
    elif char == aStr[len(aStr)//2]:
        return True
    else:
        if char > aStr[len(aStr)//2]:
            return isIn(char, aStr[len(aStr)//2:])
        else:
            return isIn(char, aStr[:len(aStr)//2])
        
# Grader: Polysum
            
from math import tan
import math
math.pi
def polysum (n, s):
    area = (0.25*n*(s**2))/ (tan(math.pi/n))
    perimeter= n * s
    sum = area + (perimeter**2)
    sum = round(sum, 4)
    return sum

# Problem set 2:

# Problem 1

month = 0
while month < 12:
    month +=1
    minPayment = (balance * monthlyPaymentRate)
    balance = balance - minPayment
    interest = balance * (annualInterestRate / 12)
    balance = balance + interest
print('Remaining balance: ' + "%.2f" % (balance))

# Problem 2

month = 0
original = balance
fixPayment = 10

while balance != 0 and balance > 0:
    fixPayment += 10
    balance = original
    while month < 12:
        month +=1     
        balance = balance - fixPayment
        monthRate = balance * (annualInterestRate/12)
        balance = balance + monthRate    
    month = 0
print ('Lowest Payment:',fixPayment)

# Problem 3

monthRate = annualInterestRate / 12
lowerBound = balance / 12
higherBound = (balance *(1+monthRate)**12)/12.0
left = balance
month = 0

while balance != 0:     
    x = ((lowerBound + higherBound) / 2)
    balance = left
    while month < 12:
        month +=1
        balance = balance - x
        interest = balance * (annualInterestRate / 12)
        balance = balance + interest
    month = 0
    if balance <= 0:
        higherBound = x
    elif balance >= 0:
        lowerBound = x
    balance = round(balance,2)
    
print('Lowest payment:', round(x,2))        



