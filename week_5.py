#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:08:03 2020

@author: smoneta
"""

# Weeks 5
# Exercise: coordinate

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__ (self, other):
        assert  type(other) == type(self)
        return self.getX() == other.getX() and self.getY() == other.getY()
    
    def __repr__ (self):
        return 'Coordinate(' + str(self.x) + ',' + str(self.y) + ')'


# Exercise: int set
        
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect (self, other):
        assert type(self) == type(other)
        newset = intSet()
        for i in range(len(self.vals)):
            if self.vals[i] in other.vals:
                newset.insert(self.vals[i])
        return newset
    def __len__(self):
        return len(self.vals)
    
# Exercise: spell    

class Spell(object):
    def __init__(self, spellName, spellType):
        self.spellName = spellName
        self.spellType = spellType
        
    def __str__(self):
        return str(self.getDescription)

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm') 
    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'

# Exercise: hand

        handCopy = self.hand.copy()
        try:
            for letter in word:
                if self.hand[letter] > 0:
                    self.hand[letter] -= 1
                else:
                    self.hand = handCopy.copy()
                    return False
        except KeyError:
            self.hand = handCopy.copy()
            return False
        else:
            return True
            
        raise NotImplementedError()
        
        
# Exercise: genPrimes

def genPrimes():
    primes = [2]
    yield primes[0]
    guess = 3
    while True:
        if all(guess%x != 0 for x in primes):
            primes.append(guess)        
        if guess == primes[-1]:
            yield primes[-1]
        guess += 2
        
# Problem set 5 / problem 1

class Message(object):
    def __init__(self, text):
        self.message_text = text
        self.words = load_words(WORDLIST_FILENAME)
        
    def get_message_text(self):
        return self.message.text
    
    def get_valid_words(self):
        return self.valid_words[:]
    
    def build_shift_dict(self,shift):
        lower_keys = list(string.ascii_lowercase)
        lower_values = list(string.ascii_lowercase)
        shift_lower_values = lower_values[shift:] + lower_values[:shift]
        
        upper_keys = list(string.ascii_uppercase)                 
        upper_values = list(string.ascii_uppercase)
        upper_shift_values = upper_values[shift:] + upper_values[:shift]

        full_keys = lower_keys + upper_keys
        full_values = shift_lower_values + upper_shift_values

        self.shift_dict = dict(zip(full_keys, full_values))
        return self.shift_dict
    
    def apply_shift(self, shift):
        new_msg = []
        for i in self.message_text:
            if i not in self.build_shift_dict(shift).keys():
                new_msg.append(i)
                continue
            else:
                new_msg.append(self.build_shift_dict(shift)[i])
        return ''.join(new_msg)
    
# Problem set 5 / problem 2

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        self.shift = shift
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.encrypting_dict = super(PlaintextMessage, self).build_shift_dict(shift)
        self.message_text_encrypted = super(PlaintextMessage, self).apply_shift(shift)

    def get_shift(self):
        return self.shift

    def get_encrypting_dict(self):
        encrypting_dict_copy = self.encrypting_dict.copy()
        return encrypting_dict_copy

    def get_message_text_encrypted(self):
        return self.message_text_encrypted

    def change_shift(self, shift):
        self.shift = shift
        self.encrypting_dict = super(PlaintextMessage, self).build_shift_dict(shift)
        self.message_text_encrypted = super(PlaintextMessage, self).apply_shift(shift)
     
# Problem set 5 / problem 3

class CiphertextMessage(Message):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        word_counter = 0
        max_count = 0
        for i in range(26):
            for j in list(super(CiphertextMessage, self).apply_shift(i).split(' ')):
                if is_word(self.valid_words, j):
                    word_counter += 1
                if word_counter > max_count:
                    max_count = word_counter
                    shift_value = i
                    decrypted_msg = super(CiphertextMessage, self).apply_shift(i)                  
        return (shift_value, decrypted_msg)

# Problem set 5 / problem 4

def decrypt_story():
    joke_code = CiphertextMessage(get_story_string())
    return joke_code.decrypt_message()
