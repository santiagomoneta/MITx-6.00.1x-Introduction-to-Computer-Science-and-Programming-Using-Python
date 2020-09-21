#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:11:59 2020

@author: smoneta
"""

# Week 3: Structured Types

# Excercise: Odd tuples

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    bTup = ()
    count = 0
    for i in aTup:
        if count%2 == 0:
            bTup = bTup + (i,)
        
        count +=1
    return bTup 

# Excercise: Apply to each
    
def absolute(a):
        return abs(a)
applyToEach(testList, absolute)

# Excercise: How many

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    values = aDict.values()
    count = 0
    for i in values:
        for x in i:
            count +=1
    return count

# Excersice: Biggest
    
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''

    values = aDict.values()
    best = max(values)
    for i in aDict:
        if aDict[i] == best:
            biggest = i
    return biggest

# Problem set 3
    
# Problem 1
    
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for w in secretWord:
        if w not in lettersGuessed:
            return False
    return True 

# Problem 2
    
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    tempWord = ''
    for w in secretWord:
        if w in lettersGuessed:
            tempWord = tempWord+w
        else:
            tempWord = tempWord+'_'
    return tempWord 

# problem 3
    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    letters = string.ascii_lowercase 
        
    for i in lettersGuessed:
        if i in letters:
            letters = letters.replace(i,'')
    return letters 

# Problem 4
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lives = 8
    lettersGuessed = []
    lettersUsed = []
    
    print ('Welcome to the game, Hangman!')
    print (	'I am thinking of a word that is',len(secretWord),'letters long.')

    while lives >= 1 and isWordGuessed != True:
        print ('-----------')
        print ('You have',lives,'chances left')
        print ('Available letters:',getAvailableLetters(lettersUsed))
        letter = input('Please guess a letter: ')                  
        if letter in lettersUsed:
                print ("Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersUsed.append(letter)            
            if letter in secretWord:
                lettersGuessed.append(letter)
                print ('Good guess:',getGuessedWord(secretWord, lettersGuessed))
                if (isWordGuessed(secretWord, lettersGuessed)) == True:
                    break
                    
            else:
                print ('Oops! That letter is not in my word:',getGuessedWord(secretWord, lettersGuessed))
                lives -=1
    print ('-----------')      
    if lives == 0:
        print ('Sorry, you ran out of guesses. The word was else.')
    else:
        print ('Congratulations, you won!')
        
