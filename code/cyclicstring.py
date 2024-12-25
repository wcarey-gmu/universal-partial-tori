#!/usr/bin/env python3
###############################################################################
#
#  Project:  MEGL Universal Partial Tori
#  Authors:  William Carey <wcarey1@gmu.edu>
#            Matthew Kearney <mkearne@gmu.edu>
#            Rachel Kirsch <rkirsch4@gmu.edu>
#            Stefan Popescu <spopesc@gmu.edu>
#
#  Acknowledgements: We would like to thank the Mason Experimental Geometry 
#                    Lab (MEGL) for supporting this project and Charles 
#                    Landreaux for collaboration in early stages of the 
#                    research. The third author is supported in part by 
#                    Simons Foundation Grant MP-TSM-00002688.
# 
#  Copyright (c) 2023-2024, William Carey, Matthew Kearney, Rachel Kirsch, Stefan Popescu
#  SPDX-License-Identifier: MIT
#

class CyclicString(object):
    def __init__(self, alphabet, length):
        self.alphabet = alphabet
        self.length = length
        self.values = " " * length

# Value Setters/Getters ----------------------------------------------------- #

    def __str__(self):
        return self.values
    
    def setValueAt(self, position, value):
        v = list(self.values)
        v[position] = value
        self.values = "".join(v)
        
    def setValues(self, values):
        assert(len(values) == self.length)
        self.values = values
        
    def valueAt(self, index):
        s = list(self.values)
        if (index < 0):
            index = index + self.length
        index = index % self.length
        return self.values[index]
    
    def valuesAt(self, index, length):
        s = list(self.values)
        result =""
        if (index < 0):
            index = index + self.length
        index = index % self.length
        for offset in range(0, length):
            result += self.valueAt(index + offset)
        return result

# Rotation ------------------------------------------------------------------ #
 
    def rotateLeftBy(self, offset):
        self.values = self.values[offset:] + self.values[:offset]
    
    def rotateRightBy(self, offset):
        self.values = self.values[self.length-offset:] + self.values[:-offset]
    
    def rotateLeft(self):
        self.rotateLeftBy(1)
    
    def rotateRight(self):
        self.rotateRightBy(1)

# Alphabet Multiplier Shenanigans ------------------------------------------- #

    def add(self, cyclicString):
        """Returns the result of component-wise adding each element of this 
           cyclic string to the corresponding element of @cyclicString. 
           Treats a + w = w for all a. Alphabet must be embiggened first. 
           Modifies this CyclicString in place."""
        assert(len(self.values) == len(cyclicString.values))
        for x in range(0, len(self.values)):
            if self.values[x] == self.alphabet.wildcard:
                continue
            elif cyclicString.values[x] == self.alphabet.wildcard:
                self.setValueAt(x, self.alphabet.wildcard)
            else:
                newValue = str(int(self.values[x]) + int(cyclicString.values[x]))
            assert(newValue in self.alphabet.symbols)
            self.setValueAt(x, newValue)

    def scalarMultiply(self, multiplier):
        vs = list(self.values)
        for x in range(0, len(vs)):
            if vs[x] == self.alphabet.wildcard:
                vs[x] = self.alphabet.wildcard
            else:
                vs[x] =str(int(vs[x]) * multiplier)
        self.values = "".join(vs)

    def multiply(self, cyclicString):
        """Returns the result of component-wise multplication of each element"""
        assert(len(self.values) == len(cyclicString.values))
        for x in range(0, len(self.values)):
            if self.values[x] == self.alphabet.wildcard:
                continue
            elif cyclicString.values[x] == self.alphabet.wildcard:
                self.setValueAt(x, self.alphabet.wildcard)
            else:
                newValue = str(int(self.values[x]) * int(cyclicString.values[x]))
            assert(newValue in self.alphabet.symbols)
            self.setValueAt(x, newValue)

    def concatenate(self, count):
        self.length = self.length * count
        self.values = self.values * count
        
    def stripWildcards(self):
        self.values = self.values.replace(self.alphabet.wildcard, "")
        self.length = len(self.values)

# Covering Structures ------------------------------------------------------- #
    
    def substringCount(self, substring):
        count = 0
        # Otherwise, we count up how many times it's present. Because the string is
        # cyclic, any character can be the initial character, so we need to examine
        # all the possible starting characters.
        for j in range(self.length):
            if self.alphabet.areEqualWords(substring, self.valuesAt(j, len(substring))):
                count += 1
        return count
        
    def isPresentExactlyOnce(self, substring):
        """Returns true if @substring appears exactly once as a substring
           of this cyclic string. Sensitive to repeating overlapping 
           substrings unlike the built in count() function"""

        # If the substring is longer than this string, then it can't be a substring.
        if len(substring) > self.length:
            return False

        return self.substringCount(substring) == 1
    
    def isDeBruijnCycle(self, subwordLength):
        for w in self.alphabet.wordsOfLength(subwordLength):
            if not self.isPresentExactlyOnce(w):
                return False
        return True