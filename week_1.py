#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:02:18 2020

@author: smoneta
"""

# Week 1: python Basics / 2 Core elements of programs

# Excerise: hello world

print ("hello world")

# Excercise: happy

if happy > 2:
    print ("hello world")
    
# Excercise: while

x = 2
while x <= 10:
    print (x)
    x +=2
print ("Goodbye!")

# Excercise: for

x = 2
while x <= 10:
    print (x)
    x +=2
print ("Goodbye!")
    
# Problem set 1

# Problem 1

count = 0
for x in s:
    if x in ['a','e','i','o','u']:
        count += 1
print ('Number of vowels: ',count)
        
# Problem 2

count = 0
for i in range(len(s)):
    if (s[i:i+3] == 'bob'):
        count +=1
print ("Number of times bob occurs is: ",count)

# Problem 3

current = ''
longest = ''
for i in range(len(s)):
 if (s[i] >= s[i-1]):
  current += s[i]
 else:
  current = s[i]
 if len(current) > len(longest):
  longest = current
print("Longest substring in alphabetical order is: " + longest)