#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:33:30 2020

@author: smoneta
"""

# Week 4: Good programming

# excercise: Bugs

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count


# Excercise 6:
    
def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    print ('0- values:',x, a)
    print ("1- Is",x,"equal to",a,"?",(x == a))
    if x == a:
        return 0
    elif x < a:
        print ("2- Is",x,"less than",a,"?",(x < a))
        return x
    else:
        print ("3- Doing rem again with x been",x-a,"and a been",a)
        return rem(x-a, a) # here is the error, it have to RETURN the value of the function.
    

# Excercise 7
        
def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return n
   else:
      return n * f(n-1)

# Try & Catch until is OK

while True:
    try:
        number1 = int(input("Enter a number: "))
        number2 = int(input("Enter another number: "))
        print()
        print ("The sum os",number1,"and",number2,"is",number1+number2)
        break
    except:
        print(
            """
Sorry, the input is invalid
- Have to be an positive integer (ex: 1, 4, -19, -2)

Try again.
            
            """
            )
print()
print("Thanks, see you later!")


# Try , Catch, else and finally

def test(list):
    # test the function with a list of items (ex. test(['a','b','c']))
    try:
        for i in range(len(list)):
            print(list[i])
    except:
        print('error')
    else:
        print(i,'else')
    finally:
        print(i,'finally')
        
# Excersice simpe divide:

def fancy_divide(list_of_numbers, index):
       denom = list_of_numbers[index]
       return [simple_divide(item, denom) for item in list_of_numbers]
   
def simple_divide(item, denom):
    try:
       return item / denom
    except ZeroDivisionError:
        return 0
    
# Assersion sample

def normalize(x):
    # If the following is TRUE, the code stops
    assert (type(x) == int), "Sorry, the input have to be an integer"
    assert (x >= 1 and x <= 10), "Sorry, the number have to be between 1 and 10"
    
    # If the above is FALSE, it continue
    print ('valid input')
    return x    



